# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

words = ["near", "announce", "size", "amusement", "safe", "dynamic", "shaky", "boast", "pass", "ancient", "enormous", "shake", "wine", "skinny", "elephant", "glass", "travel", "phone", "reject", "emotion", "stress", "marriage", "calculate", "decide", "grumpy", "foolish", "inexpensive", "squirrel"]

# print(random.choice(words))   tried to get a random word from the list

def get_random_Word(words):
    """
    this function gets a randome word from the word list
    """
    print(random.choice(words))

get_random_Word():