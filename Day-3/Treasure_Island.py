print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

# Prints a message to the screen
print("Welcome to the Treasure Island.")
print("Your mission is to find the Treasure.")

# Ask user for their first choice
first_choice = input('You are at the cross road, where do you want to go? Type "left" or "right".\n').lower()

if first_choice == 'left':
	second_choice = input('You arrived at a lake. There is an island in the middle. Do you want to "swim" or "wait". \n').lower()
	if second_choice == 'swim':
		third_choice = input('You finally arrived at the Island. There is a house with three doors. "Red", "Green" and "Blue". Choose one door. \n').lower()
		if third_choice == 'red':
			print("Game over, you just fell into a dark hole...")
		elif third_choice == 'green':
			print("Congratulation..You Win. You found the treasure worth $50 million")
		else:
			print("Game over!!!...You entered the room with fire...")
	else:
		print("Game over!!!...You were attacked by wide dogs")
else:
	print("Game over!!!...You got attacked by a beast!!!")

