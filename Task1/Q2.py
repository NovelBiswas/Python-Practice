#Q2) How can you check if a number is either less than 10 or greater than 50? 

def check(number):
  if number < 10:
    print("The number is less than 10")
  else:
    print("The number is not less than 10")

  if number > 50:
    print("The number is greater than 50")
  else:
    print("The number is not greater than 50")

number = int(input("Enter a number: "))
result = check(number)
print(result)