# Reverse queue using stack
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element: ",temp.data)
            self.top=self.top.next
            return temp.data

    def print(self):
        temp = self.top
        print("stack elements are")
        while temp:
            print(temp.data)
            temp = temp.next

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
            dequed_data = temp.data
            #if its last node
            if self.front==None:
                self.rear = None
            temp = None
            return dequed_data
        else:
            print("Queue is empty...")

    def is_empty(self):
        return self.front is None
    

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

def reverse_stack(s1):
    q1 = LQueue()
    while not s1.isempty():
        q1.enqueue(Node(s1.pop()))
    q1.print()

# que = LQueue()
# que.enqueue(Node(15))
# que.enqueue(Node(67))
# que.enqueue(Node(55))
# que.enqueue(Node(24))
# que.enqueue(Node(11))

# que.print()

s = stack()
s.push(Node(11))
s.push(Node(21))
s.push(Node(31))
s.push(Node(41))
s.print()
reverse_stack(s)