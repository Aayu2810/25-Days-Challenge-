import random

# Game symbols
symbols: dict[str, str] = {'rock': '🪨',  # rock
                           'paper': '📄',  # paper
                           'scissors': '✂️'}  # scissors

# Get user input:
player_choice: str = input('Choose rock (🪨), paper (📄), or scissors (✂️): ').strip().lower()
computer_choice: str = random.choice(tuple(symbols))

# Display choices:
print('\nResults')
print('----------------')
print(f'You:      {symbols[player_choice]}  {player_choice}')
print(f'Computer: {symbols[computer_choice]}  {computer_choice}')
print('----------------')

# Determine the winner
if player_choice == computer_choice:
    print('It\'s a tie!')
elif player_choice == 'rock' and computer_choice == 'scissors':
    print('You won with rock! 🪨')
elif player_choice == 'paper' and computer_choice == 'rock':
    print('You won with paper! 📄')
elif player_choice == 'scissors' and computer_choice == 'paper':
    print('You won with scissors! ✂️')
else:
    print('Computer wins! 🤖')

# Homework:
# 1. Make this code loop indefinitely so that you can play forever without
# having to re-run the script each time.
