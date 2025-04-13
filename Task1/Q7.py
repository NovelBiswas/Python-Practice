#Q7) Program: calculate simple interest.  (Formula: principle * (rate/100) * time )

principal = int(input("Enter principle amount: "))    # Principal amount
rate = int(input("Enter rate: "))                     # Interest rate (in percentage)
time= int(input("Enter time: "))                      # Time in years

#Simple Interest
simple_interest = principal * (rate / 100) * time

print(f"Simple Interest: {simple_interest}")
