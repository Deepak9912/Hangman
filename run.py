# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

words = ["near", "announce", "size", "amusement", "safe", "dynamic", "shaky", "boast", "pass", "ancient", "enormous", "shake", "wine", "skinny", "elephant", "glass", "travel", "phone", "reject", "emotion", "stress", "marriage", "calculate", "decide", "grumpy", "foolish", "inexpensive", "squirrel"]

# print(random.choice(words))   tried to get a random word from the list

print("Welcome to Hangman game")
print("___________________________")

def get_random_word():
    """
    this function gets random word from the list
    and allow user to select words until there is _ or blank space
    """
    random_Word = random.choice(words)     #it gets random words from the list of words
    global = random_Word      #using global to make this local variable, a global one
    while "_" in random_Word or " " in random_Word:  
        random_Word = random.choice(words)
    
    return random_Word.upper()


def get_hangman():
    """
    It prints the hangman when user selects wrong character from the word
    """
    if(guess_the_word == 0):
        print("\n+---+")
        print("     |")
        print("     |")
        print("     |")
        print("   ===")
    elif(guess_the_word == 1):
        print("\n+---+")
        print(" O    |")
        print("      |")
        print("      |")
        print("   ===")
    elif(guess_the_word == 2):
        print("\n+---+")
        print(" O    |")
        print(" |    |")
        print("      |")
        print("   ===")
    elif(guess_the_word == 3):
        print("\n+---+")
        print(" O    |")
        print(" |\   |")
        print("      |")
        print("   ===")
    elif(guess_the_word == 4):
        print("\n+---+")
        print(" O    |")
        print("/|\   |")
        print("      |")
        print("   ===")
    elif(guess_the_word == 5):
        print("\n+---+")
        print(" O    |")
        print("/|\   |")
        print("  \   |")
        print("   ===")
    elif(guess_the_word == 6):
        print("\n+---+")
        print(" O    |")
        print("/|\   |")
        print("/ \   |")
        print("   ===")

def guess_the_letter(guessedletter):
    counter = 0
    correct_letter = 0
    for guess in guessedletter:
        if(guess in guessedletter):
            print(random_Word[counter], end " ")
            correct_letter += 1
        else: 
            print("_", " ")
            counter += 0
    
    return correct_letter


get_random_word()