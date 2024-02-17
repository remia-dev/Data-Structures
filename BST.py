# Creation of Binary search trees

# Root node, Levels, leaf node

class node:
    def __init__(self, value = None):
        self.value = value 
        self.left_child = None
        self.right_child = None
        self.parent = None

class BinarySearchTree:
    # Constructor
    def __init__(self):
        self.root = None

    # There are two functions: one public and private; private functions are recursive
    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = node(value)
                # Set Parent
                current_node.left_child.parent = current_node
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = node(value)
                # Set Parent
                current_node.right_child.parent = current_node
            else:
                self._insert(value, current_node.right_child)
        else:
            print(" Value already in tree")

    def display(self):
        if self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self, current_node):
        # Inorder traversal
        if current_node != None:
            self._print_tree(current_node.left_child)
            print(current_node.value)
            self._print_tree(current_node.right_child)

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
    
    def search(self, value):
        if self.root != None:
            return self._search(self.root, value)
        else:
            return False
    
    def _search(self, current_node, value):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._search(current_node.left_child, value) 
        elif value > current_node.value and current_node.right_child != None:
            return self._search(current_node.right_child, value)
        else:
            return False
        
    def find(self, value):
        if self.root != None:
            return self._find(self.root, value)
        else:
            return None
        
    def _find(self, current_node, value):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left_child != None:
            return self._find(current_node.left_child, value)
        elif value > current_node.value and current_node.right_child != None:
            return self._find(current_node.right_child, value)
    
    def delete_value(self, value):
        return self.delete_node(self.find(value))
    
    def delete_node(self, node):
        # Protect against deleting a node not found in the tree
        if node == None or self.find(node.value) == None:
            print("Node not found in the tree")
            return None
        
        # Returns the node with min value in the tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current
        
        # Returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left_child != None: num_children += 1
            if n.right_child != None: num_children += 1
            return num_children
        
        # Get the parent of the node to be deleted 
        node_parent = node.parent

        # Get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operations into dfirrerent cases 
        # Case 1 (node has no children)
        if node_children == 0:
            # If you deleted the root node it would delete the entire tree 
            if node_parent != None:
                if node_parent.left_child == node:
                    node_parent.left_child = None 
                else:
                    node_parent.right_child = None
            else:
                self.root = None


        # Case 2 (node has 1 child)
        if node_children == 1:
            # Get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            # If you delete the root node it would delete entire tree
            # In this case it would replace the node to be deleted with its child
            if node_parent != None:
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child
            
            # Correct the parent pointer in node
            child.parent = node_parent

        # Cases 3 (node has two children)
        if node_children == 2:
            # Get the inorder succesort of the deleted node
            successor = min_value_node(node.right_child)

            # Copy the inorder successor's value to the node holding the value we wishedd to delete
            node.value = successor.value 

            # Delete the inorder successor now that its value is copied to another node
            self.delete_node(successor)

    # Naive approah in validating BST
    '''
    def validate_bst(self, min, max):
        if self.root == None:
            return True
        if (self.root.value > min and self.root.value < max and validate_bst(self.root.left_child, min, self.root.value))
    '''


        



'''
def fill_tree(tree, num_elems = 100, max_int = 1000):
    from random import randint
    for _ in range(num_elems):
        curr_elem = randint(0, max_int)
        tree.insert(curr_elem)
    return tree
'''


my_tree = BinarySearchTree()
my_tree.insert(23)
my_tree.insert(5)
my_tree.insert(9)
my_tree.insert(4)
my_tree.insert(11)
my_tree.insert(16)
my_tree.display()
print("Tree height is: " + str(my_tree.height()))
print(my_tree.search(9))
print(my_tree.search(30))