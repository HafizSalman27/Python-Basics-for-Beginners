# Special Program: Number Guessing Game

import random 

num = random.randint(1, 50)
guess = int(input('Enter a number between 1 and 50: '))

while guess != num:
   
   if guess < num:
    print ('Your Guess is too low.')
   elif guess > num:
    print ('Your Guess is too high.')

   guess = int(input('Guess again: '))    

print ('You guessed it right.')        
