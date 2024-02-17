class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node()

    ''' 
    def begin_insert(self, data):
        current_node = self.head
        current_node.next = data
        current_node = current_node.next
    '''
    def length(self):
        count = 0
        current_node = self.head
        while current_node.next != None:
            count += 1
            current_node = current_node.next
        print(count)
        return count



    def append(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def traverse(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            print(current_node.data)

    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next 
            elems.append(current_node.data)
        print(elems)

    def get(self, index):
        current_node = self.head
        count = 0
        while current_node.next != None:
            current_node = current_node.next
            if count == index:
                print(current_node.data)
                return current_node.data
            count += 1
    
    def erase(self, index):
        current_node = self.head 
        count = 0 
        while current_node.next != None:
            last_node = current_node
            current_node = current_node.next
            if count == index:
                last_node.next = current_node.next
                return
            count += 1
                

                



# LinkedList    





my_list = linkedList()
my_list.append(32)
my_list.append(12)
my_list.append(44)
my_list.append(232)
my_list.append(94)
my_list.display()
my_list.length()
my_list.get(3)
my_list.erase(3)
my_list.display()

        


        

