#Q3) How can you find the factorial of a number using a while loop? 

def fact(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

num = int(input("Enter a number: "))
print(f"Factorial of {num}: {fact(num)}")
