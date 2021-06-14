# This is a simple fortune teller program from my Open University year 1 module
# This program asks the user if they want to play, if y is entered, a random fortune is selected from a list and displayed on screen.

import random

fortunes = ['stun the world with your OUBuild programs',
            'become an OU tutor',
            'gain fame and fortune as a computer scientist',
            'need to study very hard',
            'become the OU\'s vice chancellor',
            'suffer nightmares involving the OUBuild owl',
            'receive a beautiful algorithm for your next birthday',
            'gain your tutor\'s undying admiration for your next assignment']

play_game = input('Do you want to play? Hit (y) for yes or (n) for no.')
if play_game == 'y':
    random_number = random.randint(0, len(fortunes))     # When using a range with randint, it includes the last element
    print(random_number)     # To debug
    print(f'We have consulted the magic realm and it has spoken.... YOU... WILL...')
    print(fortunes[random_number])
else:
    print('you didn\'t enter yes so I\'ll be going now...')
