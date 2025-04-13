#Q1)Write a Python program to find the frequency of each character in a given string using a dictionary. 

def char_frequency(string):
    frequency_dict = {}
    
    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict


input_string = input("Enter a string: ")
result = char_frequency(input_string)
print("Character frequencies:")
for char, freq in result.items():
    print(f"'{char}': {freq}")
