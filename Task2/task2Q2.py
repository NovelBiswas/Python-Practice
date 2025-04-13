#Q2) Create a program to reverse the digits of a number using a while loop. 

def rev_num(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

num = int(input("Enter a number: "))
print(f"Reversed number: {rev_num(num)}")
