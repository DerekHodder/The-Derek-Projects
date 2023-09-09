# ---------------------------------------------
# WAR/views.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------
#
# War exists only in JS because making calls to the server
# for every single battle is just unnecessary.
# So, no views are needed.
#

#Django imports

from django.shortcuts import render

#Page generation

def generateWARPage(request):
	if request.method == 'POST':
		pass
	else:
		context = {}	
		return render(request, 'WarHTML.html', context)