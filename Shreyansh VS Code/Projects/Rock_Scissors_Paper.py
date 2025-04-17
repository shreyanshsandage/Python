import random
print ("Welcome to Rock, Paper, Scissors!")
player = input("Enter your choice (rock/paper/scissors): ")
opponent = random.choice(['rock', 'paper', 'scissors'])
print(f'Opponent choice is {opponent}')
if player == opponent:
    print("It's a tie!")
elif player == 'rock':
    if opponent == 'scissors':
        print('You win!')
    else:
        print('You lose!')
elif player == 'paper':
    if opponent == 'rock':
        print('You win!')
    else:
        print('You lose!')
elif player == 'scissors':
    if opponent == 'paper':
        print('You win!')
    else:
        print('You lose!')
else:
    print('Please enter a valid move') 