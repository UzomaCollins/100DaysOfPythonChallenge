


# CAESAR CIPHER

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',

			 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

			 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',

			 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# create a function to accept the user input
def caesar(start_text, shift_amount, cipher_direction):
	end_text = ""
	if cipher_direction == "decode":
		shift_amount *= -1
	for char in start_text:
		if char in alphabets:
			position = alphabets.index(char)
			new_position = position + shift_amount
			end_text += alphabets[new_position]
		else:
			end_text += char
	print(f"Here's the {cipher_direction}d result {end_text}")
	print()

should_continue = True
while should_continue:

	# Ask the user of their choice
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

	# user input
	text = input("Type your message:\n").lower()

	# shift number
	shift = int(input("Type the shift number:\n"))
	shift = shift % 26

	# calling the caesar function
	caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

	result = input("Type 'yes' if you wish to go again. Otherwise type 'no'.\n" )
	if result == "no":
		should_continue = False
		print("Thanks, Goodbye")




# Encrypt
# def encrypt(plain_text, shift_amount):
# 	cipher_text = ""
# 	for letter in plain_text:
# 		position = alphabets.index(letter)
# 		new_position = position + shift_amount
# 		new_letter = alphabets[new_position]
# 		cipher_text += new_letter
# 	print(f"The encoded text is {cipher_text}")
#
#
# # Decrypt
# def decrypt(cipher_text, shift_amount):
# 	plain_text = ""
# 	for letter in cipher_text:
# 		position = alphabets.index(letter)
# 		new_position = position - shift_amount
# 		plain_text += alphabets[new_position]
# 	print(f"The decoded text is {plain_text}")
#
#
# # direction variable
# if direction == "encode":
# 	encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
# 	decrypt(cipher_text=text, shift_amount=shift)