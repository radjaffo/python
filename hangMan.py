#hangman practice game
import random
import re

#def gallowLoop():

#use regex to remove all non letters 
def splitWord(s):
	letters_only = re.sub("[^a-zA-Z +]",'',s)
	tempWord = letters_only.lower()
	words = [i for i in tempWord]
	return words

def main():
	guesses = 6
	missedGuesses = []
	correctWord = []
	currentProgress = []
	print("Welcome to Hangman!")
	print "Please enter a word: "
	#capture user input for word to guess
	solution = raw_input()
	#parse list and remove all non letters
	correctWord = splitWord(solution)
	#create our underscore list to display correct guesses
	for x in correctWord:
		currentProgress.append('_')
	print currentProgress
	#tempWord = solution.lower()
	#correctWord = [i for i in tempWord]
	#print correctWord



	

if __name__ == "__main__":
	main()