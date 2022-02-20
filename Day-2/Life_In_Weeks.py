'''Create a program using maths and f-String
   that tells us how many days, weeks and months
   that we have left, if we are to live until 90 years'''

# Ask the user of their age
user_age = input("What is your current age?\n")
age_as_int = int(user_age)

# user years, months, weeks and days remaining
years_remaining = (90 - age_as_int)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

# store the message in a variable
message = (f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left.")

# Print the message value
print(message)

# Print a warning message for all
print("Be very careful and live according to Gods plans for you!!!, Wish you the best.")