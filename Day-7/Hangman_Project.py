

# HANGMAN GAME

print('''
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       
''')

# ASCII for Hangman
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========


''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========

''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========

''', '''
  +---+
  |   |
      |
      |
      |
      |
========='''

		  ]



import random

# create a lis of words
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()


# randomly chose word
chosen_word = random.choice(word_list)

# Number of player live's.
lives = 6

# Number of stages
print(stages[-1])

#create an empty list
display = []

# add symbol into the list
for letter in chosen_word:
    display.append("_")

# make a print
print(display)

# use a while loop to make conditions on lives
while lives > 0:  # Check for number of lives
    guess = input("Choose a letter: ").lower()
    if guess not in chosen_word:  # reduce lives in guess not on chosen_word
        lives -= 1
        print(stages[lives])
    if lives == 0:
        print("You have no more lives try again")

    # If index of letter in word matches the index of display replace display index with letter
    for index, elem in enumerate(chosen_word):
        if elem == guess:
            display[index] = guess
    print(display)

    # When "_" is no longer present in display than you win.
    if "_" not in display:
        lives = 0
        print(" Yay you win!")
        break
# make the final print
print("The answer was: ",chosen_word)
