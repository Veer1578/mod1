import random

playing = True
num = str(random.randint(0, 10))
print('I have a number between 0 and 10. You have to guess it.')
print('Game will end when number is guessed correctly.')

while playing:
    guess = input('Give me your best guess: ')
    if num == guess:
        print('Yay! You got it correct')
        break
    else:
        print('You got it wrong.')