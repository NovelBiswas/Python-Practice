#Q10) Write a program to print a square pattern with 4 rows and columns.

def print_square(size):
    for i in range(size):
        print("* " * size)

# Example usage
size = 4
print_square(size)
