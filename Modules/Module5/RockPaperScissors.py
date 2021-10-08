import random
def RPS():
    moves = ['rock','paper','scissors']
    randChoice = random.choice(moves)
    print(f'Computer selected: {randChoice}')
    yamove = str(input('Your move is? (rock, paper, or scissors) = '))
    if (randChoice == 'rock' and yamove == 'paper') or (randChoice == 'paper' and yamove == 'scissors') or (randChoice == 'scissors' and yamove == 'rock'):
        print('You won.')
    else:
        print('You lost.')
    keep = str(input('Keep playing? (y or n) = '))
    if keep == 'y':
        RPS()
RPS()