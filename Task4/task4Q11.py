#Q11)

def vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
vowel = vowels(user_input)
print("Number of vowels:", vowel)
