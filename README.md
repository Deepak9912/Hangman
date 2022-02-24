# Hangman!
Hangman is a word game where the goal is to guess the words until you can guess the complete word. The user will be presented with a number of blank spaces representing the missing letters that they will need to find.

The live link can be found [Hangman](https://hang-man22.herokuapp.com/)

![hangman](https://user-images.githubusercontent.com/93731898/155214445-28ca9e32-c1b7-46d1-a33c-6678e9b6cf4e.PNG)


## How to play
* User will need to enter the name and once name is entered, user will get a hint that how many letters are there in the word and blank spaces.

* Use the keyboard to guess a letter (I recommend starting with vowels).

* If your chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.

* After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.

* User can only guess six wrong letters, for every wrong guess, user will lose one life and hangman will appear piece by piece.

* If user cannot guess the word and exceeds the lives, the game will be over and hangman will die.

## Features
The game features a welcome message to the user and when user starts the game, it will ask user to type their name, once name is entered, user will get a hello message and the game will start.

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

## Credits
_____________________________________
Special thank you to Dave Horrocks for his support in Slack and the Slack community that volontereed and gave thorough feedback on my Peer Code Review post.

Below resources were used to improve my skills and find assistance:

1. [Tech with mike](https://www.youtube.com/channel/UCnvj-t_xNcB0ap82KoEm8mQ) For tutorial on hangman.
2. [Net ninja](https://www.youtube.com/channel/UCW5YeuERMmlnqo4oq8vwUpg) For python lists, if else statements and OOP (Object oriented programming).
3. [Kylie Ying](https://www.youtube.com/channel/UCKMjvg6fB6WS5WrPtbV4F5g) For tutorial on hangman.

