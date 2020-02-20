"""
Defines the URLs for the social module.
"""

# pylint: disable-msg=C0103

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='profile')
]
