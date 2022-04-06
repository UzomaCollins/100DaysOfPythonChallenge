
# Simple function
# def greet():
# 	print("Good morning")
# 	print("How are you doing?")
# 	print("See you later. Bye...")

# #greet()

# # Function with inputs
# def greet_with_name(name):
# 	print(f"Good morning {name}")
# 	print(f"How are you doing {name}?")
# 	print(f"See you later {name}")

# greet_with_name("Collins")

#more then 1 input
# def greet(name = "collins", location = "london"):
# 	print(f"Good morning {name}")
# 	print(f"How's it in {location}?")
#
# greet()


# import math
#
# # Paint for a wall
# def pait_calc(height, width, cover):
# 	area = height * width
# 	num_of_cans = math.ceil(area / cover)
# 	print(f"You will need {num_of_cans} cans of paint.")
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# pait_calc(height=test_h, width=test_w, cover = coverage)


#PRIME NUMBER CHECKER
# def prime_checker(number):
# 	is_prime = True
# 	for i in range(2, number):
# 		if number % i == 0:
# 			is_prime = False
# 	if is_prime:
# 		print("It's a prime number")
# 	else:
# 		print("It's not a prime number")
#
# prime_checker(7)