#hangman practice game
import random
import re
import os



#use regex to remove all non letters, ensure we have a valid format to parse 
def validLetters(s):
	letters_only = re.sub("[^a-zA-Z +]",'',s)
	tempWord = letters_only.lower()
	words = [i for i in tempWord]
	return words

#compare the two lists to see if win condition is met
def checkWin(list1, list2):
	if list1 == list2:
		return True
	else:
		return False


def main():
	guesses = 6
	gameWon = False
	correctWord = []
	missedGuesses = []
	currentProgress = []

	print("Welcome to Hangman!")
	print "Please enter a word: "
	#capture user input for word to guess
	solution = raw_input()
	#parse list and remove all non letters
	correctWord = validLetters(solution)
	#create our underscore list to display correct guesses
	for x in correctWord:
		currentProgress.append('_')
	while (guesses > 0 or gameWon != True):

		os.system('clear')
		print("Guesses remaining:", guesses)
		print(currentProgress)
		print("Misses:", missedGuesses)
		#check for win condition before accepting more input
		gameWon = checkWin(currentProgress,correctWord)
		if(gameWon == True):
			print("You win!")
			return
		print("Guess a Letter!")
		playerGuess = raw_input()	#need to ensure only a single char is entered
		#find a more pythonic way to do this, using a temp int counter feels very C++
		i = 0
		for letter in correctWord:
			if playerGuess == letter:
				currentProgress[i] = letter
			i+=1

	

if __name__ == "__main__":
	main()