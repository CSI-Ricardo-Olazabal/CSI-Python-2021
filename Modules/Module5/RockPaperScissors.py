import random
def RPS():
    moves = ['rock','paper','scissors']
    wmoves = [moves[1],moves[2],moves[0]]
    randChoice = random.choice(moves)
    yamove = str(input(f'Your move is? ({moves[0]}, {moves[1]}, or {moves[2]}) = '))
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