# this is a small program to determin tenis competition price and add to relevant list

juniors = []
intermiediate = []
senior = []

junior_price = 2.50
intermiediate_price = 3.50
senior_price = 5.00

print('Welcome to the Tennis tournament registration!')

while True:
	want_to_play = input('Do you want to enter a name? Hit "y" for yes or any other key to quit...')
	if want_to_play != 'y':
		break
	else:
		competitor_name = input('What is your name?')
		competitor_age = int(input('How old are you?'))
		if competitor_age < 1 or competitor_age > 100:
			print('Input error')
			print('Try again')
		elif competitor_age < 12:
			print(f'Thanks {competitor_name}, you will be added to the junior competition and will be charged £{junior_price}.')
			juniors.append(competitor_name)
		elif competitor_age < 18:
			print(f'Thanks {competitor_name}, you will be added to the intermiediate competition and will be charged £{intermiediate_price}.')
			intermiediate.append(competitor_name)
		else:
			print(f'Thanks {competitor_name}, you will be added to the seniors competition and will be charged £{senior_price}.')
			senior.append(competitor_name)

print(f'In the Juniors tournament we have {juniors}...')
print(f'In the intermiediate tournament we have {intermiediate}...')
print(f'In the senior tournament we have {senior}...')
