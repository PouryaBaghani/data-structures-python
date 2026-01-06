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

def optimized_power(base, exponent): # O(log exeponent)
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        result = optimized_power(base, exponent // 2)
        return result * result
    result = optimized_power(base, (exponent - 1) // 2) 
    return base * result * result
        
n=int(input("number= "))
p=int(input("power= "))

print(power(n,p))  