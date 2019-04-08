#hangman practice game
import random
import re
import os
#DEBUG import time



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
	while True:
		print("Please enter a word")
		#capture user input for word to guess
		solution = input(':')
		#ensure it is a word     			#TODO check against some dictionary? probably too intensive
		if solution.isalpha():
			break
		print("Please enter a valid word")
		print
	
	#parse list and remove all non letters
	correctWord = validLetters(solution)
	#create our underscore list to display correct guesses
	for x in correctWord:
		currentProgress.append('_')
	while (guesses > 0 or gameWon != True):

		os.system('clear')
		print("Guesses remaining:", guesses)	#TODO add a hangman or images?
		print("Word:", currentProgress)
		print("Misses:", missedGuesses)
		#check for win condition before accepting more input
		gameWon = checkWin(currentProgress,correctWord)
		if(gameWon == True):
			print("You win!")
			return
		elif(guesses == 0):
			print("You lose, good day sir")
			return
		#ensure guesses are a single character
		else:
			while True:
				print("Guess a Letter!")
				playerGuess = input(':')
				#TODO ensure player has not guessed this letter already
				if len(playerGuess) == 1 and playerGuess.isalpha():
					break
				print("Please enter a single letter")
				print
				
			for (x, letter) in enumerate(correctWord):
				#check for a correct player guess
				print(len(correctWord))
				if playerGuess == letter:
					currentProgress[x] = letter
					guesses += 1
					break
				#check for a miss
				if(x == len(correctWord)-1 and playerGuess != letter):
					#DEBUG print"entered miss conditional"
					#DEBUG time.pause(1)
					missedGuesses.append(playerGuess)
			guesses -=1
	

if __name__ == "__main__":
	main()