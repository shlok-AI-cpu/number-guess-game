# number guessing game
# used random, if-else and random
import random
print("hey enter your name")
name=input()
print(name, ",such a nice name")
print("Let's move towards the game")

og=(random.randint(0,100))
print(name,"guess the number between 0 and 100😎")
guess=int(input())
while guess!=og:
    if guess<og:
        print("your guess is low, try again")
        guess=int(input())
    elif guess>og:
        print("your guess is high, try again")
        guess=int(input())
while guess==og:
    print("congratulations",name,"you guessed the number correctly")
    break
