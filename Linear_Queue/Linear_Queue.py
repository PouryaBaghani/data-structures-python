"""
===========================================
  🚀 »Linear Queue Project - By BASH 🚀
===========================================
"""
class Linear_Queue():

    def __init__(self, size):  
        self.size = size  
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return None  # implemented by Pouria
        
    def is_full(self):
        return None  # implemented by Pouria

    def display(self):
        return None  # implemented by Pouria

        

    def enqueue(self, data):
        if self.is_full():
            print("full")
            self.display()
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            print(f"Data {data} added to queue")
            self.display()
        else:
            self.rear += 1
            self.queue[self.rear] = data
            print(f"Data {data} added to queue")
            self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is EMPTY!")
            self.display()
            return
        elif(self.front == self.rear):
            removedItem = self.queue[self.front]
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
            print(f"Data {removedItem} was deleted from queue")
            self.display()
            return removedItem
        else:
            removedItem = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            print(f"Data {removedItem} was deleted from queue")
            self.display()
            return removedItem

    def peek(self):
        return None  # implemented by Pouria

    
    def reverse_queue(self):
        return None  # implemented by Pouria
    


q = Linear_Queue(3)
q.enqueue(2)
q.enqueue(6)
q.enqueue(10)


print(q.peek())
w=q.reverse_queue()
q.display()
w.display()
