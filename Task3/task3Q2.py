#Q2) Write a Python program to rotate the elements of a list by a specified number of positions to the right.

def rotate_list(list, positions):
    if not list:
        return list  # Return empty list if input is empty
    
    positions = positions % len(list) 
    return list[-positions:] + list[:-positions]


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_positions = int(input("Enter number of positions to rotate: "))
rotated_list = rotate_list(input_list, num_positions)
print("Rotated list:", rotated_list)