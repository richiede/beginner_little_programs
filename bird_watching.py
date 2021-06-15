# This is a program that asks the user what bird they saw. It will then add that bird to a list with a time stamp
# The user presses "y" to keep playing
# Any other key pressed and the program ends with a for loop running over the list to display them in order spotted

import sys
from datetime import datetime

birds = []

while True:
	print('Have you spotted a bird? Press (y) for yes or any other key to quit: ')
	spotted = input()
	if spotted != 'y':
		break
	print('What bird did you spot? ')
	bird_spotted = input()
	now = datetime.now()
	birds.append(bird_spotted + ' ' + now.strftime("%H:%M"))

for i in range(len(birds)):
	print(f'Number {str(i+1)} bird spotted was {birds[i]}')

