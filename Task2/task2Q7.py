#Q7) Write a Python program to remove duplicate characters from a string. Use control 
#flow to check if a character has already been added to the result.

def remove_duplicates(s):
    result = ""
    seen = set()
    
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    
    return result
string = input("Enter a string: ")
unique_string = remove_duplicates(string)
print(f"String after removing duplicates: {unique_string}")