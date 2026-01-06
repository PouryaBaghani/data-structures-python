"""
=============================================
  🚀 Power Project - By BASH 🚀
=============================================
"""
def power(x1, x2):
    if x2 == 0:
        return 1
    elif x2 < 0:
        return 1 / power(x1, -x2)
    else:
        return x1 * power(x1, x2 - 1)

        
n=int(input("number= "))
p=int(input("power= "))

print(power(n,p))  