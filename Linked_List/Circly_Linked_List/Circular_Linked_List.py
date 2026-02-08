"""
=============================================
  🚀 Circular Linked List Project - By BASH 🚀
=============================================
"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.size = 0

class Circular_Linked_list():
    def __init__(self):
        self.head = None

    def is_empty(self):
        if (self.head is None):
            return True
        return False
    
    def display(self):
        if self.is_empty():
            print("List is EMPTY!")
            return
        
        currentAddress = self.head
        print(currentAddress.data, end = " -> ")
        currentAddress = currentAddress.next

        while currentAddress != self.head:
          print(currentAddress.data, end=" -> ")
          currentAddress = currentAddress.next

        print(f"back to head {self.head.data}")
        return 

    def insert_at_begin(self, data):
        #By Baqani
        pass

    def remove_node_at_begin(self):
        #By Baqani
        pass

    def insert_at_end(self, data):
        #By Baqani
        pass

    def remove_node_at_end(self):
        #By Baqani
        pass

    def insert_at_index(self, data, index):
        #By Baqani
        pass
        
    def remove_node_at_index(self, index):
        #By Baqani
        pass
    
    def update_node(self, newData, index):
        if (index < 0):  
            raise IndexError("Index must be non-negative")

        if self.is_empty():
            print ("There is no data to update")
            return
        
        currentAddress = self.head
        steps = 0

        while((steps < index) and (currentAddress.next != self.head)):
            currentAddres = currentAddres.next
            steps += 1

        if steps != index:
            raise IndexError("Index out of range.")
        
        currentAddress.data = newData

    def size_of_list(self):
        if self.is_empty():
            print("List is empty")
            return 0

        currentAddress = self.head
        listSize = 1

        while (currentAddress.next != self.head):
            currentAddress = currentAddress.next
            listSize += 1

        return listSize

    def concatenate(self, otherList):
        if self.is_empty():
            self.head = otherList.head
            return 

        if otherList is self:
            return

        elif otherList.is_empty():
            return
        
        currentAddress1 = self.head
        while(currentAddress1.next != self.head):
            currentAddress1 = currentAddress1.next

        currentAddress2 = otherList.head 
        while(currentAddress2.next != otherList.head):
            currentAddress2 = currentAddress2.next

        currentAddress1.next = otherList.head
        currentAddress2.next = self.head

    def invert(self):
        if((self.is_empty()) or (self.head.next == self.head)):
            return
        
        prevNode = self.head
        currentAddress = self.head.next

        while(currentAddress != self.head):
            nextNode = currentAddress.next
            currentAddress.next = prevNode
            prevNode = currentAddress
            currentAddress = nextNode

        self.head.next = prevNode
        self.head = prevNode

    def find(self, target):
        if self.is_empty():
            print("List is EMPTY!")
            return -1
        
        size = self.size_of_list()
        currentAddress = self.head

        for index in range(size):
            if(currentAddress.data == target):
                return index
            
            currentAddress = currentAddress.next

        print(f"Data {target} wasn't in linked list")
        return -1
         

q = Circular_Linked_list()
q.insert_at_begin(5)
q.insert_at_begin(6)
q.insert_at_begin(8)
print(q.remove_node_at_index(1))
q.display()