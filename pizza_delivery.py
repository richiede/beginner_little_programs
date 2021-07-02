# This program determins if a £1.50 per mile delivery charge over 3 miles is applicable.
# Over 12 miles is non deliverable

import sys

cost_per_mile = 1.50

print('Welcome! The first 3 miles delivery are included in the price. After then there is a £1.50 charge per mile')

try:
	customer_distance = float(input('How far away do you live?'))
except ValueError:
	print('Sorry you entered an invalid entry.')
	sys.exit()

if customer_distance < 0:
	print('You entered a negative number....')
	sys.exit()

if customer_distance > 12:
	print('Sorry we don\'t deliver to over 12 miles.')
elif round(customer_distance) > 3:
	print(f'The charge for your delivery is {(round(customer_distance)-3)*cost_per_mile}')
else:
	print('Delivery is free! You are within 3 miles of the pizza place')
