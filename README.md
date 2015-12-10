# project3
#This program will be a python version of mastermind.
#Mastermind is a game of code creation and code breaking. The basic game is played this way.

#The code maker selects 4 symbols out of 6 and sets the code. The symbols can be repeated, but no spaces may be left blank. The code breaker then has 10 tries to try and break the code. They do this by guessing what the code it. On each guess the code maker indicates how many symbols have been guessed correctly and are in the correct location or how many symbols are guessed correctly but not in the correct location.

#For example, we are going to use the symbols: q,w,e,r,t,and y. If the code maker has selected this as the code: q r t y. This is how the game might be played:

#First guess: q w e r So then the code maker would indicate the following: X O 
#Second guess: w e r t So then the code maker would indicate the following: O O

#In this example X indicates that a correct symbol was placed in the right place, that was the # for the first guess. Then the O indicates that a correct symbol was chosen but it was not in the correct place, that was the r in the first guess.

#For the second guess since the w was removed, we lost the X but now the t has been guessed but both it and the r are in the wrong locations so two O's have been shown.

#If a symbol is just plain ole wrong, then nothing is displayed, hence only two symbols being displayed for both the first and second guesses.

#The game ends when either 10 turns are up or when the code breaker guesses the code.

#Repeated inputs will result in more than one match ie: if the code is qwer and the user inputs wwww
#the output will be OXOO
#The code can be run by using the command line with the command python mastermind.py when the file is in the correct pathway