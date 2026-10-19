class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None


    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return

        t = self.head
        while t.next:
            t=t.next

        newNode.prev = t
        t.next = newNode

    def print(self):
        if self.head == None:
            print("Linked list is empty!")
            return

        t = self.head
        print("None <- ",end="")

        while t:
            print(f"{t.data} -> ",end="")
            t=t.next

        print("None")

    def insert(self,data,posi):
        if self.head == None and posi > 1:
            print("Invalid position")
            return

        newNode = Node(data)
        if posi == 1:
            newNode.next = self.head
            self.head.prev = newNode
            self.head =newNode
            return

        count = 1
        p = self.head
        #Invalid position and condition
        while count != posi-1 and p.next:
            p = p.next
            count+=1

        newNode.next = p.next
        newNode.prev = p
        #Last position
        if newNode.next: #Not Last Node
            newNode.next.prev = newNode
        p.next = newNode

    def removeNodeByData(self,data):
        if self.head == None:
            print("Linked List is empty!")
            return

        t = self.head
        if t.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        while t.data!=data:
            t=t.next
            if t == None:
                print("Value is not present in the list!")
                return

        t.prev.next = t.next
        if t.next:
            t.next.prev = t.prev
        t = None


    def printByReverse(self):
        if self.head == None:
            print("Linked list is empty!")
            return

        t= self.head
        while t.next:
            t=t.next

        while t:
            print(t.data,end=" -> ")
            t=t.prev

        print("None")


dll = DoublyLinkedList()
dll.append(11)
dll.append(22)
dll.append(33)
dll.append(44)
dll.print()
dll.insert(1,1)
dll.print()
dll.insert(999,300)
dll.print()
dll.removeNodeByData(1)
dll.print()
dll.printByReverse()