#Q13) Create a Python function that takes a string and returns all possible substrings of that 
#string without using any built-in functions. 

def generate_substrings(string):
    substrings = []
    
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    
    return substrings


input_string = "novel"
result = generate_substrings(input_string)
print("All possible substrings:", result)