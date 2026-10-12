#guess no from 1 to 10
import random
n = int(input("Enter a Number: "))
guess = random.randint(1,10)
if n==guess:
    print("Corret guess!")
else :
    print("Wrong guess, number was",guess)