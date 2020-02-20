"""
Defines the URLs for the blog module.
"""

# pylint: disable-msg=C0103

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.view, name='view'),
    path('post/<slug:slug>/comment', views.comment, name='comment')
]
