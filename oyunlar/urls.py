from django.urls import path
from oyunlar.views import *

urlpatterns = [
    path('', index, name="index"),
    path('details/<int:gameId>/', games, name='details'),
    path('add/', addGames, name='addgames'),
    path('comments/<int:game_id>/', game_comments, name='comments'),
    path('create_comment/<int:game_id>/', create_comment, name='create_comment')
]