import random
words = ["announce", "size", "amusement", "safe", "dynamic", "shaky"]

def get_randomword():
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
    guessed_letters = set(random_word)  # it will keep a track of all the letters in the random word
    letters_selected_by_user = set() # it will keep a track of letter selected by the user
      
    while len(guessed_letters) > 0:
        print("you have used the letters: ", " ".join(letters_selected_by_user))

        random_word_list = [letter if letter in guessed_letters else "-" for letter in random_word]
        print("current word is: ", " ".join(random_word_list))
        
        #user input
        user_input_letter = input("guess a letter: ").upper() 

        if user_input_letter in guessed_letters:
            user_input_letter.add(guessed_letters)
        else:
            user_input_letter.add(letters_selected_by_user)



# getting an input from the user
get_user_input = input("Make a guess...")
print(get_user_input)



def print_hangman():
    if incorrect_answer == 0:
        print("\n+===+")
        print("      |")
        print("      |")
        print("      |")
        print("   ===+")
    if incorrect_answer == 1:
        print("\n+===+")
        print(" O    |")
        print("      |")
        print("      |")
        print("   ===+")
    if incorrect_answer == 2:
        print("\n+===+")
        print(" O    |")
        print(" |    |")
        print("      |")
        print("   ===+")
    if incorrect_answer == 3:
        print("\n+===+")
        print(" O    |")
        print("/|    |")
        print("      |")
        print("   ===+")
    if incorrect_answer == 4:
        print("\n+===+")
        print(" O    |")
        print("/|\   |")
        print("      |")
        print("   ===+")
    if incorrect_answer == 5:
        print("\n+===+")
        print(" O    |")
        print("/|\   |")
        print("/     |")
        print("   ===+")
    if incorrect_answer == 6:
        print("\n+===+")
        print(" O    |")
        print("/|\   |")
        print("/ \   |")
        print("   ===+")


