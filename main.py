print("Welcome to the tip calculator!")
total_bill = float(input("What is the total bill: "))
tip = int(input("How much percentage tip would you like to give: "))
people = int(input("How many people to split the bill: "))
total_bill += total_bill*(tip/100)
each_person_pay = round((total_bill / people),2)
print(f"Each person should pay {each_person_pay}$")

