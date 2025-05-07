import random

while True:
    userC = input('Chose between rock, paper and scissors: ')
    compO = ['rock', 'paper', 'scissor']
    compC = random.choice(compO)

    print(f'You chose {userC} and the computer chose {compC}')

    if userC == compC:
       print('It is a tie')
    elif userC == 'rock':
        if compC == 'scissor':
            print('You win')
        else:
            print('You lose')
    elif userC == 'paper':
        if compC == 'rock':
            print('You win')
        else:
            print('You lose')
    elif userC == 'scissor':
        if compC == 'rock':
            print('You lose')
        else:
            print('You win')

    again = input('Want to play again(y,n): ')
    if again != 'y':
        break
