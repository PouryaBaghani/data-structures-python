"""
=============================================
  🚀 Sparse with Array Project - By BASH 🚀
=============================================
"""
def to_sparse(matrix):
    sparse=[]
    i=0
    for row in matrix:
        j=0
        for value in row:
            if value!= 0:
                sparse.append((i,j,value))
            j+=1
        i+=1
        
    return sparse

class MyArray():
    def __init__(self):
        self.data=[]
    
    def insert(self, obj, index):
        new_data=[]
        i=0
        
        for item in self.data:
            if i==index:
                new_data.append(obj)
            new_data.append(item)
            i+=1
        if index==i:
            new_data.append(obj)
                
        self.data=new_data
        
    def delete(self, index):
        new_data=[]
        i=0
        removed = None
        for item in self.data:
            if i==index:
                removed = item
            else:
                new_data.append(item)
            i+=1
            
        self.data = new_data
        return removed
    
    def find(self, obj):
        i = 0
        for item in self.data:
            if item == obj:
                return i
            i += 1
        return -1
    
    
n=int(input("n*n matrix ---> n="))
matrix=[]

for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input("entry=")))
    matrix.append(row)
    
Sparse = to_sparse(matrix)
for item in Sparse:
    print("Sparse element(row,column,value):", item)  

arr = MyArray()
for item in Sparse:
    arr.insert(item, 0)
     
print("Array after inserts:", arr.data) 

print("Deleted element:", arr.delete(1))  

print("Array after deletion:", arr.data)