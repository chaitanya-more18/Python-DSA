class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Create Linked List
    def Create(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Traverse and print
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Insert at a specific position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Find middle node
    def middle(self):
        temp = self.head
        count = 0

    # Count number of nodes
        while temp:
            count += 1
            temp = temp.next

        if count == 0:
            print("List is empty")
            return

    # Find middle position
        mid = count // 2

    # Traverse to middle node
        temp = self.head
        for i in range(mid):
            temp = temp.next

        print("Middle node:", temp.data)

    # Delete at a specific position
    def delete(self, pos):
        if pos < 1 or self.head is None:
            print("Invalid position")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head
        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None or temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Reverse Linked List
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Sum of every two consecutive nodes (non-overlapping pairs)
    def sum_pairs(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data, "+", temp.next.data, "=",
                  temp.data + temp.next.data)
            temp = temp.next.next

        if temp:
            print("Unpaired node:", temp.data)

# Create Linked List
l1 = LinkedList()
l1.Create(Node(10))
l1.Create(Node(20))
l1.Create(Node(30))
l1.Create(Node(40))
l1.Create(Node(50))

# Call operations
print("Original List:")
l1.display()

print("Insert 90 at position 3:")
l1.insert(Node(90), 3)
l1.display()

l1.middle()

print("Delete node at position 2:")
l1.delete(2)
l1.display()

print("Reverse List:")
l1.reverse()
l1.display()

print("Sum of Consecutive Pairs:")
l1.sum_pairs()
