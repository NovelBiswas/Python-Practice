#Q9) Write a Python program to create a dictionary from a string, where each key is a word 
# and its value is the frequency of the word in the string. 

def word_frequency(string):
    words = string.split()
    frequency_dict = {}
    
    for word in words:
        word = word.strip(".,!?;:").lower()
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict

input_string = input("Enter a string: ")
result = word_frequency(input_string)
print("Word frequencies:", result)