import random
number = random.randint(1, 100)
print("*****",number)
guess = ""
guess_diff = 0
while guess != number:
    guess = int(input("Guess the secret number: "))
    delta = abs(guess - number) 
    if guess == number:
        print("That is about right!")
        break

    if (delta > 20):
        print("Cold ", end='')
    if (delta <= 20):
        print("Hot ", end='')

    if (delta > guess_diff) and (guess_diff != 0):
        print("Getting colder")
    if (delta < guess_diff) and (guess_diff != 0):
        print("Getting warmer")
    guess_diff = delta