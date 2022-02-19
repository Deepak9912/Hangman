import random
words = ["announce", "size", "amusement", "safe", "dynamic", "shaky"]

def get_randomword():
    """
    the function gets randon words from the word list
    """
    random_word = random.choice(words)

    print(random_word.upper())

get_randomword()



