##Part 1: Stack Implementation using Array
##Task 1: Implementthe ArrayStack Class Structure
class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * capacity  # underlying array
        self.top = -1  # indicates empty stack
        print(f"Created new ArrayStack with capacity: {capacity}")
        print(f"Stack is empty: {self.is_empty()}")

    # Push operation
    def push(self, element):
        if self.top == self.capacity - 1:
            print("Stack Overflow! Cannot push element.")
            return
        self.top += 1
        self.stack[self.top] = element
        print(f"Pushed {element} to the stack")

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        element = self.stack[self.top]
        self.top -= 1
        print(f"Popped element: {element}")
        return element

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        print(f"Top element: {self.stack[self.top]}")
        return self.stack[self.top]

    # Check if stack is empty
    def is_empty(self):
        return self.top == -1

    # Size of stack
    def size(self):
        return self.top + 1

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Display stack:", self.stack[:self.top + 1])
            
            # Create stack
s = ArrayStack(10)

# Operations
s.push(10)
s.display()

s.push(20)
s.display()

s.push(30)
s.display()

s.peek()

s.pop()

print("Stack size:", s.size())
s.display()

##Part 2: Stack Implementation using Linked List
##Task 3 & 4: Node and LinkedStack Classes
# Node class to represent each element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None  # reference to the top node
        self._size = 0
        print("Created new LinkedStack")
        print(f"Stack is empty: {self.is_empty()}")

    # Push element onto the stack
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top  # point new node to current top
        self.top = new_node       # update top
        self._size += 1
        print(f"Pushed {element} to the stack")

    # Pop element from the top
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        popped_data = self.top.data
        self.top = self.top.next  # move top to next node
        self._size -= 1
        print(f"Popped element: {popped_data}")
        return popped_data

    # Peek top element without removing
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data

    # Check if stack is empty
    def is_empty(self):
        return self.top is None

    # Return current size
    def size(self):
        return self._size

    # Display stack elements
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Display stack:", elements)
        # Create linked stack
stack = LinkedStack()

# Push elements
stack.push(10)
stack.display()

stack.push(20)
stack.display()

stack.push(30)
stack.display()

stack.peek()

stack.pop()

# Display remaining stack in linked style
current = stack.top
print("Current stack:", end=" ")
while current:
    print(current.data, end=" -> ")
    current = current.next
print("null")

print("Stack size:", stack.size())