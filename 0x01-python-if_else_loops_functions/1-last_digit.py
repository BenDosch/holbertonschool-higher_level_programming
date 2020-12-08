#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
print('Last digit of ' + str(number) + ' is', end=' ')
if number < 0 and last != 0:
    print('-', end='')
print(str(last), end=' ')
if  last == 0:
    print('and is 0')
elif number < 0:
    print('and is less than 6 and not 0')
elif last > 5:
    print('and is greater than 5')
elif last < 6 and last != 0:
    print('and is less than 6 and not 0')
