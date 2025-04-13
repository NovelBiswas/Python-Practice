#Q5) Check if the string "radar" is a palindrome using slicing.

def palindrome(w):
    return w ==w[::-1]

word = "Novel"
if palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')
