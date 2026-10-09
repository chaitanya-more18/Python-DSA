class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


    def insert(self, new_data):
        
        new_node = Node(new_data)
        temp = self
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node        

    def print(self):
        temp = self
        while temp is not None:
            print(temp.data)
            temp = temp.next
            
n1 = Node(10)
n1.insert(20)
n1.insert(30)

n1.print()