import sys

days_of_week = list(range(8))

gym_days = int(input('How many days do you intend on visiting the gym?'))

if gym_days not in days_of_week:
	print('Invalid input.')
	sys.exit()

if gym_days == 0:
	print('You are not eligable for a gym membership.')
elif gym_days > 4:
	print('You are eligable for a Gold membership.')
else:
	print('You are eligable for a standard membership')
