empty_list = []
word = ''
while word != 'quit':
    word = input("Enter words, use word quit to exit: ")
    empty_list.append(word)
# remove quit
full_list = empty_list[:-1]
index = 0
even_list = []
odd_list = []
for word in full_list:
    if index % 2 == 0:
        odd_list.append(word)
    else:
        even_list.append(word)
    index = index + 1
print(odd_list)
print(even_list)