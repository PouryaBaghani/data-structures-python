def combinatorics(n , k): # C(n, k) = n! / k! * (n - k)!
    if k < 0 or k > n or n < 0:
       return "invalid input"
    
    if k == 0 or k == n:
        return 1
    
    if k == 1:
        return n
    
    return combinatorics(n - 1 , k - 1) + combinatorics(n  - 1 , k)

print("C(n, k)")
print(combinatorics(int(input("enter n\n")), int(input("enter k\n"))))