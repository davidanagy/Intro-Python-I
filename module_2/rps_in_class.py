import random

# Create a RPS game where player can type r, p, or s, the computer chooses
# a random move, and the game tells you who won.

# You should be able to play multiple games and the game will tell you
# your score after each round.

# Type q to quit.


# Create a REPL

wins = 0
losses = 0
ties = 0

choices = ['r', 'p', 's']

win_matrix = {'r': {'r': 'tie', 'p': 'loss', 's': 'win'},
              'p': {'r': 'win', 'p': 'tie', 's': 'loss'},
              's': {'r': 'loss', 'p': 'win', 's': 'tie'}}

# LOOP
while True:
    # PRINT
    print(f'Score: {wins} / {losses} / {ties}')
    # READ
    cmd = input('-> ')
    # EVAL
    cpu_cmd = random.choice(choices)
    # If q, quit the loop
    if cmd == 'q':
        print('Goodbye!')
        break
    elif cmd in ['r', 'p', 's']:
        result = win_matrix[cmd][cpu_cmd]
        if result == 'win':
            print('You win!')
            wins += 1
        elif result == 'loss':
            print('You lose...')
            losses += 1
        else:
            print('You tie')
            ties += 1
    else:
        print('Please enter "r", "p", "s", or "q"')
