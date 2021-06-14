# This is a short program to round any float (decimal number) to one decimal place.


decimal = float(input('Give me a number with decimal digits. '))
rounded_decimal = round(decimal*10)/10
print(f'To one decimal place, your number is {rounded_decimal}')