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

## Deployment
I followed below steps when deploying my project to Heroku, based on Code Institute instructions:

1. Remove un-needed import features in run.py file
2. Add to requirements.txt file:-
* pip3 freeze > requirements.txt
* Commit changes to Github:
* git commit -m "Add requirements for deployment”

In HEROKU after creating account:

1. "Create new App"
2. Give the App a unique name and enter region
3. Click on "Create App"
4. Click on "Settings" on your new App Dashboard
5. Scroll down to Config Vars where in my instance I only inserted KEY: PORT and VALUE: 8000 since I have no creds.json files to add.
6. Press Add-button
7. Scroll down to Buildpacks and press the icon for Python, click Save Changes, then press the icon for Nodejs and save changes. These Buildpacks need to be in below order:

    Python
    NodeJS
8. Go to Deploy section tab and scroll down to Deployment Method. I connected to my Github pages and could thereafter search for my Github Repository "Parents Allowance Calculator" and then click connect.
9. Scroll down to Automatic and Manual Deploys sections. I clicked on Automatic Deployment so that my changes that I push to github automatically updates in Heroku.
10. Then in the Manual Deploy section, press Deploy Branch.
11. After project has been deployed successfully I clicked the View-button to see the program run in the terminal.
