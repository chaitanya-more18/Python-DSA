class Node:
    def __init__(self, pid, name, prio):
        self.pid = pid
        self.name = name
        self.prio = prio
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def addProcess(self, pid, name, prio):
        if prio < 1 or prio > 4:
            print("Invalid Priority! Must be between 1 and 4.")
            return

        newNode = Node(pid, name, prio)

        # inserting into empty queue
        if self.front == None:
            self.front = newNode
            return

        # inserting when queue isn't empty and for first position!
        t = self.front
        if t.prio > newNode.prio:
            newNode.next = t
            self.front = newNode
            return

        else:
            prev = None
            while t and newNode.prio >= t.prio:
                prev = t
                t = t.next

            prev.next = newNode
            newNode.next = t

    def deque(self):
        if self.front:
            temp = self.front
            print(f"Process executed: PID {temp.pid} ({temp.name})")
            self.front = self.front.next
        else:
            print("Queue is empty.")

    def display_next(self):
        if self.front == None:
            print("Queue is empty.")
        else:
            print(f"Next Process -> PID: {self.front.pid}, Name: {self.front.name}, Priority: {self.front.prio}")

    def display_all(self):
        if self.front == None:
            print("Queue Underflow")
            return

        t = self.front
        print("Pending Processes: ")
        while t:
            print(f"PID: {t.pid} | Name: {t.name} | Prio: {t.prio}")
            t = t.next

        print("-------------------")

    def count(self):
        c = 0
        t = self.front
        while t:
            c += 1
            t = t.next
        print("Total pending processes:", c)


PQ = PriorityQueue()
PQ.addProcess(1, "P1", 4)
PQ.addProcess(2, "P2", 2)
PQ.addProcess(3, "P3", 1)
PQ.addProcess(4, "P4", 3)
PQ.display_all()
PQ.deque()
PQ.display_all()
PQ.display_next()
PQ.count()