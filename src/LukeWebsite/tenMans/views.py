from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView

from tenMans.models import Game, Player, Lane

class Dashboard(TemplateView):
    template_name = "tenMans/index.html"
    def get_context_data(self,*args, **kwargs):
        context = super(Dashboard, self).get_context_data(*args,**kwargs)
        context['player_list'] = Player.objects.all().order_by('playerName')
        return context

def overallWinrateBarChart(request):
    labels, overallData, topData, jungData, midData, botData, suppData, overallAlpha, topAlpha, jungAlpha, midAlpha, botAlpha, suppAlpha = ([] for i in range(13))
    queryset = Player.objects.order_by('playerName')

    for player in queryset:
        labels.append(player.playerName)

        overallData.append(player.getWinrate(None))
        topData.append(player.getWinrate(Lane.objects.get(laneName__exact="Top")))
        jungData.append(player.getWinrate(Lane.objects.get(laneName__exact="Jungle")))
        midData.append(player.getWinrate(Lane.objects.get(laneName__exact="Mid")))
        botData.append(player.getWinrate(Lane.objects.get(laneName__exact="Bot")))
        suppData.append(player.getWinrate(Lane.objects.get(laneName__exact="Support")))

        overallAlpha.append(player.getLaneRate(None))
        topAlpha.append(player.getLaneRate(Lane.objects.get(laneName__exact="Top")))
        jungAlpha.append(player.getLaneRate(Lane.objects.get(laneName__exact="Jungle")))
        midAlpha.append(player.getLaneRate(Lane.objects.get(laneName__exact="Mid")))
        botAlpha.append(player.getLaneRate(Lane.objects.get(laneName__exact="Bot")))
        suppAlpha.append(player.getLaneRate(Lane.objects.get(laneName__exact="Support")))


    return JsonResponse(data={
        'labels': labels,
        'overall': overallData,
        'top': topData,
        'jungle': jungData,
        'mid': midData,
        'bot': botData,
        'support': suppData,
        'overallAlpha': overallAlpha,
        'topAlpha': topAlpha,
        'jungleAlpha': jungAlpha,
        'midAlpha': midAlpha,
        'botAlpha': botAlpha,
        'supportAlpha': suppAlpha
    })
def overallPlaytimeBarChart(request):
    labels, overallData, topData, jungData, midData, botData, suppData = ([] for i in range(7))
    queryset = Player.objects.order_by('playerName')

    for player in queryset:
        labels.append(player.playerName)

        overallData.append(player.getLaneCount(None))
        topData.append(player.getLaneCount(Lane.objects.get(laneName__exact="Top")))
        jungData.append(player.getLaneCount(Lane.objects.get(laneName__exact="Jungle")))
        midData.append(player.getLaneCount(Lane.objects.get(laneName__exact="Mid")))
        botData.append(player.getLaneCount(Lane.objects.get(laneName__exact="Bot")))
        suppData.append(player.getLaneCount(Lane.objects.get(laneName__exact="Support")))


    return JsonResponse(data={
        'labels': labels,
        'overall': overallData,
        'top': topData,
        'jungle': jungData,
        'mid': midData,
        'bot': botData,
        'support': suppData,
        'max': Game.getTotalGames()
    })

def overallWinrateTable(request):
    data = []
    queryset = Player.objects.order_by('playerName')

    for player in queryset:
        playerDict = {}
        playerDict["name"] = player.playerName
        playerDict["overall"] = player.getWinrate(None)
        playerDict["top"] = player.getWinrate(Lane.objects.get(laneName__exact="Top"))
        playerDict["jungle"] = player.getWinrate(Lane.objects.get(laneName__exact="Jungle"))
        playerDict["mid"] = player.getWinrate(Lane.objects.get(laneName__exact="Mid"))
        playerDict["bot"] = player.getWinrate(Lane.objects.get(laneName__exact="Bot"))
        playerDict["supp"] = player.getWinrate(Lane.objects.get(laneName__exact="Support"))
        playerDict["overallAlpha"] = player.getLaneRate(None)
        playerDict["topAlpha"] = player.getLaneRate(Lane.objects.get(laneName__exact="Top"))
        playerDict["jungleAlpha"] = player.getLaneRate(Lane.objects.get(laneName__exact="Jungle"))
        playerDict["midAlpha"] = player.getLaneRate(Lane.objects.get(laneName__exact="Mid"))
        playerDict["botAlpha"] = player.getLaneRate(Lane.objects.get(laneName__exact="Bot"))
        playerDict["suppAlpha"] = player.getLaneRate(Lane.objects.get(laneName__exact="Support"))
        data.append(playerDict)

    return JsonResponse(data={
        'data': data
    })

def overallPlaytimeTable(request):
    data = []
    queryset = Player.objects.order_by('playerName')

    for player in queryset:
        playerDict = {}
        playerDict["name"] = player.playerName
        playerDict["overall"] = player.getLaneCount(None)
        playerDict["top"] = player.getLaneCount(Lane.objects.get(laneName__exact="Top"))
        playerDict["jungle"] = player.getLaneCount(Lane.objects.get(laneName__exact="Jungle"))
        playerDict["mid"] = player.getLaneCount(Lane.objects.get(laneName__exact="Mid"))
        playerDict["bot"] = player.getLaneCount(Lane.objects.get(laneName__exact="Bot"))
        playerDict["supp"] = player.getLaneCount(Lane.objects.get(laneName__exact="Support"))
        data.append(playerDict)

    return JsonResponse(data={
        'data': data
    })
