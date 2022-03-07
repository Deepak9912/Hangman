# Hangman!
Hangman is a word game where the goal is to guess the word by selecting different letters until the word is complete. The user is presented with a number of blank spaces representing the missing letters that they will need to find.

The live link can be found here [Hangman](https://hang-man22.herokuapp.com/)

![start](https://user-images.githubusercontent.com/93731898/155842329-d86935fa-7d1a-4a80-b7f2-229ec6935356.PNG)



## How to play
* User will need to enter their name and once entered, the user will be presented with the number of letters in the word and blank spaces for each letter.

* The user will utilise the keyboard to guess a letter (its recommended to start with vowels).

* If the letter, the user choses, exists in the answer, then all the blank spaces, where that letter exists, will be populated with that letter.

* After the user has guessed a few letters, they may be able to guess the answer and fill in the remaining letters.

* The user can only guess six wrong letters, for every wrong guess, the user will lose one life and hangman will appear piece by piece.

* If the user cannot guess the word and exceeds the lives, the hangman will be completed and the game will be over.

## Features
The game features a welcome message to the user and when the user starts the game, it will ask the user to type their name. The username must be letters only, if the user puts a number, an error message with appear instructing the user that the name must be letters only.

![one](https://user-images.githubusercontent.com/93731898/155842602-1aeb20fb-e7bf-4ac9-8533-a72c1db4ba33.PNG)


When the user types their name, a hello message will appear displaying their name and the game will begin. The program will also display the number of letters in the word.

![game-begin](https://user-images.githubusercontent.com/93731898/155603982-4c37bfd8-9192-4e1e-8283-b78ec60db81f.PNG)

If the letter guessed by the user matches any of the letters in the word, the letter will appear in the blank space where that letter belongs. In the following screenshot, the letter "i" was guessed and it appeared on the blank space.

![3](https://user-images.githubusercontent.com/93731898/155757179-c9e9cb4c-4978-4c0d-887b-2b6573db481e.PNG)


If the letter guessed by the user is incorrect, the hangman picture will be populated piece by piece, starting from head to the legs. Also, the wrong letter will be displayed to the user. If the user selects a letter that has already been chosen, the following message will appear "You already guessed it, please try again". The following screenshot displays the message.

![4](https://user-images.githubusercontent.com/93731898/155757790-61b0f661-bf25-487c-9d16-af31c5ee6b5b.PNG)

If the user is unable to guess the word in 6 attempts, the hangman will be completed and the user will lose the game. Also, the correct answer will be displayed to the user as shown in the below screen shot. To replay the game, the user will need to click on run the program and the game will restart.

![five](https://user-images.githubusercontent.com/93731898/155758231-241dcc5a-a3ff-4917-87b0-183307a692ad.PNG)

If the user can guess the word within 6th attempts, the user will receive a congratulations message and they will win the game.

![six](https://user-images.githubusercontent.com/93731898/155758591-4b8419ab-af5c-4c8d-a009-636e3f16590f.PNG)

## Lucid Chart
![Capture](https://user-images.githubusercontent.com/93731898/156442492-ecfac73b-e673-4e4f-89f9-a5623403329a.PNG)


## Future features
I would like to add hints such as country name, movies, famous person in the random selection, so that when user selects the game, they receive a hint in the headline and then they start guessing the word.

## Technologies used
* [Python](https://www.python.org/)

## Frameworks, Deployement & Libraries
* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)

## Testing

* Testing was done throughout the project mainly by running the program in the terminal as well as python debugger. I committed the codes to github after writing every new list or function.
* I used the deployed site to manually enter correct and incorrect data to see how the program responded.
* Tested in both Gitpod terminal and CI Heroku terminal.
* Friends and family members were asked to review game and content to point out any bugs and/or user experience issues.

## Accessibility
1. There are no images on the site.
2. The whole project was built using python, therefore no color was used and no CSS properties were used.

## Issues and bugs found and fixed
1. User Welcome message:  
When I defined the `welcome_user()` function, I wanted to avoid numbers and special characters in the name input to make sure the user uses the correct name and therefore I used the `isalpha()` string in the try and except method, but the user could still input the number in the name input. I then declared the username is None and used username input in while loop with the help of the `isalpha()` string and the code worked.

2. Update guessed letters side by side:  
In the function `update_correctguess_list()`, when I tried for loop to iterate through correct guesses and update them in the blank space, the correctly guessed letters were printed vertically rather than side by side, therefore I used `end = " "` and it removed the error.

3. Index for correct letters:  
I have used `INDEX` with empty value and created a loop in `random_word` to update every correctly guessed letter to fill the blank space where it belonged.

4. Capital letters did not work:  
When I submitted my project to the peer code review, a fellow student advised me that when they input letters in capitals, even though the letter belongs to the word, it was read as the wrong letter. Therefore i added `.lower()` to the `user_input` and the code worked.


## Validator Testing
I ran through my file in [PEP8 Online](http://pep8online.com/) No errors occured.

![pep8](https://user-images.githubusercontent.com/93731898/155856666-65680a60-77bf-4fca-a900-7a2b26b85556.PNG)

## Deployment
I followed the below steps when deploying my project to Heroku, based on the Code Institute instructions:

1. Remove un-needed import features in run.py file
2. Add to requirements.txt file:-
* pip3 freeze > requirements.txt
* Commit changes to Github:
* git commit -m "Add requirements for deployment”

In HEROKU after creating the account:

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

Below resources were used to improve my skills and gain assistance:

1. [Tech with mike](https://www.youtube.com/channel/UCnvj-t_xNcB0ap82KoEm8mQ) For tutorial on hangman.
2. [Net ninja](https://www.youtube.com/channel/UCW5YeuERMmlnqo4oq8vwUpg) For python lists, if else statements and OOP (Object oriented programming).
3. [Kylie Ying](https://www.youtube.com/channel/UCKMjvg6fB6WS5WrPtbV4F5g) For tutorial on hangman.

## Special Thanks
_______________________
Special thanks to my mentor Victor Miclovich, Slack Community, Kasia, Christine from tutor support and my work colleague Angel for their assistance throughout this project.
