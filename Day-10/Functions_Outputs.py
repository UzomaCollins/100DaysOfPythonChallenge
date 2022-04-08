# Functions with outputs

# def add(a, b):
# 	result = a + b
# 	return result
#
#
# print(add(5, 5))
#
#
# def format_name(f_name, l_name):
# 	first_name = f_name.title()
# 	last_name = l_name.title()
# 	result = first_name + " " + last_name
# 	return result
#
#
# print(format_name("UZOMA", "COLLINS"))


# lEAP yEAR

def leap_year(year):
	"""Take a date and check if it's a
	new year and print it out."""

	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return ("Leap Year")
			else:
				return ("Not leap year")
		else:
			return ("Leap Year.")
	else:
		return ("Not leap year.")

print(leap_year(1600))

# Docstring