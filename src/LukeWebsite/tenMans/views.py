from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from tenMans.models import Game, Player

# Create your views here.

# Create your views here.
def index(request):
    gameCount = Game.objects.count()
    playerCount = Player.objects.count()
    context = {
        'gameCount': gameCount,
        'playerCount': playerCount
    }
    return render(request, 'tenMans/index.html', context)
