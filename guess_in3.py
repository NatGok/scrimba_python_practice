
num = 67
guess = 0
guess_limit=7
guess_number = 0

# while guess_number < guess_limit:
#     guess = int(input('Choose a number between 1 and 100: '))
#     guess_number += 1
#     if guess == num:
#         print("Amazing you got it right!")
#         break
#     elif guess < num:
#         print("Too low, try again")
#     else:
#         print("Too high, try again")


num = 76
guess = 0
guess_limit=5
guess_number = 0


guess = int(input(f'Guess a number 1-20: '))
while guess_number < guess_limit:
    
    if guess != num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 1-100: '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    
if guess != num:
    print(f'Sorry you lose! It was {num}')