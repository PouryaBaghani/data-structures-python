"""
===========================================
  🚀 Stack Project - By BASH 🚀
===========================================
"""
class Stack():
    def __init__(self, size):
        """Initialize a stack with a fixed maximum size."""
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def display(self):
        """Print the stack contents from top to bottom."""
        if self.is_empty():
            print("-----")
            print("Stack is EMPTY!")
            print("-----")
            return
        
        i = 0
        while i <= self.top:
            i += 1

        i -= 1
        while i >= 0:
            if i == self.top:
                print(f"| {self.stack[i]} |  <- top")
            else:
                print(f"| {self.stack[i]} |")
            i -= 1 

        print("-----")

    def is_empty(self):
        """Return True if the stack has no elements."""
        if (self.top == -1):
            return True
        return False
        
    def is_full(self):
        """Return True if the stack is at maximum capacity."""
        if (self.top == self.size - 1):
            return True
        return False

    def push(self, data):
       pass # by Shalilian

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            print("Stack Underflow")
            return
        
        removedItem = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        print(f"Data {removedItem} deleted from stack")
        return removedItem
     
    def peek(self):
        pass # by Shalilian