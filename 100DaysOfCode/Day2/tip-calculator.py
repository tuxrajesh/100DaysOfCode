print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
no_of_people = input("How many people to split the bill? ")
tip_percent = input("What percentage tip would you like to give? 10, 12 or 15? ")
per_person_cost = (total_bill + (total_bill * tip_percent / 100.0))/no_of_people
print("Each person should pay: $" + per_person_cost)