import random
words = ["announce", "size", "amusement", "safe", "dynamic", "shaky"]

def get_randomword():
    """
    the function gets random words from the word list
    """
    random_word = random.choice(words)

    print(random_word.upper())


def get_hangman(incorrect_answer):
    """
    the function will print hangman for incorrect answers    
    """
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

get_hangman(incorrect_answer)



