# gameoflife/urls.py
from django.urls import path
from .views import game_of_life

urlpatterns = [
    path('', game_of_life, name='game_of_life'),
]
