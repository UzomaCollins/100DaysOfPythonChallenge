
# 1. Describe the problem
# # change the range from 20 to 21 to solve the problem.
# # def my_function():
# # 	for i in range(1,21):
# # 		if i == 20:
# # 			print("You got it")
# #
# # my_function()
# 
# 
# # 2. Reproduce the Bug
# # continually run the program to find the bug.
# # Change the range from 1-6 to 0-5
# # from random import randint
# # dice_ings = ["1", "2", "3", "4", "5", "6"]
# # dice_num = randint(0, 5)
# # print(dice_ings[dice_num])
# 
# # 3. Play Computer
# # change th ">" to ">=" in the elif block
# # year = int(input("What's your year of birth?: "))
# # if year > 1980 and year < 1994:
# # 	print("You are a millenial.")
# # elif year >= 1994:
# # 	print("You are a Gen Z.")
# 
# # 4. Fix the Error
# # Add an "int" to the input and also add af f_string in th print statement
# # age = int(input("How old are you?: "))
# # if age > 18:
# # 	print(f"You can drive at {age}.")
# 
# # 5. Print is your friend
# # Add more print statements to fix the problem and change the "==" to "="
# # in the "word_per_page" line
# # pages = 0
# # word_per_page = 0
# # pages = int(input("Number of pages: "))
# # word_per_page = int(input("Number of words per page: "))
# # total_words = pages * word_per_page
# # print(f"You have a total of {total_words} words in you book.")
# 
# # 6. Use a Debugger
# # Example: Python Tutor
# # def mustate(a_list):
# # # 	b_list = []
# # # 	for item in a_list:
# # # 		new_item = item * 2
# # # 		b_list.append(new_item)
# # # 	print(b_list)
# # #
# # # mustate([1,2,3,4,5])
# 
# # DEBUGGING EXERCISE
# 
# # Even or Odd
# # number = int(input("Which number do you want to check?: "))
# #
# # if number % 2 == 0:
# # 	print("This is an even number.")
# # else:
# # 	print("This is an odd number.")
# 
# # Leap Year
# 
# # year = int(input("Which year do you want to check?: "))
# # if year % 4 == 0:
# # 	if year % 100 == 0:
# # 		if year % 400 == 0:
# # 			print("Leap Year.")
# # 		else:
# # 			print("Not leap year.")
# # 	else:
# # 		print("Leap Year")
# # else:
# # 	print("Not leap year.")
# 
# # FizzBuzz
# for number in range(1, 101):
# 	print(f"Currently on number {number}")
# 	if number % 3 == 0 and number % 5 == 0:
# 		print("FizzBuzz.")
# 	elif number % 3 == 0:
# 		print("Fizz.")
# 	elif number % 5 == 0:
# 		print("Buzz.")
# 	else:
# 		print([number])
