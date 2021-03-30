from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView

from tenMans.models import Game, Player, Lane

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

def overallWinrateBarChart(request):
    labels, overallData, topData, jungData, midData, botData, suppData = ([] for i in range(7))
    queryset = Player.objects.order_by('playerName')

    for player in queryset:
        labels.append(player.playerName)
        overallData.append(player.getWinrate(None))
        topData.append(player.getWinrate(Lane.objects.get(laneName__exact="Top")))
        jungData.append(player.getWinrate(Lane.objects.get(laneName__exact="Jungle")))
        midData.append(player.getWinrate(Lane.objects.get(laneName__exact="Mid")))
        botData.append(player.getWinrate(Lane.objects.get(laneName__exact="Bot")))
        suppData.append(player.getWinrate(Lane.objects.get(laneName__exact="Support")))

    return JsonResponse(data={
        'labels': labels,
        'overall': overallData,
        'top': topData,
        'jungle': jungData,
        'mid': midData,
        'bot': botData,
        'support': suppData
    })
