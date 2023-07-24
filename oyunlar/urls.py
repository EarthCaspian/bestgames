from django.urls import path
from oyunlar.views import *

urlpatterns = [
    path('', index, name="index"),
    path('details/<int:gameId>/', games, name='details'),
    path('add/', addGames, name='addgames'),
    path('comments/<int:gameId>/', game_comments, name='comments'),
    path('create_comment/<int:gameId>/', create_comment, name='create_comment'),
    path('all_comments', all_comments, name='all_comments'),
    path('user_games/', user_games, name='user_games'),
    path('upvote/<int:gameId>/', upvote_game, name='upvote_game')
]