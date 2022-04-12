import random
number = random.randint(1, 100)
guess = ""
while guess != number:
    guess = int(input("Try to guess what number I am thinking of: "))
    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else:
        print("That is about right!")