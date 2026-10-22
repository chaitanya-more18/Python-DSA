class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self, value):
        self.data = value
        self.next = None

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

    def print(self):
        temp = self.top
        print("stack elements are")
        while temp:
            print(temp.data)
            temp = temp.next


st=stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))
st.print()
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
st.print()