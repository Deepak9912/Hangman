# Hangman!
Hangman is a word game where the goal is to guess the words until you can guess the complete word. The user will be presented with a number of blank spaces representing the missing letters that they will need to find.

Use the keyboard to guess a letter (I recommend starting with vowels).

If your chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.

After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.

User can only guess six wrong letters, for every wrong guess, user will lose one life and hangman will appear piece by piece.

If user cannot guess the word and exceeds the lives, the game will be over and hangman will die.

The live link can be found [Hangman](https://hang-man22.herokuapp.com/)

![hangman](https://user-images.githubusercontent.com/93731898/155214445-28ca9e32-c1b7-46d1-a33c-6678e9b6cf4e.PNG)


## How to play

* User will be presented with the hangman game, with a hint, number of letters in the word and blank spaces "_" for user to guess.
* If the user selects the letter which matches with any letter in the word, the "_" will be replaced by the letter.
* If user can guess the answer based on guessed letters, a message will appear to congratulate the user.
* If user make a wrong guess, user will lose one life for every incorrect guess.
* User has 6 lives, after every wrong guess, hangman will appear piece by piece.
* After the sixth wrong guess, user hangman will and user will lose the game.

## Technologies used
* [Python](https://www.python.org/)

## Frameworks, Deployement & Libraries
* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)

## Testing
* I used the deployed site to manually entering correct and incorrect data to see how my program responded.
* I used python3 run.py after writing new code to test if they work.

## Validator Testing
I ran through my file in [PEP8 Online](http://pep8online.com/) No errors occured.
