# Singly Linked List Implementation in Python

A **singly linked list** implementation in Python with common operations such as insert, remove, update, find, invert, and concatenate.  
This project demonstrates both the **classic traversal logic** for computing size and the **optimized constant-time size tracking** using a `self.size` attribute.

---

##  Features

- 🔹 Insert at **beginning**, **end**, or at a specific **index**
- 🔹 Remove from **beginning**, **end**, or at a specific **index**
- 🔹 Update node data by index
- 🔹 Find a node by value
- 🔹 Invert (reverse) the linked list
- 🔹 Concatenate two linked lists
- 🔹 Display the list contents
- 🔹 Track size efficiently with `self.size`

---

##  Size Tracking

This implementation shows two approaches to determine the size of the linked list:

1.  **Efficient tracking (`self.size`)**
   - The `size` attribute is updated whenever nodes are inserted or removed.
   - Provides **O(1)** constant-time size checks.
   - Used internally for all index validations.

2.  **Traversal method (`size_of_list()`)**
   - Demonstrates the traditional way of counting nodes by walking through the list.
   - Provides **O(n)** linear-time size checks.
   - Included for **educational purposes** to show the underlying logic of linked list traversal.

---

##  Complexity

- **Insert at begin**: O(1)  
- **Insert at end**: O(n)  
- **Insert at index**: O(n)  
- **Remove at begin**: O(1)  
- **Remove at end**: O(n)  
- **Remove at index**: O(n)  
- **Update node**: O(n)  
- **Find node**: O(n)  
- **Invert list**: O(n)  
- **Concatenate lists**: O(n)  
- **Size (attribute)**: O(1)  
- **Size (traversal)**: O(n)  

---

##  Notes

- `self.size` is the efficient way to track list length.  
- `size_of_list()` is kept to demonstrate the traversal logic for learning purposes.  
- This project is intended for **academic practice** and **data structure learning**.

---

##  Acknowledgments

Special thanks to my dear friend [TAYMAZ328](https://github.com/TAYMAZ328), who helped me with the `self.size` idea and supported the whole project.  
Gratitude also goes to my partner Shalilian, who contributed and supported the project throughout.