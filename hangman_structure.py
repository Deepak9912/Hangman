def print_hangman(incorrect_guess):
    if incorrect_guess == 0:
        print("\n+====+ ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("===+"     )
    if incorrect_guess == 1:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|        ")
        print("|        ")
        print("===+"     )
    if incorrect_guess == 2:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|      | ")
        print("|        ")
        print("===+"     )
    if incorrect_guess == 3:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /| ")
        print("|        ")
        print("===+"     )
    if incorrect_guess == 4:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\ ")
        print("|        ")
        print("===+"     )
    if incorrect_guess == 5:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\ ")
        print("|     /  ")
        print("===+"     )
    if incorrect_guess == 6:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\ ")
        print("|     / \ ")
        print("===+"     )
