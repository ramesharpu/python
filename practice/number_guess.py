import random


num = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for guess_taken in range(1, 7):
    print('Take a guess:')
    guess = int(input())

    if guess < num:
        print('Your guess is too low')
    elif guess > num:
        print('Your guess is too high')
    else:
        break  # This is for the correct guess!

if guess == num:
    print('Good job! You guessed my number in ' + str(guess_taken) + ' guesses!')
else:
    print('Better luck next time, the number I was thinking is ' + str(num))