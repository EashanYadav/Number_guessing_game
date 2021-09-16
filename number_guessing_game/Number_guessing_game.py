import random
import math
#taking inputs
lower=int(input("Enter lower bound:- "))
upper=int(input("Enter upper bound:- "))
# generating random number between
# the lower and upper
x=random.randint(lower,upper)
print("\n\tYou've only",round(math.log(upper-lower+1,2)),"chances to get integer\n")
# Initializing the number of guesses.
count=0
# for calculation of minimum number of
# guesses depends upon range
while count<math.log(upper-lower+1,2):
    count+=1
# taking guessing number as input
    guess = int(input("Guess a number:- "))
# Condition testing
    if x==guess:
        print("congratulations you guessed the answer in",count,"try")
        break
    elif x>guess:
        print("you guessed too small")
    elif x<guess:
        print("you guessed too large")
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper-lower+1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")