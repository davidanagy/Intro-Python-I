"""
Planning:
### necessary variables
welcome_message: STRING (the welcome message will be an English phrase)
historical_data_message: STRING (three separate numbers
surrounded by an English explanation)
quit_message: STRING (English phrase)
win_message: STRING (English phrase)
loss_message: STRING (English phrase)
tie_message: STRING (English phrase)

wins: INTEGER (with each win, number goes up by one)
ties: INTEGER (with each tie, number goes up by one)
losses: INTEGER (with each loss, number goes up by one)

choice_options: LIST (three separate choices, grouped together)

computer_choice: STRING (doesn't really matter but string is clearest,
                         since the choices are "rock," "paper," and "scissors")
user_choice: STRING (same as above)


### procedures
"start" function:
1. display welcome_message
2. load historical_data and populate variables with data
3. display historical_data_message with historical data
4. prompt user to make a choice between rock, paper, scissors, or quit

"quit" function:
  1. if quit, update text file with current wins, ties, losses data and exit game

"determine_winner" function:
  2. if not quit, move on to step 5
5. computer makes a choice between rock, paper, and scissors
6. compare user choice and computer choice
7. display message based on result of comparison
8. update wins, ties, losses appropriately
9. return to step 4
"""

import random


# The procedures below are divided differently from how I'd do it,
# but I'll copy the code provided.

# removing the welcome_message definition since it's superfluous
def show_welcome_message():
    # welcome_message = 'Welcome to Rock, Paper, Scissors!'
    print(welcome_message)


# rewriting this one a bit to use the "with" command
def get_historical_data():
    with open('history.txt', 'r') as text_file:
        text_data = text_file.read().split(',')
    return {
        'wins': int(text_data[0]),
        'ties': int(text_data[1]),
        'losses': int(text_data[2])
    }


# changing a bit to use the .format() method
def show_historical_data_message():
    print(historical_data_message.format(
        score['wins'], score['ties'], score['losses']
    ))


def get_user_choice(prev_user, prev_comp):
    if prev_user is not None:
        print(f'Last time, you picked {prev_user} and your opponent picked {prev_comp}.')
    print('Choose your fighter!')
    choice = input('[1] rock    [2] paper   [3] scissors    [9] quit\n')
    return choice_options[int(choice)]


# modifying a bit to use the "with" command
def quit_game(wins, ties, losses):
    show_historical_data_message()
    print(quit_message)
    with open('history.txt', 'w') as text_file:
        text_file.write(str(wins) + ',' + str(ties) + ',' + str(losses))


def compare_choices_and_get_result(user, computer):
    print(computer_choice_message.format(computer))
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
         return 'win'
    else:
        return 'loss'


def display_result_message_and_update_score(result):
    if result == 'tie':
        print(tie_message)
        score['ties'] += 1
    elif result == 'win':
        print(win_message)
        score['wins'] += 1
    else:
        print(loss_message)
        score['losses'] += 1
    show_historical_data_message()


score = {
    'wins': 0,
    'ties': 0,
    'losses': 0
}

welcome_message = 'Welcome to Rock, Paper, Scissors!'
historical_data_message = 'Wins: {}, Ties: {}, Losses: {}'
quit_message = 'Thanks for playing Rock, Paper, Scissors!'
win_message = 'Congratulations, you won!'
loss_message = 'Sorry, you lost!'
tie_message = 'It was a tie.'
computer_choice_message = 'The computer chose {}.'

historical_data = get_historical_data()
score['wins'] = historical_data['wins']
score['ties'] = historical_data['ties']
score['losses'] = historical_data['losses']

# The given code has this as a dictionary instead of a list.
# A list would work too, but I'll use the dictionary provided.
choice_options = {
    1: 'rock',
    2: 'paper',
    3: 'scissors',
    9: 'quit'
}

### Start of Game
show_welcome_message()
show_historical_data_message()

### First user choice
user_choice = get_user_choice(None, None)

### Game Loop
while user_choice != 'quit':
    computer_choice = choice_options[random.randint(1,3)]
    result = compare_choices_and_get_result(user_choice, computer_choice)
    display_result_message_and_update_score(result)
    user_choice = get_user_choice(user_choice, computer_choice)

### Quit game if user exits game loop
quit_game(score['wins'], score['ties'], score['losses'])

"""
The requested features each required different methods for implementing them.
For instance, several times it was requested to display the current score--after
every user choice and before exiting the program. Luckily we already had a function
to do this, "show_historical_data_message()," so all I had to do was run that function
in the appropriate areas of the code. Displaying the computer's choice was also just
a matter of adding a line to the "compare_choices..." function.
On the other hand, displaying the previous round's user and computer choices was more
complicated. It had to go alongside the prompt for the user choice--i.e., the
"get_user_choice()" function--but since the user and computer choices can change,
that meant I had to modify the function to take "prev_user" (previous user choice)
and "prev_comp" (previous computer choice) as arguments. But that caused a problem for what
to do at the very beginning, during the user's first choice. I decided to implement a
default "None" value for prev_user and prev_comp, and to only display the
"Last time, you picked..." message when the value wasn't "None."
"""
