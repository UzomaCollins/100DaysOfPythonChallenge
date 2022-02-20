
# This program calculates the weight of a person

# Ask the user of their weight(kg)
user_weight = int(input("What is your weight in kg?\n"))

# Ask the user for their height in squared-meters
user_height = float(input("What is your height in sqaured-meters\n"))

# Calculate the users BMI
bmi = user_weight / user_height

# Round the value of the BMI
user_bmi = round(bmi)

# Print out the BMI
print(f"Your BMI is {user_bmi}")
