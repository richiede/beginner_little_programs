# This is a script that converts pounds to kilos, rounding to the nearest 1 decimal place

coversion_factor = 0.45

print('I will convert a weight from lbs to kilos.')
pounds = float(input('What is the weight in lbs?'))
kilos = pounds * coversion_factor
kilos_rounded = round(kilos*10)/10

print(f'The weight in kilos is {kilos_rounded}')
