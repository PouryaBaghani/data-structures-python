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
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.size+=1
        print(f"data {data} sucessfully added to the begining of list.")
        self.display()
        

    def insert_at_end(self, data):
        new_node=Node(data)
        
        if self.is_empty():
            self.head=new_node
            self.size+=1
            return
        currentAddress=self.head                  #starts from beggining
        while currentAddress.next:
            currentAddress=currentAddress.next    #till there is one left
        
        currentAddress.next=new_node              #changing the None address that the last one was pointing to, to the new_node address
        self.size+=1
        print(f"data {data} sucessfully added to the end of list.")
        self.display()

    def insert_at_index(self, data, index):
        if (index < 0 or index > self.size):
            raise IndexError(f"Index {index} is not valid, must be non-negative and less than or equal to list size")
        
        if index==0:
            self.insert_at_begin(data)
            return
        
        new_node=Node(data)
        currentAddress=self.head
        for _ in range(index-1):
            currentAddress=currentAddress.next
            
        new_node.next=currentAddress.next
        currentAddress.next=new_node
        self.size+=1
        print(f"data {data} sucessfully added to list at index {index}.")
        self.display()
        
    def remove_node_at_begin(self):
        if self.is_empty():
            print("List is EMPTY!")
            return None
        
        removedData=self.head.data
        self.head=self.head.next
        self.size-=1
        print(f"data {removedData} sucessfully deleted from the begining of list.")
        self.display()
        return removedData
        
    def remove_node_at_end(self):
        if self.is_empty():
            print("List is EMPTY!")
            return None
        
        if self.head.next==None:
            removedData=self.head.data
            self.head.next=None
            self.size-=1
            print(f"data {removedData} sucessfully deleted from the end of list.")
            self.display()
            return removedData
        
        currentAddress=self.head
        while currentAddress.next.next:          #we need to stop where there is one data left to the last one
            currentAddress=currentAddress.next
            
        removedData=currentAddress.next.data
        currentAddress.next=None
        self.size-=1
        print(f"data {removedData} sucessfully deleted from the end of list.")
        self.display()
        return removedData
    
    def remove_node_at_index(self, index):
        if (index < 0 or index >= self.size):
            raise IndexError(f"Index {index} is not valid, must be non-negative and less than list size")
        
        if index==0:                              #we need this condition cause one before 0 is -1 !!
            self.remove_node_at_begin()
            return
        
        currentAddress=self.head
        for _ in range(index-1):                  #we need to stop one before the one we want to delete
            currentAddress=currentAddress.next
            
        removedData=currentAddress.next.data
        currentAddress.next=currentAddress.next.next
        self.size-=1
        print(f"data {removedData} sucessfully deleted from index {index} of list .")
        self.display()
        return removedData
    
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
        self.display()
        return
        
    def size_of_list(self):
        listSize = 0
        if self.is_empty():
            return listSize

        currentAddress = self.head
        while(currentAddress != None):
           currentAddress = currentAddress.next
           listSize += 1 
        print(f"list size is now= {listSize}")
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
        print("linked list sucessfully inverted!")
        self.display()

    def find(self, target):
        if self.is_empty():
            return False
        
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
    
# TEST
list = Singly_Linked_List()
list2 = Singly_Linked_List()
list2.insert_at_begin(2)
list.concatenate(list2)
list.display()

list.update_node(2,0)
list.insert_at_begin(16)
list.insert_at_index(5,0)
list.insert_at_end(8)
list.insert_at_index(0,2)
#list.insert_at_index(3,5) ----> INDEXERROR!!
list.insert_at_index(22,4)
list.insert_at_begin(32)
list.size_of_list()
#list.update_node(42,8) ----> INDEXERROR!!
list.update_node(42,3)
list.find(16)
list.find(8)
list.find(55)
list.invert() 
list.find(16)
list.find(8)
list.remove_node_at_begin()
list.remove_node_at_end()
list.remove_node_at_index(3)
list.remove_node_at_index(2)
list.remove_node_at_index(0)