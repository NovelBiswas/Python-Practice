#Q4) Write a program that prints a right-angled triangle pattern using stars (*).

def triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

# Example usage
num_rows = int(input("Enter the number of rows: "))
triangle(num_rows)
