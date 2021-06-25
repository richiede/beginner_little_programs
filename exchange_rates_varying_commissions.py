# This program will convert Euros to Sterling and charge an applicable commission based on amount
# Low commission = £3 and applicable for anything under €500 not including €500
# Medium commisison = £4 for €500 - €1000 (including €1000)
# High commission = £5 for €1001 and above

exchange_rate = 1.16270
low_commission = 3
medium_commission = 4
high_commission = 5

print('I will exchange Euros for pounds.')
euros = int(input('How many Euros are wanted?'))

if euros < 500:
	commission = low_commission
elif euros < 1001:
	commission = medium_commission
else:
	commission = high_commission

cost = euros / exchange_rate + commission
rounded_cost = round(cost * 100/100)

print(f'The exchange rate is {exchange_rate}. The commission changed is £{commission}')
print(f'The total cost is {rounded_cost}')
