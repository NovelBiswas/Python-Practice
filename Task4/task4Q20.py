#Q20)

def frequency(items):
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

list = [1, 2, 2, 3, 1, 4, 2, 3, 1, 1]

frequencies = frequency(list)

print("Frequencies of elements:")
for element, count in frequencies.items():
    print(f"{element}: {count}")
