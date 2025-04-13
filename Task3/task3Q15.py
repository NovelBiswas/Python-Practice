#Q15)  Write a Python program to find all permutations of a given string without using any built
#in permutation functions.

def string_permutations(string, step=0):
    if step == len(string):
        print("".join(string))
    
    for i in range(step, len(string)):
        string_list = [c for c in string]
        string_list[step], string_list[i] = string_list[i], string_list[step]
        string_permutations(string_list, step + 1)

input_string = input("Enter a string: ")
string_permutations(list(input_string))
