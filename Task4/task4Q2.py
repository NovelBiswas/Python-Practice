#Q2) 


my_dict = {"name": "Novel", "age": 25}
my_list = [10, 20, 30]

try:
    print("Name:", my_dict["name"])
    print("City:", my_dict["city"]) 

    print("Item at index 5:", my_list[5]) 

    result = 10 / 0
    print("Result:", result)

except KeyError:
    print("KeyError: doesn't exist in the dictionary.")

except IndexError:
    print("IndexError: doesn't exist in the list.")

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

finally:
    print("finished.")
