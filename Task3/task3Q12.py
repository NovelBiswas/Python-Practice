#Q12) Given a list of integers, write a Python program to find all unique combinations of 
#elements that sum up to a target value.

from itertools import combinations

def find_combinations(nums, target):
    result = set()
    
    for r in range(1, len(nums) + 1):
        for combo in combinations(nums, r):
            if sum(combo) == target:
                result.add(tuple(sorted(combo)))
    
    return list(result)

nums = [3, 6, 8, 9]
target = 9
unique_combos = find_combinations(nums, target)
print("Unique combinations that sum to target:", unique_combos)
