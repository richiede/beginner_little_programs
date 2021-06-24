# This program sets a variable called user_password.
# If the password is less than 5 characters or more than 12, the program loops round to re-enter the password

user_password = input('Set a password - minimum 5 characters please: ')

while True:
	if len(user_password) < 5 or len(user_password) > 12:
		print('Password length invalid ... Try again: ')
		user_password = input('Set a password - min 5 max 12: ')
	else:
		print('Password has been set!')
		break
