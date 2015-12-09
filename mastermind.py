#Raymond Chaing
#Mastermind

#create randomized code
a=[]
i= [1,2,3,4]
c=0
#create list of 4 random letters from qwerty
for i in range(0,4):
	a.append(random.choice('qwerty'))
	
#enter inputs
print "Welcome to Mastermind"
print "Enter your inputs in this format"
print ""qwer""# probably need to escape this
user= input("Enter your guess:")
guess=list(user)

#while loop to compare code and user input
#allow 10 tries
while c<10:
	for w in a:
		if guess[w] == a[w]:
			print "X"
		else 
			b=w+1
			while b<4
				if guess[b]== a[b]:
					print "O"
				b=b+1
	if guess==a:
		print "You Win"
		c=10
	c=c+1
	print "Guess Again"
	user= input("Enter your guess:")
	guess=list(user)


#at 10 tries reset the code and counter and the game ends