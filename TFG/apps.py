# ---------------------------------------------
# TFG/apps.py
# Derek Stephens
# 2023 September 9
# ---------------------------------------------
#
# No special configuration for TFG is needed.
#

#Django imports

from django.apps import AppConfig

#App configuration

class TfgConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TFG'