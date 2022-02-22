def get_hangman(x):
    """
    function to print hangman when user enters a wrong input
    There are total 6 trials to the user and after every incorrect input, hangman will be displayed
    """
    if x == 0:
        print("\n+====+ ")
        print("|      | ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("===+"     )
    if x == 1:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|        ")
        print("|        ")
        print("===+"     )
    if x == 2:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|      | ")
        print("|        ")
        print("===+"     )
    if x == 3:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /| ")
        print("|        ")
        print("===+"     )
    if x == 4:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\ ")
        print("|        ")
        print("===+"     )
    if x == 5:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\ ")
        print("|     / \ ")
        print("===+"     )

