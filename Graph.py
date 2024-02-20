import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)  # Assuming an undirected graph

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")

    def draw(self):
        G = nx.Graph()
        for vertex, edges in self.adjacency_list.items():
            for edge in edges:
                G.add_edge(vertex, edge)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        plt.savefig("my_graph.png")

# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'B')
graph.add_edge('D', 'E')
graph.add_edge('E', 'A')

print("Graph adjacency list:")
graph.display()

print("Drawing the graph:")
graph.draw()
