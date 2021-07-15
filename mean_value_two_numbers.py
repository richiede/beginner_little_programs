# 2 random numbers are generated and the mean of both calculated
# The user has 3 guesses to get the mean value
import random
import sys

number_1 = random.randint(0, 100)
number_2 = random.randint(0, 100)

mean = (number_1 + number_2) / 2

print(f'What is the mean of {number_1} and {number_2}.')

mean_attempt = int(input())
attempt_count = 1

while mean_attempt != mean:
	if attempt_count < 4:
		print('Wrong. Please try again...')
		attempt_count += 1
		print(f'What is the mean of {number_1} and {number_2}.')
		mean_attempt = int(input())
	else:
		print('Sorry you ran out of guesses...')
		sys.exit()

print('Correct!')
