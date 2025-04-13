#Q6) Program: find largest number out of given three numbers ie., a, b & c. 
#(you can assign value to a, b and c as per your choice) 

A = int(input("Enter A: "))
B = int(input("Enter B: ")) 
C = int(input("Enter C: "))

if A >= B and A >= C:
    largest = A
elif B >= A and B >= C:
    largest = B
else:
    largest = C

print("The largest number is:", largest)