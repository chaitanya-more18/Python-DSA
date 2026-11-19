class Node:
    def __init__(self, pid, name, prio):
        self.pid = pid
        self.name = name
        self.prio = prio
        self.next = None


class CPU_Scheduler:
    def __init__(self):
        self.front = None

    def enqueue(self, pid, name, prio):
        if prio < 1 or prio > 4:
            print("Invalid Priority! Enter between 1 and 4.")
            return

        newNode = Node(pid, name, prio)

        # inserting when queue is empty
        if self.front == None:
            self.front = newNode
            print("Process added:", name)
            return

        # inserting at first position if new process has higher priority
        t = self.front
        if t.prio > newNode.prio:
            newNode.next = t
            self.front = newNode
            print("Process added:", name)
            return
        else:
            prev = None
            while t and newNode.prio >= t.prio:
                prev = t
                t = t.next

            prev.next = newNode
            newNode.next = t
            print("Process added:", name)

    def dequeue(self):
        if self.front:
            temp = self.front
            print(f"Executing Process: {temp.pid} - {temp.name} (Priority {temp.prio})")
            self.front = self.front.next
        else:
            print("No processes in queue.")

    def display_next(self):
        if self.front == None:
            print("No next process, queue is empty.")
        else:
            print(f"Next Process: {self.front.pid} - {self.front.name} (Priority {self.front.prio})")

    def display_all(self):
        if self.front == None:
            print("Queue is empty")
            return

        t = self.front
        print("\nPending Processes:")
        while t:
            print(f"PID: {t.pid} | Name: {t.name} | Priority: {t.prio}")
            t = t.next
        print("-------------------")

    def count(self):
        c = 0
        t = self.front
        while t:
            c += 1
            t = t.next
        print("Total pending processes:", c)


# menu driven program
pq = CPU_Scheduler()

while True:
    print("\n1. Add Process")
    print("2. Execute Process")
    print("3. View Next Process")
    print("4. Display All Processes")
    print("5. Count Processes")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        pid = input("Enter Process ID: ")
        name = input("Enter Process Name: ")
        print("Priority: 1-System, 2-Interactive, 3-Background, 4-Low")
        prio = int(input("Enter Priority: "))
        pq.enqueue(pid, name, prio)

    elif ch == 2:
        pq.dequeue()

    elif ch == 3:
        pq.display_next()

    elif ch == 4:
        pq.display_all()

    elif ch == 5:
        pq.count()

    elif ch == 6:
        print("Exiting...")
        break

    else:
        print("Wrong choice!")