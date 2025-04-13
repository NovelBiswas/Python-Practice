# Q5) Write a Python program to find the intersection of two sets without using the built-in intersection method. 

def set_intersection(set1, set2):
    intersection_result = {item for item in set1 if item in set2}
    return intersection_result

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

result = set_intersection(set_a, set_b)
print("Intersection of sets:", result)
