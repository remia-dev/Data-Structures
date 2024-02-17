# Defining a Tree

class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child == None:
                # Create that node
                current_node.left_child = node(value)
            else:
                self._insert(current_node.left_child, value)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = node(value)
            else:
                self._insert(current_node.right_child, value)
        else:
            print("Value is already in the tree")

    def display(self):
        if self.root != None:
            self._display(self.root)

    def _display(self, current_node):
        # Inorder traversal - Left -> Root -> Right | abc
        '''
        if current_node != None:
            self._display(current_node.left_child)
            print(current_node.value)
            self._display(current_node.right_child)
        '''


        # Preorder traversal - Root -> Left -> Right | bac
        '''
        if current_node != None:
            print(current_node.value)
            self._display(current_node.left_child)
            self._display(current_node.right_child)
        '''


        # Postorder traversal - Root -> Right -> Left | bca
        if current_node != None:
            print(current_node.value)
            self._display(current_node.right_child)
            self._display(current_node.left_child)
    
    # Breadth First Search (BFS) - print by levels
            
    # Adjacency List - list of children of the node 
    
    def makelist(self):
        if self.root != None:
            self._adjacencyList(self.root)
    
    def _adjacencyList(self, current_node):
        d = {}
        '''
        if current_node != None:
            d[current_node.value] = []

            if current_node.left_child:
                d[current_node.value].append(current_node.left_child.value)

            if current_node.right_child:
                d[current_node.value].append(current_node.right_child.value)
                 
            self._adjacencyList(current_node.left_child)
            self._adjacencyList(current_node.right_child)

        print(d)
        return d
        '''
        while current_node != None:
            d[current_node.value].append(current_node.left_child.value)

    
    

    
tree = BinaryTree()
tree.insert('g')
tree.insert('c')
tree.insert('b')
tree.insert('a')
tree.insert('e')
tree.insert('d')
tree.insert('f')
tree.insert('i')
tree.insert('h')
tree.insert('j')
tree.insert('k')
# tree.display()
tree.makelist()