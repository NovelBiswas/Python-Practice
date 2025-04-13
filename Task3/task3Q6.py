#Q6) Write a Python program that checks if a string contains only alphanumeric characters and then returns the length of the string. 

def alpha_length(string):
    if string.isalnum():
        return len(string)
    else:
        return "The string contains non alphanumeric characters."

input_string = input("Enter a string: ")
result = alpha_length(input_string)
print("Result:", result)
