import random


def guess(randNum, guessNum):
    randNum = str(randNum)
    guessNum = str(guessNum)
    if guessNum != randNum:
        print("Sorry! Maybe next time, your number is %s, and the answer is %s" % (guessNum, randNum))
    else:
        print("Congratulations! You WIN! your number is %s, and the answer is %s" % (guessNum, randNum))


print("Let's play a game!")
print("I have a number in my mind, if you can guess it, you will win $1.")
randNum = random.randint(10, 15)
guessNum = input("Please guess a number between 10 and 15: ")
guess(randNum, guessNum)