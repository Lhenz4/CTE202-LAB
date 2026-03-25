
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None   

class LinkedStack:
    def __init__(self):
        self.top = None    
        self._size = 0     
        print("Created new LinkedStack")

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        removed = self.top.data
        self.top = self.top.next
        self._size -= 1
        return removed

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def display(self):
        current = self.top
        if current is None:
            print("Stack is empty")
            return
        
        print("Stack elements (top to bottom):")
        while current:
            print(current.data)
            current = current.next


# Example usage
stack1 = LinkedStack()

print("Stack is empty:", stack1.is_empty())

stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.display()
print("Top element:", stack1.peek())
print("Popped:", stack1.pop())
stack1.display()
print("Stack size:", stack1.size())