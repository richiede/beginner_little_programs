# Another simple password gerenerator
# This program will ask the user to enter a 3 letter word
# The password gerenerated will be the 3rd letter, followed by the '&' symbol,
# followed by the 2nd letter, then the '%' symbol, finishing with the 1st letter.

# So if "cat" is entered, the password will ve t&a%t

import sys

while True:
	print('Enter a 3 letter word to create a password: ')
	word = input()
	if len(word) != 3:
		print('That isn\'t 3 letters... Try again!')
		continue
	else:
		break

password = word[2] + '&' + word[1] + '%' + word[0]

print(f'Your password is {password}')
