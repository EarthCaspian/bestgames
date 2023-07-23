from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    oyunlar = Game.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        oyunlar = Game.objects.filter(
            Q(oyunIsim__icontains = search) |
            Q(oyunPlatformu__platform__icontains = search) |
            Q(oyunTuru__tur__icontains = search)
        )
    game_count = Game.objects.count()

    for oyun in oyunlar:
        if len(oyun.oyunAciklama) > 300:
            oyun.oyunAciklama = oyun.oyunAciklama[:300] + '...'

    context = {
        'oyunlar':oyunlar,
        'search':search,
        'game_count':game_count
    }
    return render(request, 'index.html', context)

def games(request, gameId):
    mygame = Game.objects.get(id = gameId)
    comments = Comment.objects.filter(commentedGame=mygame)
    context = {
        'gameItem':mygame,
        'comments':comments
    }
    return render(request, 'detail.html', context)

def addGames(request):
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'add.html', context)

def game_count(request):
    count = Game.objects.count()
    response = JsonResponse({'count':count})

    print(response)

    return response

def game_comments(request, gameId):
    game = Game.objects.get(id=gameId)
    comments = Comment.objects.filter(commentedGame=game)
    context = {
        'game': game,
        'comments': comments,
    }
    return render(request, 'comments.html', context)

def create_comment(request, gameId):
    if request.method == 'POST':
        content = request.POST['content']
        commenter = request.user
        game = Game.objects.get(id=gameId)

        comment = Comment(content=content, commenter=commenter, commentedGame=game)
        comment.save()

        return redirect('details', gameId=gameId)
    context = {
        'gameId': gameId,
    }
    return render(request, 'create_comment.html',context)

def all_comments(request):
    comments = Comment.objects.all()
    context = {
        'comments':comments
    }
    return render(request, 'all_comments.html',context)

@login_required
def user_game_count(request):
    user = request.user
    count = Game.objects.filter(user=user).count()
    return JsonResponse({'count':count})

def user_games(request):
    user = request.user
    userGames = Game.objects.filter(user=user)
    context = {
        'userGames':userGames
    }
    return render(request, 'user_games.html', context)