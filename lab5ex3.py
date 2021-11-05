import random
randomnum=random.randint(0,100)
ournum=0
while ournum!=randomnum:
    print("Guess a number between 1 and 100:")
    ournum=int(input())
    if ournum<randomnum:
        print("Increase your number")
    else:
        print("Decrease your number")  
if ournum==randomnum: 
    print("You guessed correctly")          