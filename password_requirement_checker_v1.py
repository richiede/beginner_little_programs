# This password checker ensures that the first password character is alphabetical
# We will use a list here to check

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z']

new_password = input('Enter a new password - first character must be alphabetical...')

if new_password[0].lower() not in alphabet:  # Specifiying lower will convert first character to lower for list checking
	print('Invalid password..')
else:
	print('Your password has been accepted.')
