import random
ver = 5
moves = ['rock','paper','scissors']
wmoves = [moves[1],moves[2],moves[0]]
score = 0
print(f'ITS TIME FOR {moves[0].upper()} {moves[1].upper()} {moves[2].upper()}!!!!!!!')
print(f'(RPS code ver {ver} by Ricardo Olazabal)')
def RPS(score):
    randChoice = random.choice(moves)
    yamove = str(input(f'Your move is? ({moves[0]}, {moves[1]}, or {moves[2]}) = '))
    print(f'Computer selected: {randChoice}')
    if yamove == wmoves[moves.index(randChoice)]:
        print('You won.')
        score += 1
    else:
        if yamove == randChoice:
            print('Tied.')
        else:
            print('You lost.')
            score -= 1
    print(f'Your score is: {score}')
    keep = str(input('Keep playing? (y or n) = '))
    if keep == 'y':
        RPS(score)
    else:
        print(f'Your score this game was {score}, share with friends!!!!')
def RPSHard(score):
    yamove = str(input(f'Your move is? ({moves[0]}, {moves[1]}, or {moves[2]}) = '))
    print(f'Computer selected: {wmoves[moves.index(yamove)]}')
    print('You lost.')
    score -= 1
    print(f'Your score is: {score}')
    keep = str(input('Keep playing? (y or n) = '))
    if keep == 'y':
        RPSHard(score)
    else:
        print(f'Your score this game was {score}, you have no friends.')
mode = str(input('Which mode will you play? (classic or hard) = '))
if mode == 'hard':
    RPSHard(score)
else:
    RPS(score)