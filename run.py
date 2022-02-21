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
        print(i, end = ' ') # end = ' ' will print the letters horizontally
    print()

update_correctguess_list()


while True:

    user_input = input("type a letter: ")
    print("=====================================")

    if user_input in random_word: # this if statement will allow to update the correct guess letter at correct index
        index = 0
        for i in random_word:
            if i == user_input:
                correct_guess[index] = user_input
            index += 1
        update_correctguess_list()

    else:
        if user_input not in incorrect_guess:
            incorrect_guess.append(user_input)
        else:
            print("You already guessed it, please try again...")
        print(incorrect_guess)
    
    if len(incorrect_guess) > 6:
        print("You lose, please try again")
        print('correct word is ', random_word)
        break
    
    if '_' not in correct_guess:
        print("Congratulations!!!, you have guessed the correct letter")
        break



