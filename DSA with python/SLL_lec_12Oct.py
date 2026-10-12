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

    def findmid_del(self):
        temp = temp1 = self.head
        prev = None
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1 = temp1.next.next
            print("Middle Node: ",temp.data)
            prev.next=temp.next
            temp = None

    def del_first_last(self):
        temp = None
        temp1=self.head
        temp1=None
        prev=None
        temp=self.head = self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        temp=None

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

print("After del first and last")
llist.del_first_last()
llist.print()