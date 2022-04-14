import random
string = 'random item from the container'
word_list  = string.split()
random.shuffle(word_list)
new_word = list(random.choice(word_list))
random.shuffle(new_word)
shuffle_word = ''.join(new_word)
guess = ''
while True:
    guess = input(f"Try to solve this jumbled word: {shuffle_word}    ")
    if guess in word_list:
        print("Congratulations your a Winner")
        break
    else:
        print("Incorrect, please try again.")