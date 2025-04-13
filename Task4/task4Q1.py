#Q1) 


class appropriate(Exception):
    pass

def check_age(age):
    if age < 18:
        raise appropriate("at least 18 years old.")
    else:
        print("You are allowed!")
try:
    age = int(input("Enter your age: "))
    check_age(age)
except appropriate as e:
    print("Access denied:", e)
except ValueError:
    print("Please enter a valid age.")
