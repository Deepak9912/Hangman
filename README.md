# Hangman!
Hangman is a word game where the goal is to guess the words until you can guess the complete word. The user will be presented with a number of blank spaces representing the missing letters that they will need to find.

The live link can be found here [Hangman](https://hang-man22.herokuapp.com/)

![start](https://user-images.githubusercontent.com/93731898/155842329-d86935fa-7d1a-4a80-b7f2-229ec6935356.PNG)



## How to play
* User will need to enter the name and once name is entered, user will get a hint that how many letters are there in the word and blank spaces.

* Use the keyboard to guess a letter (I recommend starting with vowels).

* If your chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.

* After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.

* User can only guess six wrong letters, for every wrong guess, user will lose one life and hangman will appear piece by piece.

* If user cannot guess the word and exceeds the lives, the game will be over and hangman will die.

## Features
The game features a welcome message to the user and when user starts the game, it will ask user to type their name. The username must be letters only, if user puts a number, they will get an error message that name must be letters only.

![one](https://user-images.githubusercontent.com/93731898/155842602-1aeb20fb-e7bf-4ac9-8533-a72c1db4ba33.PNG)


When the user type their name, they will get a hello message addressting their name. And the game will begin. User will also get a hint about the length of the word.

![game-begin](https://user-images.githubusercontent.com/93731898/155603982-4c37bfd8-9192-4e1e-8283-b78ec60db81f.PNG)

If the letter guessed by the user matches the random word, it will appear on the blank space where that letter belongs. In the following screenshot, i guessed letter i, and it appeared on the blank space.

![3](https://user-images.githubusercontent.com/93731898/155757179-c9e9cb4c-4978-4c0d-887b-2b6573db481e.PNG)


If the letter guessed by the user is incorrect, than hangman pic will display piece by piece, starting from head to legs. Also the wrong letter will be displayed to the user. If the user selects the letter, already chosen, they will get a message that letter was already chosen and please try again. Following screenshot displays it.

![4](https://user-images.githubusercontent.com/93731898/155757790-61b0f661-bf25-487c-9d16-af31c5ee6b5b.PNG)

If user is unable to guess the word in 6 attempts, then user will lose the game and hangman will die. User will also get the correct answer as shown below. Ans user will need to click on run the program again and play the game again.

![five](https://user-images.githubusercontent.com/93731898/155758231-241dcc5a-a3ff-4917-87b0-183307a692ad.PNG)

If user is able to guess the word, before 6th attempt, user will get a congratulations message and they will win the game.

![six](https://user-images.githubusercontent.com/93731898/155758591-4b8419ab-af5c-4c8d-a009-636e3f16590f.PNG)


## Technologies used
* [Python](https://www.python.org/)

## Frameworks, Deployement & Libraries
* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)

## Testing

* Testing was done throughout the project mainly by running the program in the terminal as well as python debugger. I commited the codes on github after writing every new list or function.
* I used the deployed site to manually entering correct and incorrect data to see how my program responded.
* Tested in both Gitpod terminal and CI Heroku terminal.
* Friends and family members were asked to review game and content to point out any bugs and/or user experience issues.

## Accessibility
1. There are no images on the site.
2. No color was used in creating this project.

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

