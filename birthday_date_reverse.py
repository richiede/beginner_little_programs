# This is a simple program that takes a birthday in the DD/MM UK format and reverses to US MM/DD format.
# There is little error checks here - just a simple program.

uk_dob = input('What is your birthday in DD/MM format? ')

us_dob = uk_dob[3:] + '/' + uk_dob[0:2]

print(f'Your US birthday is {us_dob}')
