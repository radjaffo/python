#python dice rolling simulator
#3/10/19
import random

choice = 0
print("Welcome to the dice rolling simulator")
#simple list of 3 options, continue until choice flag is satisfied
while(choice != 3):
	print("1. Roll a d6?")
	print("2. Roll a d20?")
	print("3. Quit")
	choice = input()	#capture integer input, would want it to accept all input eventually

	if(choice == 1):
		print("Rolling the dice!")
		print
		dice = random.randint(1,6)
		print "The d6 landed on ", dice, "!" 
		print
		
	elif(choice == 2):
		print("Rolling a d20!")
		dice = random.randint(1,20)
		print 
		print "The d20 landed on ", dice, "!"
		print

	elif(choice == 3):
		print("Quitting, have a nice day!")
		break

	else:
		print("Please use the numbers 1-3 to select an option")
		print()