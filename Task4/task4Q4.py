#Q4) 


import Calculator


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("Choose operation: +  -  *  /")
operation = input("Enter operator: ")


if operation == "+":
    result = Calculator.add(num1, num2)
elif operation == "-":
    result = Calculator.subtract(num1, num2)
elif operation == "*":
    result = Calculator.multiply(num1, num2)
elif operation == "/":
    result = Calculator.divide(num1, num2)
else:
    result = "Invalid operator!"

print("Result:", result)

