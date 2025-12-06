import random

randomnum = random.randint(1,10)

def bigguess(guess):
    assert guess is type(int), "Input must be an integer between 1 and 10"
    if guess == randomnum:
        print("Winna!")
        return False
    else:
        print("Try Again")
        return True

while True:
    guess = input("GUESS A NUMBER NOW BETWEEN 1 & 10")
    bigguess(guess)