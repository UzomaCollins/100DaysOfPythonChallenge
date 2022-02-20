# Welcome to the Tip Calculator

# Prints out a message and ask for the user input
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

# Ask user for how many people to split the bill between
people = int(input("How many people are to split the bill?"))

# Ask for the tip
tip = int(input("What is the split tip? (10, 12 or 15)?"))

# tip calculator
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
print("Thank you!")