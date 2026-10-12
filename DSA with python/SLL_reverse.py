class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    tmep = None
    #Reversing a LL
    def reverse(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode = curr.next
            curr.next=prev
            prev = curr
            curr = nextnode
        self.head = prev
    def print(self):
        print("List elements : ")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
            print("None")

llist = LinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

llist.head = node1      
node1.next = node2   
node2.next = node3     
print("Before Reverse:")
llist.print()

llist.reverse()

print("\nAfter Reverse:")
llist.print()