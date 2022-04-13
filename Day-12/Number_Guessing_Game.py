
# GUESS THE NUMBER GAME
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
	if guess > answer:
		print("Too high")
		return turns - 1
	elif guess < answer:
		print("Too low")
		return turns - 1
	else:
		print(f"You got it! The answer was {answer}.")


def set_difficulty():
	level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
	if level == 'easy':
		global turns
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS


def game():
	print("WELCOME TO THE NUMBER GUESSING GAME!")
	print()
	print("I'm thinking of a number between 1 and 100.")
	answer = random.randint(1, 100)

	guess = 0

	turns = set_difficulty()

	while guess != answer:
		print(f"You have {turns} attempts remaining to guess the number.")
		guess = int(input(("Make a Guess: ")))
		turns = check_answer(guess, answer, turns)
		if turns == 0:
			print("You have run out of guess. You lose")
			return
		elif guess != answer:
			print("Guess again")


game()
