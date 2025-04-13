#Q1) Create a program that determines if a given year is a leap year. 

def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
year = int(input("Enter a year: "))
if leapyear(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
