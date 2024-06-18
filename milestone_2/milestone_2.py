import random

word_list = ['bannana', 'mango', 'apple', 'pineapple', 'strawberry']

word = random.choice(word_list)

print(word)


guess = input("Guess a letter: ")
if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")