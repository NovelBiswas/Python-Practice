#Q8) Write a program to find the first non-repeating character in a string. Use control flow 
#to iterate through the string and check character frequency. 

def first_non_repeating_character(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

string = input("Enter a string: ")
non_repeating_char = first_non_repeating_character(string)
if non_repeating_char:
    print(f"First non-repeating character: {non_repeating_char}")
else:
    print("No non-repeating character found.")