# ---------------------------------------------
# W2T/views.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------

#Django imports

from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

#Python imports

import math

#Postgres fetch function

def getWordVector(word):
	cursor = connection.cursor()
	cursor.execute('SELECT nums FROM w2v_values WHERE word = %s', [word])
	result = cursor.fetchone()
	cursor.close()
	if result == None:
		return False
	else:
		return result[0]

#Vector functions

def dotProduct(vector1, vector2):
	sum = 0
	for index in range(len(vector1)):
		sum += vector1[index] * vector2[index]
	return sum

def length(vector):
	return math.sqrt(dotProduct(vector, vector))

def cosineSimilarity(vector1, vector2):
	return (dotProduct(vector1, vector2) / (length(vector1) * length(vector2)))

#'Food' functions

def PercentifyAmounts(amountsDictionary):
	sum = 0
	for ingredient in amountsDictionary:
		sum += amountsDictionary[ingredient]
	newDictionary = {}
	for ingredient in amountsDictionary:
		newDictionary[ingredient] = round(amountsDictionary[ingredient] * 100 / sum, 2)
	return newDictionary

def subtractOut(targetVector, scalableVector):
	#Calculate orthogonal projection and subtract that from the original vector
	#Result must be closer to the origin than the original vector
	scalarCoefficient = dotProduct(targetVector, scalableVector) / dotProduct (scalableVector, scalableVector)
	orthogonalProjection = []
	for num in scalableVector:
		orthogonalProjection.append(scalarCoefficient * num)
	newVector = []
	for index in range(len(targetVector)):
		newVector.append(targetVector[index] - orthogonalProjection[index])
	return newVector

def findClosestIngredient(vector, ingredients):
	if len(ingredients) == 0:
		return False
	closestIngredient = ingredients[0]
	greatestCosineSimilarity = cosineSimilarity(vector, ingredientsReference[closestIngredient])
	#The ingredient vector with the greatest cosine similarity is the closest to the target vector
	for ingredient in ingredients:
		currentCosineSimilarity = cosineSimilarity(vector, ingredientsReference[ingredient])
		if greatestCosineSimilarity < currentCosineSimilarity:
			closestIngredient = ingredient
			greatestCosineSimilarity = currentCosineSimilarity
	#Only return an ingredient that will actually make progress
	if greatestCosineSimilarity <= 0:
		return False
	else:
		return closestIngredient

def convertVectorToIngredients(givenVector):
	currentVector = givenVector[:]
	currentIngredients = list(ingredientsReference.keys())
	ingredientsAmounts = {}
	closestIngredient = findClosestIngredient(currentVector, currentIngredients)
	#Subtract out scaled ingredient vectors until no more progress can be made
	while closestIngredient != False:
		closestIngredientVector = ingredientsReference[closestIngredient]
		amountOfIngredient = dotProduct(currentVector, closestIngredientVector) / dotProduct(closestIngredientVector, closestIngredientVector)
		currentVector = subtractOut(currentVector, closestIngredientVector)
		ingredientsAmounts[closestIngredient] = amountOfIngredient
		currentIngredients.remove(closestIngredient)
		closestIngredient = findClosestIngredient(currentVector, currentIngredients)
	return PercentifyAmounts(ingredientsAmounts)

#Calculator initialization

ingredientsFile = open("W2T/ingredientslist.txt")
ingredientsReference = {}
for line in ingredientsFile:
	newIngredient = line.strip()
	queryResult = getWordVector(newIngredient.replace(' ', '_'))
	if queryResult != False:
		ingredientsReference[newIngredient] = queryResult
ingredientsFile.close()

#Page generation

def generateW2TPage(request):
	if request.method == 'POST':
		targetWord = request.POST.get('word')
		#Normal algorithm breaks when the input word is itself an ingredient???
		if targetWord in ingredientsReference:
			return JsonResponse({targetWord : 100})
		targetVector = getWordVector(targetWord.replace(' ', '_'))
		if targetVector == False:
			return JsonResponse({})
		else:
			return JsonResponse(convertVectorToIngredients(targetVector))
	else:
		context = {}	
		return render(request, 'Word2TasteHTML.html', context)