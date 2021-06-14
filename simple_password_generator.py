# This is a simple password generator that takes the user's favourite colour, 
# they first pet's name and combines then with a random number between 10 - 99
# and then adds an '!' at the end.

import random

print('I will create a password for you.')
colour = input('What is your favourite colour? ')
pet_name = input('What was the name of your first pet? ')
digit = random.randint(10, 99)
password = (colour + pet_name + str(digit) + '!')
print(f'Your password is {password}')
