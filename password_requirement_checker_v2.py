# Using a while loop, this password checker ensures that the first password character is alphabetical
# It will also check that the last character is not any of the following "/", "^", "*", "@"
# We will use a list here to check

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z']
reserved = ['/', '^', '*', '@']

new_password = input('Enter a new password - first character must be alphabetical...')

while True:
	if new_password[0].lower() not in alphabet:  # Specifiying lower will convert first character to lower for list checking
		print('Invalid password.. The first characted is not alphabetical..')
		new_password = input('Try again... First character has to be a letter:  ')
		continue
	elif new_password[-1] in reserved:
		print('Invlaid password.. The last character is in the reserve list..')
		new_password = input('Try again... Last character can\'t be "/", "^", "*" or "@":  ')
		continue
	else:
		break
print('Your password has been set')
