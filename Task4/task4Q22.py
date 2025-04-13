#Q22)

def find_common(list1, list2):
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common:
                common.append(item1)
    return common

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

result = find_common(list_a, list_b)

print("Common items:", result)
