"""
=============================================
  🚀 Doubly Linked List Project - By BASH 🚀
=============================================
"""
class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doubly_Linked_list():
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        if self.head == None:
            return True
        return False   
    
    def display(self):
        if self.is_empty():
            print("List is EMPTY!")
            return

        currentAddress = self.head
        print("None <- ", end="")
        while currentAddress is not None:
            print(currentAddress.data, end=" ")
            if currentAddress.next is not None:
                print("<-> ", end="")
            currentAddress = currentAddress.next

        print("-> None")
        return

    def insert_at_begin(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            print(f"Data {data} inserted")
            self.size += 1
            return
        
        newNode.next = self.head
        self.head.prev = newNode        # the differece bitween singly & doubly! with this line, 
                                        # the previous first node will point to the new first node as its previous one.
        self.head = newNode
        print(f"Data {data} inserted")
        self.size += 1
        return
    
    def remove_node_at_begin(self):
        if self.is_empty():
            print("List is empty. no data to remove")
            return
        
        removedData = self.head.data
        if self.head.next == None: #only one node
            self.head = None
            print(f"Data {removedData} removed")
            self.size -= 1
            return removedData
        
        self.head = self.head.next              # head points to the second one and makes it the first.
        self.head.prev = None                   # changing the new first node's prev to None.
        print(f"Data {removedData} removed")
        self.size -= 1
        return removedData
        
    def insert_at_end(self, data):
        if self.is_empty():
            self.insert_at_begin(data)
            return
        
        newNode = Node(data)
        currentAddress = self.head
        while currentAddress.next != None:
            currentAddress = currentAddress.next

        currentAddress.next = newNode
        newNode.prev = currentAddress
        print(f"Data {data} inserted")
        self.size += 1
        return
    
    def remove_node_at_end(self):
        if self.is_empty():
            print("List is empty. no data to remove")
            return
        
        if self.head.next == None:
            return self.remove_node_at_begin()
        
        currentAddress = self.head
        while currentAddress.next != None:
            currentAddress = currentAddress.next
            
        removedData = currentAddress.data
        currentAddress.prev.next = None        # the data before the one that we want to delete, its next changes to None.
        print(f"Data {removedData} removed")
        self.size -= 1
        return removedData
        
    def insert_at_index(self, data, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        
        elif index > self.size:
            raise IndexError("Index out of range")
        
        elif index == 0:
            self.insert_at_begin(data)
            return
        
        if index == self.size:          
            self.insert_at_end(data)
            return
        
        newNode = Node(data)
        currentAddress = self.head
        for _ in range (index - 1):
            currentAddress = currentAddress.next
        
        newNode.next = currentAddress.next
        newNode.prev = currentAddress
        currentAddress.next.prev = newNode
        currentAddress.next = newNode
        print(f"Data {data} inserted")
        self.size += 1
        return
    
    def remove_node_at_index(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        
        elif index >= self.size:
            raise IndexError("Index out of range")
        
        elif self.is_empty():
            print("List is empty. no data to remove")
            return
        
        elif index == 0:
            return self.remove_node_at_begin()
        
        elif index == self.size - 1:
            return self.remove_node_at_end()
        
        currentAddress = self.head
        for _ in range(index):
            currentAddress = currentAddress.next
        
        removedData = currentAddress.data
        currentAddress.prev.next = currentAddress.next
        currentAddress.next.prev = currentAddress.prev
        print(f"Data {removedData} removed")
        self.size -= 1
        return removedData
    
    def update_node(self, index, newData):
        if (index < 0):
            raise IndexError(f"Index {index} is not valid, must be non-negative")
        
        if self.is_empty():
            return
        
        if index >= self.size:
            raise IndexError(f"Index {index} is out of range")

        currentAddress = self.head
        for _ in range (index):
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
        if self.head==None:
            self.head=otherList.head
            self.size=otherList.size
            print("lists concatenated!")
            return
        
        currentAddress=self.head
        while currentAddress.next:
            currentAddress=currentAddress.next
            
        currentAddress.next=otherList.head
        if otherList.head:
            otherList.head.prev=currentAddress
            
        self.size += otherList.size
        print("lists concatenated!")
        
    def invert(self):
        currentAddress=self.head
        temp=None
        
        while currentAddress:
            temp=currentAddress.prev                  # we want to change its prev so we need to save it first.
            currentAddress.prev=currentAddress.next
            currentAddress.next=temp
            currentAddress=currentAddress.prev        # we replace them so for going to the next one we should use .prev instead of .next
            
        if temp:
            self.head = temp.prev
        print("linked list sucessfully inverted!")
        self.display()
        
           

    def find_data(self, target):
        if self.is_empty():
            print("List is EMPTY!")
            return False
        
        currentAddress = self.head
        index = 0
        while currentAddress:
            if currentAddress.data == target:
                print(f"Data {target} found at index {index}.")
                return index
            
            currentAddress = currentAddress.next
            index += 1
            
        print(f"Data {target} wasn't in linked list")
        return False
          
    

def menu():
    list = Doubly_Linked_list()
    
    print("\n--- Doubly Linked List Menu ---")
    print("1. Display list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at index")
    print("5. Remove at beginning")
    print("6. Remove at end")
    print("7. Remove at index")
    print("8. Invert list")
    print("9. Find data")
    print("10. Size of list")
    print("11. Update node data")
    print("0. Exit")
    
    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            list.display()

        elif choice == "2":
            data = input("Enter data to insert: ")
            list.insert_at_begin(data)

        elif choice == "3":
            data = input("Enter data to insert: ")
            list.insert_at_end(data)

        elif choice == "4":
            data = input("Enter data to insert: ")
            index = int(input("Enter index: "))
            list.insert_at_index(data, index)

        elif choice == "5":
            list.remove_node_at_begin()

        elif choice == "6":
            list.remove_node_at_end()

        elif choice == "7":
            index = int(input("Enter index: "))
            list.remove_node_at_index(index)

        elif choice == "8":
            list.invert()

        elif choice == "9":
            target = input("Enter data to find: ")
            list.find_data(target)

        elif choice == "10":
            list.size_of_list()
        
        elif choice == "11":
            newData = input("Enter new data: ")
            index = int(input("Enter index: "))
            list.update_node(index,newData)

        elif choice == "0":
            print("Have a good one...")
            break

        else:
            print("Invalid choice, try again.")

menu()