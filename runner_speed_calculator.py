# This works out the average speed of a track runner

distance = float(input('What distance did you run in meters? '))

time = float(input('What was your time in seconds? '))

speed = round(distance/time, 2)

print(f'You speed was {speed} m/s!')
