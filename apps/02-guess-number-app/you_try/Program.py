import random
print('------------------------------------')
print('         GUESS THE NUMBER APP')
print('------------------------------------')
print()
name = input('Please enter your name:')
number_random = random.randint(0, 100)
number = -1

while number != number_random:
    number_text = input('Guess a number between 0 and 100? ')
    number = int(number_text)
    if number_random < number:
        print('Sorry {0} but the number {1} is to HIGH' .format(name, number))
    elif number_random > number:
        print('Sorry {0} but number {1} is to LOW' .format(name, number))
    else:
        print('Excellent work {0}, you won, it was {1}!' .format(name, number))
print(number_random)
print('End of the program')
