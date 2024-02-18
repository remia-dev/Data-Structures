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
    
            
    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
    
    def _height(self, current_node, current_height):
        if current_node == None: return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)
    
    # Print nodes at a given level
    # Recursive na nababawasan

    # Breadth First Search (BFS) - print by levels
    def bfs(self):
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left_child:
                queue.append(current_node.left_child)
            if current_node.right_child:
                queue.append(current_node.right_child)
        return result
    

    # Adjacency List
    '''
    def adjacencyList(self):
        if self.root != None:
            return self._adjacencyList(self.root)
        else:
            return 0
    
    def _adjacencyList(self, current_node):
        if current_node is None:
            return {}
        adjacency = {current_node.value: [None, None]}
        if current_node.left_child:
            adjacency[current_node.value][0] = current_node.left_child.value
        
        if current_node.right_child:
            adjacency[current_node.value][1] = current_node.right_child.value
        
        adjacency.update(self._adjacencyList(current_node.left_child))
        adjacency.update(self._adjacencyList(current_node.right_child))

        return adjacency
    '''
    def create_adjacency_list(self):
        adjacency_list = {}
        self._create_adjacency_list_recursive(self.root, adjacency_list)
        return adjacency_list
    
    def _create_adjacency_list_recursive(self, current_node, adjacencyList):
        if current_node is None:
            return {}
        left_child_value = current_node.left_child.value if current_node.left_child else None 
        right_child_value = current_node.right_child.value if current_node.right_child else None

        adjacencyList[current_node.value] = (left_child_value, right_child_value)
        self._create_adjacency_list_recursive(current_node.left_child, adjacencyList)
        self._create_adjacency_list_recursive(current_node.right_child, adjacencyList)
            


    
    '''
    def printGivenLevel(self, level):
        if self.root != None:
            self.printGivenLevel(self.root.left_child, level - 1)
            self.printGivenLevel(self.root.right_child, level - 1)
    
    def printLevelOrder(self):
        h = self._height(self.root, 0)
        for i in range(1 + h + 1):
            self.printGivenLevel(self.root, i)
            print()
    '''


            
    # Adjacency List - list of children of the node 
    



    
    

    
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
print(tree.height())
print("BFS traversal: ", tree.bfs())
print("Adjacency List: ", tree.create_adjacency_list())
# tree.printLevelOrder()
# tree.display()
# tree.makelist()