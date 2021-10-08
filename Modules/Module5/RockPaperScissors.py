import random
def RPS():
    moves = ['rock','paper','scissors']
    wmoves = ['paper','scissors','rock']
    randChoice = random.choice(moves)
    yamove = str(input('Your move is? (rock, paper, or scissors) = '))
    print(f'Computer selected: {randChoice}')
    if yamove == wmoves[moves.index(randChoice)]:
        print('You won.')
    else:
        if yamove == randChoice:
            print('Tied.')
        else:
            print('You lost.')
    keep = str(input('Keep playing? (y or n) = '))
    if keep == 'y':
        RPS()
RPS()