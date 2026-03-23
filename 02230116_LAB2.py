# Task 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("Created new LinkedList")
        print(f"Current size: {self._size}")
        print(f"Head: {self.head}")

    # Task 2: Basic Operations
    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"Appended {element} to the list")

    def prepend(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1
        print(f"Prepended {element} to the list")

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next

        print(f"Element at index {index}: {current.data}")
        return current.data

    def set(self, index, element):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next

        current.data = element
        print(f"Set element at index {index} to {element}")

    def size(self):
        print(f"Current size: {self._size}")
        return self._size

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"


# Example usage
ls1 = LinkedList()
ls1.append(10)
ls1.get(0)
ls1.set(0, 20)
ls1.get(0)
ls1.size()
ls1.prepend(10)
print("Print Linked list:", ls1)