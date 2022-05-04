import random
number = random.randint(1, 100)
guess = ""
guess_diff = 0
while guess != number:
    guess = int(input("Guess the secret number: "))
    if abs(guess - number) > 20:
        print("Cold")
        guess_diff = abs(guess - number)
    elif abs(guess < number) <= 20:
        print("Hot")
        guess_diff = abs(guess - number)
    else:
        print("That is about right!")