import random
words = ["announce", "amusement", "ankle"]

def get_randomword(words):
    """
    the function gets random words from the word list
    """
    global random_word
    random_word = random.choice(words)  # gets random word from the list
    # print(random_word.upper())

    return random_word.upper()   # it will return the random word in uppercase



def hangman():
    """
    it allows user to guess a letter
    if the letter is in the random word, it will be printed on the blank space
    if the letter is wrong, hangman will display  
    """
    random_word = random.choice(words)
    right_guess = []
    wrong_guess = []

    while True:

        user_input = input("type a letter: ")
        print("=====================================")

        if user_input in random_word:
            right_guess.append(user_input)
            print("Correct guess ", right_guess)
        else:
            wrong_guess.append(user_input)
            print("Incorrect guess ", wrong_guess)


hangman()