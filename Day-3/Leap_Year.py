# This program tells you a year that is a leap year
print("This program tells you a year that is a leap year.")

# Ask user to input the year
year = int(input("Enter the year."))

# Check if conditions are met
if year % 4 == 0:

	if year % 100 == 0:

		if year % 400 == 0:

			print("LEAP YEAR")

		else:

			print("Not a LEAP YEAR")

	else:

		print("LEAP YEAR")

else:

	print("Not LEAP YEAR")
