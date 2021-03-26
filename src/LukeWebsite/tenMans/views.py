from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView

from tenMans.models import Game, Player

class Dashboard(TemplateView):
    template_name = "tenMans/index.html"
    gameCount = Game.objects.count()
    playerCount = Player.objects.count()
    extra_context = {
        'gameCount': gameCount,
        'playerCount': playerCount
    }
    def get_context_data(self,*args, **kwargs):
        context = super(Dashboard, self).get_context_data(*args,**kwargs)
        context['player_list'] = Player.objects.all()
        return context
