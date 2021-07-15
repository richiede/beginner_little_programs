# This works out the average speed of a track runner
# Can't be a negative or 0 time

distance = float(input('What distance did you run in meters? '))

time = float(input('What was your time in seconds? '))

while not time > 0:
	try:
		print('Time has to be positive. Try again please')
		time = float(input('What was your time in seconds? '))
	except ZeroDivisionError:
		print('Can\'t be a 0 value....')

speed = round(distance/time, 2)

print(f'You speed was {speed} m/s!')
