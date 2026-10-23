class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = self.front.next

            #if its last node
            if self.front==None:
                self.rear = None

            temp = None

        else:
            print("Queue is empty...")

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

q = LQueue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.print()

q.dequeue()
q.dequeue()
q.print()

q.dequeue()
q.dequeue()
q.print()
q.dequeue()