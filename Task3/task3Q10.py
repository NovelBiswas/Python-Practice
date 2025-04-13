#Q10) Write a Python program that takes two sets and returns the symmetric difference between them. 

def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = symmetric_difference(set1, set2)
print("Symmetric Difference:", result)