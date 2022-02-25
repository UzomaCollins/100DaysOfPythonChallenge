# This program Calculates love percentage using individual names

# Print a welcome message to the screen
print("Welcome to the Love Calculator")

# Ask for name of the first user
name1 = input("What is your name?\n")

# Ask for name of the second user
name2 = input("What is their name?\n")

# Combine the two strings
combined_string = name1 + name2

# Convert string to lower case strings
lower_case_string = combined_string.lower()

# Check for letter occurrence in true and love
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

# sum the total number of occurred letters
true = t + r + u + e

# check for love
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

# sum the total number of occurred letters
love = l + o + v + e

# Convert the string values to an integer
love_score = int(str(true) + str(love))


# use an if statement to make comparison
if (love_score < 10) or (love_score > 90):
	print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
	print(f"Your score is {love_score}, you are alright together")
else:
	print(f"Your score is {love_score }")
