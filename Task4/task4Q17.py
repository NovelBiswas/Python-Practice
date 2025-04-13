#Q17)

count = 1

def update_count():
    global count 
    count = count + 1

print("Before updating, count =", count)

update_count()

print("After updating, count =", count)
