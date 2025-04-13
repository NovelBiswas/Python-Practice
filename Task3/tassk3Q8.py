#Q8) Write a Python program to find the index of the first occurrence of an element in a tuple.

def find_index(tuple, element):
    for i, val in enumerate(tuple):
        if val == element:
            return i
    return -1  

tuple_data = (10, 20, 30, 40, 20, 50, 20, 60)
element_to_find = 20

index = find_index(tuple_data, element_to_find)
print("First occurrence index:", index)