"""
===========================================
  🚀 Queue with Stack Project - By BASH 🚀
===========================================
"""
class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def push(self, data):
        self.top += 1
        self.stack[self.top] = data
        print(f"Data {data} added to stack")
        return 

    def pop(self):
        if self.top == -1:
            print("Stack Underflow! Can not delete anything.")
            return None
        data = self.stack[self.top]
        self.top -= 1
        
        return data

    def is_empty(self):
        if (self.top == -1):
            return True
        return False
    
    def is_full(self):
        if (self.top == self.size - 1):
            return True
        return False
class Queue_With_Stack:
    def __init__(self, size):
        self.stack1 = Stack(size)   # for enqueue
        self.stack2 = Stack(size)   # for dequeue
        self.size = size

    def enqueue(self, data):
        if self.stack1.is_full():
            print("Queue Overflow! Cannot add more data.") 
            return
        
        self.stack1.push(data)
        self.display()
        return

    def dequeue(self):
        if self.stack2.is_empty():
            while self.stack1.is_full():
                self.stack2.push(self.stack1.pop())

        if self.stack2.is_empty():
            print("Queue is Empty!")
            return

        removedData = self.stack2.pop()
        print(f"data {removedData} was deleted!")
        self.display()

    def display(self):
        print("Queue:", end=" ")

        # printting the stack2 first, cause it has older data
        i = self.stack2.top
        while i >= 0:
            print(self.stack2.stack[i], end=" ")
            i -= 1

        # printting the stack1 after, cause it has newer data
        i = 0
        while i <= self.stack1.top:
            print(self.stack1.stack[i], end=" ")
            i += 1

        print()

qs= Queue_With_Stack(5)

qs.enqueue(6)
qs.enqueue(3)
qs.enqueue(23)
qs.enqueue(9)
qs.enqueue(15)
qs.enqueue(78)

qs.dequeue()
qs.dequeue()
qs.enqueue(78)   