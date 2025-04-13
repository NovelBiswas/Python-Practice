#Q23)

import math

def safe_square_root():
    try:
        user_input = input("Enter a number to find its square root: ")
        number = float(user_input) 
        if number < 0:
            print("Cannot calculate square root of a negative number.")
        else:
            result = math.sqrt(number)
            print(f"The square root of {number} is {result}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
safe_square_root()
