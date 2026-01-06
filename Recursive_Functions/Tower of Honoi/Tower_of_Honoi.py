"""
=============================================
  🚀 Tower of Honoi Project - By BASH 🚀
=============================================
"""
def TOH(n, A, B, C):
    if n == 0:
        return

    TOH(n-1, A, C, B)
    print(f"move disk from {A} to {C}")
    TOH(n-1, B, A, C)

# TEST
number = int(input("number= "))
TOH(number, 1, 2, 3)