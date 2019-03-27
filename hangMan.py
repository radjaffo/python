#hangman practice game
import random
import re
import os



#use regex to remove all non letters, ensure we have a valid format to parse 
def validLetters(initialWord):
	letters_only = re.sub("[^a-zA-Z +]",'',initialWord)
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
	guesses = 6			#TODO add difficulty levels for different amounts of guesses
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
		print("Guesses remaining:", guesses)	#TODO make print block look better
		print(currentProgress)
		print("Misses:", missedGuesses)
		#check for win condition before accepting more input
		gameWon = checkWin(currentProgress,correctWord)
		if(gameWon == True):
			print("You win!")
			return
		if(guesses == 0):
			print("You lose, good day sir")
			return
		print("Guess a Letter!")
		playerGuess = raw_input()	#TODO ensure only a single char is entered
		#TODO find a more pythonic way to do this, using a temp int counter feels very C++
		i = 0
		for letter in correctWord:
			#check for a hit
			if playerGuess == letter:
				currentProgress[i] = letter
				guesses += 1
				break
			i+=1
			#check for a miss
			if(i == len(correctWord) and playerGuess != letter):
				missedGuesses.append(playerGuess)
		guesses -=1
	

if __name__ == "__main__":
	main()