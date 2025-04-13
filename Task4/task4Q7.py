#Q7)

import random

def die():
    return random.randint(1, 6)

input("Press Enter to roll the die.")
result = die()
print("You rolled a:", result)
