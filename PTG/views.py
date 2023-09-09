# ---------------------------------------------
# PTG/views.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------

#Django imports

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

#Python imports

import random

#Reference dictionaries

lowercaseVowelsDictionary = {
	'A': ['a', 'ą'],
	'E': ['e', 'ę'],
	'I': ['i'],
	'O': ['o', 'ó'],
	'U': ['u'],
}

uppercaseVowelsDictionary = {
	'A': ['A', 'Ą'],
	'E': ['E', 'Ę'],
	'I': ['I'],
	'O': ['O', 'Ó'],
	'U': ['U'],
}

lowercaseConsonantsDictionary = {
	'C': ['c', 'ć'],
	'D': ['d'],
	'L': ['l', 'ł'],
	'N': ['n', 'ń'],
	'S': ['s', 'ś'],
	'W': ['w'],
	'Y': ['y'],
	'Z': ['z', 'ź', 'ż'],
}

uppercaseConsonantsDictionary = {
	'C': ['C', 'Ć'],
	'D': ['D'],
	'L': ['L', 'Ł'],
	'N': ['N', 'Ń'],
	'S': ['S', 'Ś'],
	'W': ['W'],
	'Y': ['Y'],
	'Z': ['Z', 'Ź', 'Ż'],
}

#Bulding block functions

def getRandomLetter(dictionary):
	#Selects a random element from a random list in the dictionary
	dictionaryKeys = list(dictionary.keys())
	randomKey = random.choice(dictionaryKeys)
	optionsList = dictionary[randomKey]
	randomLetter = random.choice(optionsList)
	return randomLetter

#Words are generated with (length - 1) consonants and 1 vowel
def generateUppercaseWord(length):
	#Exact same formula as for a lowercase word but starting with a
	#uppercase consonant and a special case for vowelPostion == 0
	currentWord = [getRandomLetter(uppercaseConsonantsDictionary)]
	for newLetter in range(length - 1):
		currentWord.append(getRandomLetter(lowercaseConsonantsDictionary))
	vowelPosition = random.randrange(length)
	if vowelPosition == 0:
		currentWord[0] = getRandomLetter(uppercaseVowelsDictionary)
	else:
		currentWord[vowelPosition] = getRandomLetter(lowercaseVowelsDictionary)
	return ''.join(currentWord)

def generateLowercaseWord(length):
	currentWord = []
	for newLetter in range(length):
		currentWord.append(getRandomLetter(lowercaseConsonantsDictionary))
	vowelPosition = random.randrange(length)
	currentWord[vowelPosition] = getRandomLetter(lowercaseVowelsDictionary)
	return ''.join(currentWord)

def generateSentence(numOfWords, maxWordLength):
	#Sentences are 1 uppercase word followed by (numOfWords - 1) lowercase words
	wordLength = random.randint(3, maxWordLength)
	currentSentence = generateUppercaseWord(wordLength)
	for newWord in range(numOfWords - 1):
		wordLength = random.randint(3, maxWordLength)
		currentSentence += ' ' + generateLowercaseWord(wordLength)
	currentSentence += '.'
	return currentSentence

def generateParagraph(numOfWords, maxWordLength, maxSentenceLength):
	#Sentence lengths are subtracted from the paragraph length 
	#And stored in sentenceLengthList until the remaining paragraph
	#length can be fitted into one sentence
	sentenceLengthList = [numOfWords]
	while (maxSentenceLength < sentenceLengthList[-1]):
		newSentenceLength = random.randint(3, maxSentenceLength)
		sentenceLengthList.append(sentenceLengthList[-1] - newSentenceLength)
		sentenceLengthList[-2] = newSentenceLength
	currentParagraph = generateSentence(sentenceLengthList[0], maxWordLength)
	sentenceLengthList.pop(0)
	for sentenceLength in sentenceLengthList:
		currentParagraph += " " + generateSentence(sentenceLength, maxWordLength)
	return currentParagraph

#Page generation

def generatePTGPage(request):
	if request.method == 'POST':
		length = int(request.POST.get('length'))
		complexity = request.POST.get('complexity')
		if (complexity == '1'):
			maxWordLength = 6
			maxSentenceLength = 6
		elif (complexity == '2'):
			maxWordLength = 10
			maxSentenceLength = 10
		else:
			maxWordLength = 15
			maxSentenceLength = 15
		return JsonResponse({'paragraph': generateParagraph(length, maxWordLength, maxSentenceLength)})
	else:
		context = {}
		return render(request, 'PolishTextGeneratorHTML.html', context)