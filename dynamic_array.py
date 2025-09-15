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

    def add(self, elem):
        # Resize if needed
        if self.len + 1 >= self.capacity:
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity *= 2
            new_arr = [None] * self.capacity
            for i in range(self.len):
                new_arr[i] = self.arr[i]
            self.arr = new_arr

        # Add element
        self.arr[self.len] = elem
        self.len += 1

    def remove_at(self, rm_index):
        if rm_index < 0 or rm_index >= self.len:
            raise IndexError("Index out of bounds")

        data = self.arr[rm_index]
        new_arr = [None] * (self.len - 1)

        for i in range(self.len):
            if i < rm_index:
                new_arr[i] = self.arr[i]
            elif i > rm_index:
                new_arr[i - 1] = self.arr[i]

        self.arr = new_arr
        self.len -= 1
        self.capacity = self.len
        return data

    def remove(self, obj):
        for i in range(self.len):
            if self.arr[i] == obj:
                self.remove_at(i)
                return True
        return False

    def index_of(self, obj):
        for i in range(self.len):
            if self.arr[i] == obj:
                return i
        return -1

    def contains(self, obj):
        return self.index_of(obj) != -1

    def to_string(self):
        if self.len == 0:
            return "[]"
        return ", ".join(str(self.arr[i]) for i in range(self.len))


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
    arr.add(30)
    arr.add(40)
    print(arr.remove(30))  # Output: True
    print(arr.index_of(40))  # Output: 0
    print(arr.contains(50))  # Output: False
    print(arr.contains(40))  # Output: True
    print(arr.remove_at(0))  # Output: 40

    arr.add(10)
    arr.add(20)
    arr.add(30)
    print(arr.to_string())  # Output: 10, 20, 30