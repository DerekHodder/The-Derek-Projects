# ---------------------------------------------
# Home/views.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------
#
# The Home app only contains links to other pages.
# For that reason, no views are needed.
#

#Django imports

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

#Page generation

def generateHomePage(request):
	context = {}
	return render(request, 'HomePageHTML.html', context)

def generateWilfredPage(request):
	context = {}
	return render(request, 'Wilfred.html', context)