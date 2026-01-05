"""
=============================================
  🚀 Singly Linked List Project - By BASH 🚀
=============================================
"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Singly_Linked_List():
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        if (self.head is None):
            return True
        return False

    def display(self):
        if self.is_empty():
            print("List is EMPTY!")
            return
        
        currentAddress = self.head
        while currentAddress != None:
          print(currentAddress.data, end=" -> ")
          currentAddress = currentAddress.next
        print("None")
        return 

    def insert_at_begin(self, data):
        pass #by Shalilian

    def insert_at_end(self, data):
        pass #by Shalilian

    def insert_at_index(self, data, index):
        pass #by Shalilian

    def remove_node_at_begin(self):
        pass #by Shalilian
    
    def remove_node_at_end(self):
        pass #by Shalilian
    
    def remove_node_at_index(self, index):
        pass #by Shalilian
    
    def update_node (self, newData, index):
        if (index < 0):
            raise IndexError(f"Index {index} is not valid, must be non-negative")
        
        if self.is_empty():
            return
        
        if index >= self.size:
            raise IndexError(f"Index {index} is out of range")

        currentAddress = self.head
        for i in range (index):
            currentAddress = currentAddress.next

        currentAddress.data = newData
        print(f"index {index} updated to {newData}") 
        return
        
    def size_of_list(self):
        listSize = 0
        if self.is_empty():
            return listSize

        currentAddress = self.head
        while(currentAddress != None):
           currentAddress = currentAddress.next
           listSize += 1 

        return listSize

    def concatenate(self, otherList):
        '''Join another linked list at the end of the current one.'''
        if self.is_empty():
            self.head = otherList.head
            self.size = otherList.size
            print("lists concatenated")
            return

        currentAddress = self.head
        while(currentAddress.next):
            currentAddress = currentAddress.next

        currentAddress.next = otherList.head
        print("lists concatenated")
        self.size += otherList.size
        return

    def invert(self):
        prev = None
        currentAddress = self.head

        while (currentAddress):
            nextNode = currentAddress.next 
            currentAddress.next = prev 
            prev = currentAddress 
            currentAddress = nextNode
        
        self.head = prev

    def find(self, target):
        if self.is_empty():
            return
        
        index = 0
        currentAddress = self.head
        while(currentAddress):
            if(currentAddress.data == target):
                print(f"data {target} was found at index {index}")
                return index
            
            index += 1
            currentAddress = currentAddress.next

        print(f"Data {target} wasn't in linked list")
        return False