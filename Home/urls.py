# ---------------------------------------------
# Home/urls.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------
#
# An empty url path redirects to this file.
# DerekProjects/urls.py may be updated sometime in the future to circumvent this file entirely.
#

#Django imports

from django.urls import path
from . import views

#Url path

urlpatterns = [
	path('', views.generateHomePage),
]