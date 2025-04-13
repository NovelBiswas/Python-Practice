#Q6) Write a program to count the number of vowels and consonants in a given string. 
#Usecontrol flow statements to classify each character. 

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return vowel_count, consonant_count

string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(string)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")