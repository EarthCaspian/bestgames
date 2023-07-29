from django.shortcuts import get_object_or_404
from .models import Game

def user_game_count(request):
    if request.user.is_authenticated:
        user = request.user
        count = Game.objects.filter(user=user).count()
    else:
        count = 0
    return {'user_game_count': count}