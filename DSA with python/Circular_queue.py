class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class CQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front=self.rear=new_node

        # new addition in cqueue
        self.rear.next = self.front

    def dequeue(self):
        if self.front:  #at least one node in q
            temp = self.front

            # if its last node
            if self.front==self.rear:   # only one node in q
                self.front = self.rear = None
                print("now queue is empty...")
            else: 
                self.front = self.front.next
                self.rear.next = self.front # added for circular
            temp = None
        else:
            print("Queue is empty...")

    def print(self):

        if not self.front:
            print("Queue is empty")
            return
        
        temp = self.front
        # change in loop for cq
        while True:
            print(temp.data, end="->")
            temp=temp.next
            if temp==self.front:
                break
        print("None")

q = CQueue()
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