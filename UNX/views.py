# ---------------------------------------------
# UNX/views.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------

#Django imports

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

#Python imports

import math

#Property functions

def isOdd(num):
	return num % 2 == 1

def isSquare(num):
	return math.sqrt(num).is_integer()

def isCube(num):
	return math.cbrt(num).is_integer()

def isTriangleNumber(num):
	return isSquare(8 * num + 1)

def isPowerOf2(num):
	return math.log(num, 2).is_integer()

def isPowerOf10(num):
	return math.log(num, 10).is_integer()

def isPrime(num):
	for i in range(2, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

def isFibonacciNumber(num):
	#Neat!
	#Does an equivalent formula exist for other Lucas Sequences?
	return isSquare(5 * num ** 2 + 4) or isSquare(5 * num ** 2 - 4)

def isFactorial(num):
	product = 1
	multiplier = 1
	while product < num:
		product *= multiplier
		multiplier += 1
	return num == product

def isPerfectNumber(num):
	sum = 1
	for i in range(2, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			sum += i
			if i ** 2 != num:
				sum += num / i
	return sum == num

def isFermatNumber(num):
	return math.log(math.log(num - 1, 2), 2).is_integer()

def isArithmeticNumber(num):
	sum = 0
	divisors = 0
	for i in range(1, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			sum += i
			divisors += 1
			if i ** 2 != num:
				sum += num / i
				divisors += 1
	return (sum / divisors).is_integer()

def isWoodallNumber(num):
	i = 1
	result = 1
	while result < num:
		i += 1
		result = i * 2 ** i - 1
	return num == result

def isPellNumber(num):
	n0 = 0
	n1 = 1
	n2 = 2
	while n2 < num:
		n0 = n1
		n1 = n2
		n2 = n0 + 2 * n1
	return n2 == num

def isPronicNumber(num):
	return (math.sqrt(num + 1 /4) - 1 / 2).is_integer()

def isCarolNumber(num):
	return math.log((math.sqrt(num + 2) + 1), 2).is_integer()

def isPoliteNumber(num):
	#Neat!
	return not isPowerOf2(num)

def isSquareFreeNumber(num):
	for i in range(2, math.floor(math.sqrt(num)) + 1):
		if num % (i ** 2) == 0:
			return False
	return True

def isPowerfulNumber(num):
	if isPrime(num):
		return False
	for i in range(2, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			if isPrime(i):
				if num % (i ** 2) != 0:
					return False
			if isPrime(num / i):
				if num % ((num / i) ** 2) != 0:
					return False
	return True

def isLucasNumber(num):
	n0 = 2
	n1 = 1
	n2 = 3
	while n2 < num:
		n0 = n1
		n1 = n2
		n2 = n0 + n1
	return n2 == num

#Page generation

def generateUNXPage(request):
	if request.method == 'POST':
		time = int(request.POST.get('time'))
		return JsonResponse(getCategories(time))
	else:
		context = {}	
		return render(request, 'UnixTimeHTML.html', context)

#Dictionary creation

def getCategories(num):
	returnDictionary = {}
	if isOdd(num):
		returnDictionary['Odd'] = 'green'
	else:
		returnDictionary['Even'] = 'red'
	if isSquare(num):
		returnDictionary['a Square'] = 'green'
	else:
		returnDictionary['not a Square'] = 'red'
	if isCube(num):
		returnDictionary['a Cube'] = 'green'
	else:
		returnDictionary['not a Cube'] = 'red'
	if isTriangleNumber(num):
		returnDictionary['a Triangle Number'] = 'green'
	else:
		returnDictionary['not a Triangle Number'] = 'red'
	if isPowerOf2(num):
		returnDictionary['a Power Of 2'] = 'green'
	else:
		returnDictionary['not a Power Of 2'] = 'red'
	if isPowerOf10(num):
		returnDictionary['a Power Of 10'] = 'green'
	else:
		returnDictionary['not a Power Of 10'] = 'red'
	if isPrime(num):
		returnDictionary['Prime'] = 'green'
	else:
		returnDictionary['Composite'] = 'red'
	if isFibonacciNumber(num):
		returnDictionary['a Fibonacci Number'] = 'green'
	else:
		returnDictionary['not a Fibonacci Number'] = 'red'
	if isFactorial(num):
		returnDictionary['a Factorial'] = 'green'
	else:
		returnDictionary['not a Factorial'] = 'red'
	if isPerfectNumber(num):
		returnDictionary['a Perfect Number'] = 'green'
	else:
		returnDictionary['not a Perfect Number'] = 'red'
	if isFermatNumber(num):
		returnDictionary['a Fermat Number'] = 'green'
	else:
		returnDictionary['not a Fermat Number'] = 'red'
	if isArithmeticNumber(num):
		returnDictionary['an Arithmetic Number'] = 'green'
	else:
		returnDictionary['not an Arithmetic Number'] = 'red'
	if isWoodallNumber(num):
		returnDictionary['a Woodall Number'] = 'green'
	else:
		returnDictionary['not a Woodall Number'] = 'red'
	if isPellNumber(num):
		returnDictionary['a Pell Number'] = 'green'
	else:
		returnDictionary['not a Pell Number'] = 'red'
	if isPronicNumber(num):
		returnDictionary['a Pronic Number'] = 'green'
	else:
		returnDictionary['not a Pronic Number'] = 'red'
	if isCarolNumber(num):
		returnDictionary['a Carol Number'] = 'green'
	else:
		returnDictionary['not a Carol Number'] = 'red'
	if isPoliteNumber(num):
		returnDictionary['a Polite Number'] = 'green'
	else:
		returnDictionary['an Impolite Number'] = 'red'
	if isSquareFreeNumber(num):
		returnDictionary['a Squarefree Number'] = 'green'
	else:
		returnDictionary['not a Squarefree Number'] = 'red'
	if isPowerfulNumber(num):
		returnDictionary['a Powerful Number'] = 'green'
	else:
		returnDictionary['not a Powerful Number'] = 'red'
	if isLucasNumber(num):
		returnDictionary['a Lucas Number'] = 'green'
	else:
		returnDictionary['not a Lucas Number'] = 'red'
	return returnDictionary