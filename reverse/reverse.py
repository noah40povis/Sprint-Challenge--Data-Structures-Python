class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    #set prev to none to avoid argument error . previous doesnt seem to be doing anything
    #use recutsion 
    def reverse_list(self, node, prev=None):
        #check if node is existent 
         if node is not None:
             #and if next node is none to find the end 
            if node.get_next() == None:
                #set head to this node  
                self.head = node
                return 
              #run recursion  on node to get next node   
            self.reverse_list(node.get_next())
            #set dummy variable to next node 
            temp = node.get_next()
            #set next to the current node
            temp.set_next(node)
            #set node to set_next . essentially make a loop around itself 
            node.set_next(node)
        
    
