
# Part 2 Implemented by Ugyen Lhendup (02203116)
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

# LinkedQueue class
class LinkedQueue:
    def __init__(self):
        self.front = None  # first node
        self.rear = None   # last node
        self._size = 0     # size counter
        print("Created new LinkedQueue")

    # Check if queue is empty
    def is_empty(self):
        return self._size == 0

    # Return the size of the queue
    def size(self):
        return self._size

    # Add element to the rear
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear:  # if queue is not empty
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:  # if queue was empty
            self.front = new_node
        self._size += 1
        print(f"Enqueued {element} to the queue")

    # Remove and return element from front
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # if queue becomes empty
            self.rear = None
        self._size -= 1
        print(f"Dequeued element: {removed_data}")
        return removed_data

    # Peek at the front element without removing
    def peek(self):
        if self.is_empty():
            print("Queue is empty, nothing to peek")
            return None
        return self.front.data

    # Display all elements in the queue
    def display(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        print("Display queue:", elements)

# Example usage
queue = LinkedQueue()
print("Queue is empty:", queue.is_empty())

queue.enqueue(10)
queue.display()

queue.enqueue(20)
queue.display()

queue.enqueue(30)
queue.display()

print("Front element:", queue.peek())

queue.dequeue()
print("Current queue:", end=" ")
current = queue.front
while current:
    print(current.data, end=" -> ")
    current = current.next
print("null")

print("Queue size:", queue.size())