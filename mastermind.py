#Raymond Chaing
#Mastermind

#create randomized code
#holds the random code
a=[]
#loop counter
c=0
import random 
#create list of 4 random letters from qwerty
for i in range(0,4):
    a.append(random.choice('qwerty'))
print (a)
	
#enter inputs
print ("Welcome to Mastermind")
print ("Enter your inputs without parentheses around them")
user= input("Enter your guess:")
guess=list(user)

#while loop to compare code and user input
#allow 10 tries
while c<10:
    for w in range(0,4):
        #print correct position
        if guess[w] == a[w]:
            print ("X")
            continue
        else:
            #print correct guess
            if guess[w]in a:
                print("O")
                continue
    #determine win
    if guess==a:
        print ("You Win")
        break
    c=c+1
    print ("Guess Again")
    user= input("Enter your guess:")
    guess=list(user)


#at 10 tries reset the code and counter and the game ends
