#Q5) Write a program to check if two variables point to the same object in memory. 


x = [1, 2, 3]
y = x
if x is y:
    print("x and y point to the same object in memory.")
else:
    print("x and y do not point to the same object in memory.")
z = [1, 2, 3]
if x is z:
    print("x and z point to the same object in memory.")
else:
    print("x and z do not point to the same object in memory.")

# check if two variables point to the same object in memory as id.

print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")
print(f"id(z): {id(z)}")
