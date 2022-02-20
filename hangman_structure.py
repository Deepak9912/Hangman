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
