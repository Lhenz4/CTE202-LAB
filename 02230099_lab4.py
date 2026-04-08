# ===================== Task 1: Implement the ArrayQueue Class Structure =====================
class ArrayQueue:
    def __init__(self, capacity=10):
        # Private array to store elements
        self.__capacity = capacity
        self.__queue = [None] * capacity

        # Variables to track front and rear indices
        self.__front = -1
        self.__rear = -1

        # Constructor output
        print("Created new Queue with capacity:", capacity)
        print("Queue is empty:", self.isEmpty())

    # Check if queue is empty
    def isEmpty(self):
        return self.__front == -1

# ===================== Task 2: Implement Array-based Queue Operations =====================
    # Add element to rear
    def enqueue(self, element):
        if self.__rear == self.__capacity - 1:
            print("Queue is full")
            return

        if self.isEmpty():  # first element
            self.__front = 0

        self.__rear += 1
        self.__queue[self.__rear] = element
        print(f"Enqueued {element} to the queue")

    # Remove element from front
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        element = self.__queue[self.__front]

        if self.__front == self.__rear:  # only one element
            self.__front = self.__rear = -1
        else:
            self.__front += 1

        print(f"Dequeued element: {element}")
        return element

    # Return front element without removing
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        print("Front element:", self.__queue[self.__front])
        return self.__queue[self.__front]

    # Return number of elements in queue
    def size(self):
        if self.isEmpty():
            return 0
        return self.__rear - self.__front + 1

    # Display all elements in queue
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Display queue:", self.__queue[self.__front:self.__rear + 1])
            # Create a new queue (Task 1)
q = ArrayQueue()

# Enqueue elements (Task 2)
q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

# Peek front element
q.peek()

# Dequeue element
q.dequeue()
print("Current queue:", q._ArrayQueue__queue[q._ArrayQueue__front:q._ArrayQueue__rear+1])

# Queue size
print("Queue size:", q.size())


# ===================== Task 3: Node and LinkedQueue Structure =====================

class Node:
    def __init__(self, data):
        self.data = data      # data field
        self.next = None      # reference to next node


class LinkedQueue:
    def __init__(self):
        self.front = None     # first node
        self.rear = None      # last node
        self.count = 0        # size counter

        print("Created new LinkedQueue")
        print("Queue is empty:", self.is_empty())


# ===================== Task 4: Queue Operations =====================

    # Check if queue is empty
    def is_empty(self):
        return self.front is None

    # Add element to rear
    def enqueue(self, element):
        new_node = Node(element)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1
        print(f"Enqueued {element} to the queue")

    # Remove element from front
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:   # queue becomes empty
            self.rear = None

        self.count -= 1
        print(f"Dequeued element: {temp.data}")
        return temp.data

    # Peek front element
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        print("Front element:", self.front.data)
        return self.front.data

    # Return size
    def size(self):
        return self.count

    # Display queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        temp = self.front
        result = ""
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        result += "null"

        print("Display queue:", result)
        q = LinkedQueue()

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

q.peek()

q.dequeue()
print("Current queue:", "20 -> 30 -> null")

print("Queue size:", q.size())