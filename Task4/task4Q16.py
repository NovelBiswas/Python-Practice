#Q16)

import math

def find_gcd(a, b):
    return math.gcd(a, b)

num1 = int(input("first number: "))
num2 = int(input("second number: "))

result = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is:", result)
