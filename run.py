import random
from hangman_structure import get_hangman
from word import words


def welcome_user():
    """
    This function allows user to input their name.
    """
    
    username = input("Enter Username: ")
    if username.isalpha() is False:
        print("Only Text allowed in Username")
    else:
        print("Welcome "+username)


print('Welcome to Hangman')
welcome_user()

random_word = random.choice(words)
print(
    "Hint: The word has", len(random_word), "letters")
print("================================")

correct_guess = ["_"] * len(random_word)
# below list collect wrong letters guessed by the user
incorrect_guess = []


def update_correctguess_list():
    """
    it will print out the correct letters in the
    correct_guess list
    """
    for i in correct_guess:
        print(i, end=" ")
    print()


update_correctguess_list()
get_hangman(len(incorrect_guess))

while True:

    user_input = input("type a letter: \n")
    print("=====================================")

    if user_input in random_word:
        index = 0
        for i in random_word:
            if i == user_input:
                correct_guess[index] = user_input
            index += 1
        update_correctguess_list()

    else:
        if (user_input not in incorrect_guess):
            incorrect_guess.append(user_input)
            get_hangman(len(incorrect_guess))

        else:
            print("You already guessed it, please try again...")
        print(incorrect_guess)

    if (len(incorrect_guess) > 5):
        print("You lose, please try again")
        print("correct word is ", random_word)
        break

    if "_" not in correct_guess:
        print("Congratulations!!!, you have guessed the correct letter")
        break
