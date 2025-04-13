#Q1) Write a program that checks if a number is both positive and even.

def positive_even(number):
    if number > 0:
        print("The number is positive.")
    else:
        print("The number is not positive.")

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is not even.")

number = int(input("Enter a number: "))
result = positive_even(number)
print(result)