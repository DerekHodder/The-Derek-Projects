# ---------------------------------------------
# TFG/views.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------

#Django imports

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

#Python imports

import random

#Expansion functions

def notIfy(prompt):
	index = 0
	while index < len(prompt):
		#50% chance of replacing any given 'True' with 'Not False'
		#or 'False' with 'Not True'
		if (random.randint(0, 1) == 1):
			#List length increases, so index must be incremented twice
			if (prompt[index] == 'True'):
				prompt[index:index + 1] = ['Not', 'False']
				index += 1
			elif (prompt[index] == 'False'):
				prompt[index:index + 1] = ['Not', 'True']
				index += 1
		index += 1
	return prompt

#Replaces a random 'True' with an equivalent 'and' statement
#or a random 'False' with an equivalent 'and' statement
def andIfy(prompt):
	promptLength = len(prompt)
	#'True' or 'False' can only exist in even indeces in the list
	randomIndex = random.randrange(0, promptLength, 2)
	if prompt[randomIndex] == 'True':
		prompt[randomIndex:randomIndex + 1] = random.choice([
			['True', 'And', 'True']])
	else:
		prompt[randomIndex:randomIndex + 1] = random.choice([
			['True', 'And', 'False'],
			['False', 'And', 'True'],
			['False', 'And', 'False']])
	return prompt

#Replaces a random 'True' with an equivalent 'or' statement
#or a random 'False' with an equivalent 'or' statement
def orIfy(prompt):
	promptLength = len(prompt)
	#'True' or 'False' can only exist in even indeces in the list
	randomIndex = random.randrange(0, promptLength, 2)
	if prompt[randomIndex] == 'True':
		prompt[randomIndex:randomIndex + 1] = random.choice([
			['True', 'Or', 'True'],
			['True', 'Or', 'False'],
			['False', 'Or', 'True']])
	else:
		prompt[randomIndex:randomIndex + 1] = random.choice([
			['False', 'Or', 'False']
		])
	return prompt

#Overall prompt functions

def generateNormalPrompt(answer):
	currentPrompt = [answer]
	for i in range(2):
		currentPrompt = orIfy(currentPrompt)
	for i in range(2):
		currentPrompt = andIfy(currentPrompt)
	currentPrompt = ' '.join(currentPrompt)
	return currentPrompt

def generateChallengePrompt(answer):
	currentPrompt = [answer]
	for i in range(3):
		currentPrompt = orIfy(currentPrompt)
	for i in range(3):
		currentPrompt = andIfy(currentPrompt)
	currentPrompt = notIfy(currentPrompt)
	currentPrompt = ' '.join(currentPrompt)
	return currentPrompt

#Page generation

def generateTrueFalsePage(request):
	if request.method == 'POST':
		mode = request.POST.get('mode')
		answer = random.choice(['True', 'False'])
		if mode == 'normal':
			prompt = generateNormalPrompt(answer)
		else:
			prompt = generateChallengePrompt(answer)
		return JsonResponse({'answer': answer, 'prompt': prompt})
	else:
		context = {}
		return render(request, 'TrueFalseGameHTML.html', context)