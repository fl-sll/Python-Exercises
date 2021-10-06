import random

x = random.randint(1,100)

print("You only have 10 chances")
count = 0
while count < 10:
    count += 1

    guess = int(input("Guess a number from 1-100:"))

    if x == guess:
        print("Congratulations, you picked the right number")
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guessed too high")
if count >= 10:
    print("The number is", x)