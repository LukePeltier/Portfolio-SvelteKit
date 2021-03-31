from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views import View
from django.views.generic.base import (ContextMixin, TemplateResponseMixin,
                                       TemplateView)
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView

from tenMans.forms import NewGameForm
from tenMans.models import Game, Lane, Player


class BaseTenMansContextMixin(ContextMixin):
    def get_context_data(self,*args, **kwargs):
        context = super(BaseTenMansContextMixin, self).get_context_data(*args,**kwargs)
        context['player_list'] = Player.objects.all().order_by('playerName')
        return context
class Dashboard(TemplateView, BaseTenMansContextMixin):
    template_name = "tenMans/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

class PlayerDetailView(DetailView, BaseTenMansContextMixin):
    model = Player

class PlayerWinrateOverTimeView(DetailView):
    model = Player
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        labels, overallData, topData, jungData, midData, botData, suppData = ([] for i in range(7))
        games = Game.objects.all().order_by('gameNumber')
        for game in games:
            labels.append(game.gameNumber)
            overallData.append(self.object.getWinrateHistorical(game, None))
            topData.append(self.object.getWinrateHistorical(game, Lane.objects.get(laneName__exact="Top")))
            jungData.append(self.object.getWinrateHistorical(game, Lane.objects.get(laneName__exact="Jungle")))
            midData.append(self.object.getWinrateHistorical(game, Lane.objects.get(laneName__exact="Mid")))
            botData.append(self.object.getWinrateHistorical(game, Lane.objects.get(laneName__exact="Bot")))
            suppData.append(self.object.getWinrateHistorical(game, Lane.objects.get(laneName__exact="Support")))
        return JsonResponse(data={
        'labels': labels,
        'overall': overallData,
        'top': topData,
        'jungle': jungData,
        'mid': midData,
        'bot': botData,
        'support': suppData
    })

class NewGameView(FormView):
    template_name = 'tenMans/new_game.html'
    form_class = NewGameForm
    success_url = '/game_submitted/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.submit_game()
        return super().form_valid(form)
