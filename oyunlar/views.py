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
    context = {
        'gameItem':mygame
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

@login_required
def user_game_count(request):
    user = request.user
    count = Game.objects.filter(user=user).count()
    return JsonResponse({'count':count})