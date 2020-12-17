'''
Number Guessing Game. The game is as follows: the (human) player comes up with a whole number between 1 and 100 in their mind. 
The robot will repeatedly make a guess, say 26; after every guess, the human player provides feedback to the robot saying whether
 its guess was correct  (=26), too small (>26) or too large (<26).
  The robot aims to guess the correct number in the smallest number of guesses.
'''

#Code
import random

start=1
end=100
def guessNumber(start,end):
    guess=random.randrange(start,end)
    return guess

while True: 
    #guess=random.randrange(start,end)
    guess=guessNumber(start,end)
    print("Did you think of ",guess,"? Enter Y or N")
    check=input()
    if check=='Y' or check=='y':
        print("Right guess by computer")
        break
    else:
        print("Enter 1 if number is less than ",guess)
        print("Enter 2 if number is greater than ",guess)
        choice=int(input())
        if choice==1:
            end=min(guess,end)
            mid=int((start+end)/2)
            guessNumber(start,mid)
            
        else:
            start=max(guess,start)
            mid=int((start+end)/2)
            guessNumber(mid,end)
