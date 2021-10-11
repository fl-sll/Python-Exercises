import random
lower = int(input("Enter a lower boumd: "))
upper = int(input("Enter an upper bound: "))
x = random.randint(lower, upper)

print("You only have 10 chances")
count = 0
while count < 10:
    count += 1

    guess = int(input(f"Guess a number from {lower}-{upper}:"))

    if x == guess:
        print("Congratulations, you picked the right number")
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guessed too high")

if count >= 10:
    print("The number is", x)