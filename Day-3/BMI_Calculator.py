# This BMI tells if someone is underweight, over-weight or has a normal weight

# This prints a value to the user
print("This calculates your BMI based on your input values")

# Ask for the users weight
user_weight = float(input("What is your weight in kg?"))

# Ask for users height
users_height = float(input("What is your height?"))

# Calculate BMI = weight / height ** 2
user_BMI = round(user_weight / users_height ** 2)

# Conditions for BMI
if user_BMI < 18.5:
	print(f"your BMI is: {user_BMI}, you are underweight.")
elif user_BMI >= 18.5 and user_BMI <= 25:
	print(f"Your BMI is: {user_BMI}, you have a normal weight.")
elif user_BMI > 25 and user_BMI <= 30:
	print(f"Your BMI is:{user_BMI}, you are overweight.")
elif user_BMI > 30 and user_BMI <= 35:
	print(f"Your BMI is {user_BMI}, you are obese.")
else:
	print(f"Your BMI is:{user_BMI}, you are clinically obese.")
