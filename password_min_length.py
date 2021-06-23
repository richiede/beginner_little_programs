# This program sets a variable called user_password.
# If the password is less that 5 characters, the program loops round to re-enter the password

user_password = input('Set a password - minimum 5 characters please: ')

while True:
	if len(user_password) < 5:
		print('Password less that 5 characters... Try again: ')
		user_password = input('Set a password - minimum 5 characters please: ')
	else:
		print('Password has been set!')
		break
