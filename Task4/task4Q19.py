#Q19)

import math

def area(shape="rectangle", length=1, width=1, radius=1):
    if shape == "rectangle":
        return length * width
    elif shape == "square":
        return length * length
    elif shape == "circle":
        return math.pi * radius * radius
    else:
        return "Invalid shape"

# Rectangle: length = 5, width = 4
print("Area of rectangle:", area("rectangle", length=10, width=5))

# Square: length = 7
print("Area of square:", area("square", length=6))

# Circle: radius = 5
print("Area of circle:", area("circle", radius=7))

# Using defaults
print("Default rectangle area:", area())
