import random
words = ["announce", "amusement", "ankle"]


random_word = random.choice(words)  # it will allow me to pick random words from the words list
print("Hint: The word has", len(random_word), "letters")  # it will print a statement with the length of word
print("================================")

correct_guess = ["_"] * len(random_word)  # an empty list which will collect the correct guess words from the user
incorrect_guess = []  # it will collect wrong letters guessed by the user

def update_correctguess_list():
    """
    it will print out the correct letters in the correct_guess list
    """
    for i in correct_guess:
        print(i, end = ' ')
    print()

update_correctguess_list()

while True:

    user_input = input("type a letter: ")
    print("=====================================")

    if user_input in random_word:
        correct_guess.append(user_input)
        print("Correct guess ", correct_guess)
    else:
        incorrect_guess.append(user_input)
        print("Incorrect guess ", incorrect_guess)



