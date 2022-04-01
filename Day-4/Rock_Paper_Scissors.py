# This is the Rock, Paper and Scissors Game

'''it has three possible outcomes: a draw, a win or a loss.
A player who decides to play rock will beat another player
who has chosen scissors ("rock crushes scissors" or "breaks
scissors" or sometimes "blunts scissors"[4]), but will lose
to one who has played paper ("paper covers rock"); a play
of paper will lose to a play of scissors ("scissors cuts paper")'''



# import your module
import random



# ASCII ART for Rock, Paper and Scissors

Rock = '''

   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''



Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''


Scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

# Creates a list
game_images = [Rock, Paper, Scissors]

# Ask for user choice
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Checks for the lenght of list
if user_choice >= 3 or user_choice < 0:
	print("You typed an invalid number, you lose!")
else:
	print(game_images[user_choice])


# Rock == 0
# Paper == 1
# Scissors == 2


# Computer choice
computer_choice = random.randint(0, 2)
print("Computer choose:")
print(game_images[computer_choice])


# Conditions

if user_choice == 0 and computer_choice == 2:
	print("You win!")

elif computer_choice == 0 and user_choice == 2:
	print("You lose!")

elif user_choice == 0 and computer_choice == 1:
	print("You win!")

elif computer_choice == 0 and user_choice == 1:
	print("You lose!")

elif user_choice == 1 and computer_choice == 2:
	print("You win!")

elif computer_choice == 1 and user_choice == 2:
	print("You lose!")

elif computer_choice == user_choice:
	print("It's a draw!")



