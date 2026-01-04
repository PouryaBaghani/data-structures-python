<<<<<<< HEAD
"""
===========================================
  🚀 »Linear Queue Project - By BASH 🚀
===========================================
"""
class Linear_Queue():

    def __init__(self, size):  
=======
class Linear_Queue():
    def __init__(self, size):  
        """Initialize an empty queue with given size."""
>>>>>>> a71429edb743a251abab1f68cb69f9116f739156
        self.size = size  
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
<<<<<<< HEAD
        return None  # implemented by Pouria
        
    def is_full(self):
        return None  # implemented by Pouria

    def display(self):
        return None  # implemented by Pouria
=======
        """Check if queue has no elements."""
        if (self.front == -1):
            return True
        else:
            return False
        
    def is_full(self):
        """Check if queue has reached maximum capacity."""
        if (self.rear == self.size -1):
            return True
        else:
            return False

    def display(self):
        """
        Display queue contents in two views:
        1. Only valid elements (front to rear)
        2. Entire array with None values
        """
        if self.is_empty():
            print("Queue is EMPTY!")
            return

        else:
            print("Queue Items: ", end = "")
            for i in range (self.front, self.rear + 1): 
                print(self.queue[i], end = " ")
            print()

            print("Queue: [", end="")
            for i in range(self.size):
                print(self.queue[i], end="")
                if i < self.size - 1:
                    print(", ", end="")
    
            print(f"], front={self.front}, rear={self.rear}")
            return
>>>>>>> a71429edb743a251abab1f68cb69f9116f739156

        

    def enqueue(self, data):
<<<<<<< HEAD
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
=======
        """Add an element to the rear of the queue."""
        if self.is_full(): # When queue is full
            print("Queue is FULL!")
            self.display()
            return

        elif (self.front == -1): # When queue is empty
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

            print(f"Data {data} added to queue")
            self.display()
            return

        else: # When queue has some items already
            self.rear += 1
            self.queue[self.rear] = data

            print(f"Data {data} added to queue")
            self.display()

    def dequeue(self): 
        """Remove and return element from the front of the queue."""
        if self.is_empty(): # When queue is empty
            print("Queue is EMPTY!")
            self.display()
            return
        
        elif (self.front == self.rear): # When queue has exactly one element
>>>>>>> a71429edb743a251abab1f68cb69f9116f739156
            removedItem = self.queue[self.front]
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
<<<<<<< HEAD
            print(f"Data {removedItem} was deleted from queue")
            self.display()
            return removedItem
        else:
            removedItem = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
=======

            print(f"Data {removedItem} was deleted from queue")
            self.display()
            return removedItem
        
        else: # When queue has some items already
            removedItem = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1

>>>>>>> a71429edb743a251abab1f68cb69f9116f739156
            print(f"Data {removedItem} was deleted from queue")
            self.display()
            return removedItem

    def peek(self):
<<<<<<< HEAD
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
=======
        """Return front element without removing it."""
        if self.is_empty():
            print("Queue is EMPTY!")
            return
        
        return self.queue[self.front]
    
    def reverse_queue(self):
        """Create and return a new queue with elements in reverse order."""
        if self.is_empty():
            return Linear_Queue(self.size)
        
        newQueue = Linear_Queue(self.size)
        count = self.rear - self.front + 1 # Number of elements
        newQueue.front = 0 # always begin to put reverse ordered elements from zero index 
        newQueue.rear = count -1 # Last occupied index

        # Copy elements in reverse order
        for i in range(count): 
            originalIndex = self.front + i
            newIndex = count - 1 - i
            newQueue.queue[newIndex] = self.queue[originalIndex]

        return newQueue

# Test
obj = Linear_Queue(3)
obj.enqueue(2)
obj.enqueue(6)
obj.enqueue(10)
print(f"the peek item is: {obj.peek()}")
reversed = obj.reverse_queue()
obj.display()
reversed.display()
obj.dequeue()
obj.dequeue()
obj.dequeue()
reversed = obj.reverse_queue()
>>>>>>> a71429edb743a251abab1f68cb69f9116f739156
