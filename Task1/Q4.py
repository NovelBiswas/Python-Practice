#Q4) Create a program to demonstrate bitwise XOR and NOT
a = int(input("Enter a: "))
b = int(input("Enter b: ")) 

# Bitwise XOR
xor_result = a ^ b
print(f"{a} ^ {b} = {xor_result} (Binary: {bin(xor_result)})")

# Bitwise NOT
not_a = ~a
print(f"~{a} = {not_a} (Binary: {bin(not_a)})")

