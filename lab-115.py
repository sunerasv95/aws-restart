# -------- Working with Loops

import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#---- Working with a while loop
number = random.randint(1, 10)
isGuessRight=False

while isGuessRight != True:
    userGuess = input("Guess the number betweeen 1 to 10 ?")
    
    if(int(userGuess) == number):
        print("You guessed {}. That is correct! You win!".format(userGuess))
        isGuessRight = True;
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(userGuess))
    
# ------Writing the for loop

for n in range(0,10):
    print(f'Number: {n}')