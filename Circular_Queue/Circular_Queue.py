"""
===========================================
  🚀 Circular Queue Project - By BASH 🚀
===========================================
"""
class Circular_Queue():
    """Return True if queue has no elements."""
    def __init__(self, size): 
        self.size = size
        self.queue = [None] * size
        self.front = -1 
        self.rear = -1

    def is_empty(self):
        pass #by Shalilian
        
    def is_full(self):
        pass #by Shalilian
            
    def display(self):
        """Show queue contents with front/rear markers."""
        print("[", end="")
        for i in range(self.size):
            print(self.queue[i], end="")
            if i < self.size - 1:
                print(", ", end="")
        print(f"], front={self.front}, rear={self.rear}")

        if self.is_empty():
            print("Queue is EMPTY!")
        elif (self.front <= self.rear):
            for i in range(self.front, self.rear +1):
                print(self.queue[i], end = " ")
            print()
        else:
            for i in range(self.front, self.size):
                 print(self.queue[i], end = " ")
            for i in range(0 , self.rear+1):
                 print(self.queue[i], end = " ")
            print()

    def enqueue(self, data):
        """Insert an element at rear of queue."""
        if self.is_full():
            print(f"Queue is Full! Can't add data {data} to the queue")
            self.display()
        elif self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            print(f"Data {data} added to the queue")
            self.display()
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print(f"Data {data} added to the queue")
            self.display()

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            print("Queue is EMPTY!")
            q.display()
        elif (self.front == self.rear):
            removedItem = self.queue[self.front]
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
            print(f"data {removedItem} was deleted from queue")
            self.display()
            return removedItem
        else:
            removedItem = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            print(f"data {removedItem} was deleted from queue")
            self.display()
            return removedItem
        
    def reverse_queue(self):
        pass #by Shalilian

    def peek(self):
        pass #by Shalilian

q = Circular_Queue(5)
q.display()
q.enqueue(2)
q.enqueue(6)
q.enqueue(10)
q.enqueue(12)
q.enqueue(16)

q.enqueue(18)
q.enqueue(20)

q.dequeue()

q.dequeue()
