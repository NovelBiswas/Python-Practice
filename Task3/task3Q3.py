#Q3) Create a program that takes a list of tuples and returns a list of the second elements from each tuple. 

def extract_second_elements(tuples_list):
    return [tup[1] for tup in tuples_list if len(tup) > 1]


input_list = [(1, 'n'), (2, 'o'), (3, 'v'), (4, 'e'), (5, 'l')]
result = extract_second_elements(input_list)
print("Second elements:", result)