from django.urls import path
from oyunlar.views import *

urlpatterns = [
    path('', index, name="index"),
    path('details/<int:gameId>/', games, name='details'),
    path('add/', addGames, name='addgames')
]