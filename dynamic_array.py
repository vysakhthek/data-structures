class Array:
    def __init__(self, capacity=16)
        if capacity < 0:
            raise ValueError(f"Illegal Capacity: {capacity}") 
            self.capacity = capacity
            self.len = 0
            self.arr = [None] * capacity