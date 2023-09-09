# ---------------------------------------------
# W2T/apps.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------
#
# No special configuration for W2T is needed.
#

#Django imports

from django.apps import AppConfig

#App configuration

class W2TConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'W2T'