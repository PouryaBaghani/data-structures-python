class Array():
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def display(self):
        for i in range(self.size):
            print(self.array[i], end = " ")

    def insert(self, data, index):
        if  self.size >= self.capacity:
            print("Array is full")
            return
        
        if index < 0 or index > self.size:
            print("index is not valid")
            return
        
        i = self.size - 1
        while i >= index:
            self.array[i + 1] = self.array[i]
            i -= 1

        self.array[index] = data
        self.size += 1
        print(f"data {data} inserted")
        return

    def remove(self, index):
        if index < 0 or index >= self.size:
            print("index is not valid")
            return
        
        if self.size == 0:
            print("Array is empty")
            return
        
        removedData = self.array[index]
        i = index
        while i < self.size -1:
            self.array[i] = self.array[i + 1]
            i += 1
        
        self.array[self.size - 1] = None
        self.size -= 1
        return removedData

    def find(self, data):
        for i in range (self.size):
            if data == self.array[i]:
                return i
        print("data not found")
        return
    
q = Array(5)
q.insert(8, 0)
q.insert(9, 1)
q.insert(10, 2)
q.insert(11, 3)
q.insert(12, 4)

q.display()