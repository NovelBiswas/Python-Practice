#Q14)  Write a Python program to find the longest palindromic substring in a given string. 

def longest_palindromic_substring(string):
    longest = string[0] if string else "" 
    
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substr = string[i:j]
            if substr == substr[::-1] and len(substr) > len(longest):
                longest = substr
    
    return longest


input_string = input("Enter a string: ")
result = longest_palindromic_substring(input_string)
print("Longest palindromic substring:", result)
