#Q7) Write a Python program to remove the nth occurrence of a given word in a list of words. 

def remove_nth_occurrence(word_list, word, n):
    count = 0
    for i in range(len(word_list)):
        if word_list[i] == word:
            count += 1
            if count == n:
                del word_list[i]
                return word_list  
    return word_list  
words = ["apple", "banana", "apple", "orange", "apple", "grape"]
word_to_remove = "apple"
n = 2

updated_list = remove_nth_occurrence(words, word_to_remove, n)
print("Updated list:", updated_list)
