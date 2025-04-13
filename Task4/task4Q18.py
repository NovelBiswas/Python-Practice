#Q18)


def student_info(name, age, course="Python", city="Unknown"):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("City:", city)
    print("-" * 30)

# 1.positional arguments
student_info("Novel", 24)

# 2.positional and keyword arguments
student_info("Kushal", 22, course="Java")

# 3. All arguments as keywords
student_info(name="Ashutosh", age=25, course="C++", city="Mumbai")

# 4. Positional and keyword (in order)
student_info("Aditya", 23, city="Delhi")
