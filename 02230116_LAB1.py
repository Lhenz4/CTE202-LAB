class CustomList:
    def __init__(self, capacity=100):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")

    # 1. append(element) - Add element to the end
    def append(self, element):
        if self._size >= self._capacity:
            print("List is full. Cannot append.")
            return
        
        self._data[self._size] = element
        self._size += 1
        print(f"Appended {element} to the list")

    # 2. get(index) - Retrieve element at index
    def get(self, index):
        if index < 0 or index >= self._size:
            print("Index out of bounds")
            return None
        
        value = self._data[index]
        print(f"Element at index {index}: {value}")
        return value

    # 3. set(index, element) - Replace element at index
    def set(self, index, element):
        if index < 0 or index >= self._size:
            print("Index out of bounds")
            return
        
        self._data[index] = element
        print(f"Set element at index {index} to {element}")

    # 4. size() - Return current size
    def size(self):
        print(f"Current size: {self._size}")
        return self._size


# Example Usage
List1 = CustomList()
List1.append(5)
List1.get(0)
List1.set(0, 10)
List1.get(0)
List1.size()