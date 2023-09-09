# ---------------------------------------------
# TFG/urls.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------

#Django imports

from django.urls import path
from . import views

#Url path

urlpatterns = [
    path('', views.generateTrueFalsePage),
]