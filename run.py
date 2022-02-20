import random
words = ["announce", "size", "amusement", "safe", "dynamic", "shaky"]

def get_randomword(words):
    """
    the function gets random words from the word list
    """
    random_word = random.choice(words)  # gets random word from the list
    # print(random_word.upper())

    return random_word.upper()   # it will return the random word in uppercase



def hangman():
    """
    the function defines hangman   
    """
    random_word = get_randomword(words)
    randomword_letters = set(random_word)  # it will keep a track of all the letters in the random word
    guessed_wrong_letters = set() # it will keep a track of letter selected by the user
      
    while len(randomword_letters) > 0:
        print('letters guessed: ', ' '.join(guessed_wrong_letters))  # this allows me to display the guessed letter to the user

        random_word_list = [letter if letter in guessed_wrong_letters else "-" for letter in random_word]
        print('current word: ', ' '.join(random_word_list))
        
        #user input
        user_input_letter = input("guess a letter: ").upper() 
        if user_input_letter in randomword_letters:
            randomword_letters.add(user_input_letter)
        else:
            guessed_wrong_letters.add(user_input_letter)

hangman()