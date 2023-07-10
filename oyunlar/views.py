from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    oyunlar = Game.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        oyunlar = Game.objects.filter(
            Q(oyunIsim__icontains = search) |
            Q(oyunTuru__icontains = search) |
            Q(oyunCikisTarihi__icontains = search)
        )
    context = {
        'oyunlar':oyunlar,
        'search':search
    }
    return render(request, 'index.html', context)

def games(request, gameId):
    mygame = Game.objects.get(id = gameId)
    context = {
        'game':mygame
    }
    return render(request, 'detail.html', context)

