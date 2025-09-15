class Array:
    def __init__(self, capacity=16):
        if capacity < 0:
            raise ValueError(f"Illegal Capacity: {capacity}") 
        self.capacity = capacity
        self.len = 0
        self.arr = [None] * capacity

    def size(self):
        return self.len
    
    def is_empty(self):
        return self.size() == 0
    
    def get(self, index):
        return self.arr[index]

    def set(self, index, element):
        self.arr[index] = element
    
    def clear(self):
        for i in range(self.capacity):
            self.arr[i] = None
        self.len = 0

if __name__ == "__main__":
    arr = Array(5)
    arr.set(0, 10)
    arr.set(1, 20)
    arr.len = 2
    print(arr.size())  # Output: 2
    print(arr.get(0))  # Output: 10
    print(arr.get(1))  # Output: 20
    print(arr.is_empty())  # Output: False

    arr.clear()
    print(arr.size())  # Output: 0
    print(arr.is_empty())  # Output: True