"""
Program: generator.py
Author: Jenna 
Date: 3/15/2019

Generates and displays sentences using simple grammer and vocabulary.
Words are chosen from a bank of words at random.
"""

import random

# Vocabulary bank: words in four diferent parts of speech
articles = ('A', 'AN', 'THE', 'THAT', 'THIS')
nouns = ('BOY', 'GIRL', 'BAT', 'WOLF', 'BEAR', 'FOX', 'POTATO', 'SCOOBA STEVE')
verbs = ('HIT', 'SAW', 'LIKED', 'JUMPED', 'SMACKED', 'PUNCHED', 'ATE')
prepositions = ('BY', 'ABOUT', 'NEAR', 'INTO', 'WITHIN', 'FROM')
	
def sentence():
	# Builds and returns a sentence
	return nounPhrase() + " " + verbPhrase() + "."

def nounPhrase():
	# Builds an returns a noun phrase. 
	return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
	# Builds and returns a verb phrase
	return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
	# Builds and returns a prepositional phrase.
	return random.choice(prepositions) + " " + nounPhrase()

def main():
	# Allows the user to input the number of sentences to generate.
	number = int(input("Enter the number of sentences: "))

	for count in range(number):
		print(sentence())

# The entry point for program execution
main()


