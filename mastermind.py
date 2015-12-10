#Raymond Chaing
#Mastermind

#create randomized code
a=[]
i= [1,2,3,4]
c=0
u=[]
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
        if guess[w] == a[w]:
            print ("X")
            continue
        else:
            if guess[w]in a:
                print("O")
                continue
    if guess==a:
        print ("You Win")
        break
    c=c+1
    print ("Guess Again")
    user= input("Enter your guess:")
    guess=list(user)


#at 10 tries reset the code and counter and the game ends
