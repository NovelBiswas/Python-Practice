#Q4) Write a program to merge two dictionaries and add the values of common keys

def merge_dict(dict1, dict2):
    merged_dict = dict1.copy()
    
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    
    return merged_dict

dict1 = {'n': 10, 'o': 20, 'v': 30}
dict2 = {'o': 5, 'e': 15, 'l': 25}

merged_result = merge_dict(dict1, dict2)
print("Merged Dictionary:", merged_result)
