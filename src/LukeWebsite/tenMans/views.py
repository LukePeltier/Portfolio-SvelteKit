from django.contrib.auth import authenticate
from django.db import transaction
from django.db.utils import Error, IntegrityError
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views import View
from django.views.generic.base import (ContextMixin,
                                       TemplateView)
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from tenMans.forms import CreatePlayer, NewGameForm, UpdateAllGamesForm, UpdateGameForm
from tenMans.models import Champion, Game, GameLaner, GameLanerStats, Lane, Player
import datetime
import os
from configparser import ConfigParser
from riotwatcher import LolWatcher

class BaseTenMansContextMixin(ContextMixin):
    def get_context_data(self,*args, **kwargs):
        context = super(BaseTenMansContextMixin, self).get_context_data(*args,**kwargs)
        context['player_list'] = Player.objects.all().order_by('playerName')
        return context
class Dashboard(TemplateView, BaseTenMansContextMixin):
    template_name = "tenMans/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gameTotal'] = Game.objects.all().count()
        context['memeTotal'] = Game.objects.all().filter(gameMemeStatus=True).count()
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
        playerDict["playerID"] = player.id
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
        playerDict["playerID"] = player.id
        data.append(playerDict)

    return JsonResponse(data={
        'data': data
    })

class PlayerDetailView(DetailView, BaseTenMansContextMixin):
    model = Player
    object: Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mostPlayedLane'] = self.object.getMostPlayedLaneString()
        context['mostPlayedChamp'] = self.object.getMostPlayedChampionString()
        context['highestWinrateChamp'] = self.object.getHighestWinrateChampionString()
        context['averageBansPulled'] = self.object.getAveragePulledBans()
        context['mostBannedChamp'] = self.object.getMostBannedChampionString()
        context['totalGamesPlayed'] = self.object.getLaneCount(None)
        context['blueSideWinrate'] = self.object.getSideWinrate("Blue")
        context['redSideWinrate'] = self.object.getSideWinrate("Red")
        context['overallAverageKDA'] = self.object.getAverageKDALaneString(None)
        context['uniqueChampionsPlayed'] = self.object.getUniqueChampionCount()
        return context

class PlayerWinrateOverTimeView(DetailView):
    model = Player
    object: Player
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

class PlayerLaneCountTable(DetailView):
    model = Player
    object: Player
    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        queryset = Lane.objects.all()
        for lane in queryset:
            laneDict = {}
            laneDict["lane"] = lane.laneName
            laneDict["playCount"] = self.object.getLaneCount(lane)
            laneDict["averageKDA"] = self.object.getAverageKDALaneString(lane)
            data.append(laneDict)

        return JsonResponse(data={
            'data': data
        })

class PlayerChampionCountTable(DetailView):
    model = Player
    object: Player
    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        queryset = Champion.objects.all()
        champsPlayed = self.object.championsPlayed()
        config_object = ConfigParser()
        config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
        apiKey = config_object['general']['RIOT_API_KEY']

        lolWatcher = LolWatcher(apiKey)
        region = 'na1'
        versionNumber = lolWatcher.data_dragon.versions_for_region(region)['n']['champion']
        for champ in queryset:
            champDict = {}
            champDict["name"] = champ.championName
            if champ.championName not in champsPlayed:
                continue
            else:
                champDict["playCount"] = champsPlayed[champ.championName]
                champDict["winrate"] = self.object.getWinrateOnChampion(champ)
                champDict["averageKDA"] = self.object.getAverageKDAChampionString(champ)
                champDict['championID'] = champ.id
                champDict['riotChampionName'] = champ.riotName
                champDict['championVersion'] = versionNumber
            data.append(champDict)

        return JsonResponse(data={
            'data': data
        })

class PlayerGamesTable(DetailView):
    model = Player

    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Player
        gamesPlayed = GameLaner.objects.filter(player__exact=self.object.id)
        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)
        config_object = ConfigParser()
        config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
        apiKey = config_object['general']['RIOT_API_KEY']

        lolWatcher = LolWatcher(apiKey)
        region = 'na1'
        versionNumber = lolWatcher.data_dragon.versions_for_region(region)['n']['champion']
        for stat in stats:
            stat: GameLanerStats
            statDict = {}
            statDict['gameNum'] = stat.gameLaner.game.gameNumber
            if stat.gameLaner.blueTeam:
                teamString = "Blue"
                if stat.gameLaner.game.gameBlueWins:
                    win = "W"
                else:
                    win = "L"
            else:
                teamString = "Red"
                if not stat.gameLaner.game.gameBlueWins:
                    win = "W"
                else:
                    win = "L"
            statDict['team'] = teamString
            statDict['champion'] = stat.gameLaner.champion.championName
            statDict['lane'] = stat.gameLaner.lane.laneName
            statDict['winLoss'] = win
            statDict['duration'] = stat.gameLaner.game.gameDuration
            statDict['kills'] = stat.kills
            statDict['deaths'] = stat.deaths
            statDict['assists'] = stat.assists
            statDict['largestKillingSpree'] = stat.largestKillingSpree
            statDict['largestMultiKill'] = stat.largestMultiKill
            statDict['doubleKills'] = stat.doubleKills
            statDict['tripleKills'] = stat.tripleKills
            statDict['quadraKills'] = stat.quadraKills
            statDict['pentaKills'] = stat.pentaKills
            statDict['totalDamageDealtToChampions'] = stat.totalDamageDealtToChampions
            statDict['visionScore'] = stat.visionScore
            statDict['crowdControlScore'] = stat.crowdControlScore
            statDict['totalDamageTaken'] = stat.totalDamageTaken
            statDict['goldEarned'] = stat.goldEarned
            statDict['turretKills'] = stat.turretKills
            statDict['inhibitorKills'] = stat.inhibitorKills
            statDict['cs'] = stat.laneMinionsKilled + stat.neutralMinionsKilled
            statDict['teamJungleMinionsKilled'] = stat.teamJungleMinionsKilled
            statDict['enemyJungleMinionsKilled'] = stat.enemyJungleMinionsKilled
            statDict['controlWardsPurchased'] = stat.controlWardsPurchased
            statDict['firstBlood'] = stat.firstBlood
            statDict['firstTower'] = stat.firstTower
            statDict['csRateFirstTen'] = stat.csRateFirstTen
            statDict['csRateSecondTen'] = (stat.csRateSecondTen + stat.csRateFirstTen)/2
            statDict['gameID'] = stat.gameLaner.game.id
            statDict['championID'] = stat.gameLaner.champion.id
            statDict['riotChampionName'] = stat.gameLaner.champion.riotName
            statDict['championVersion'] = versionNumber

            data.append(statDict)

        return JsonResponse(
            data={
                'data':data
            }
        )
class PlayerDraftStats(TemplateView, BaseTenMansContextMixin):
    template_name = 'tenMans/playerDraftStats.html'


class AverageDraftOrderTable(View):

    def get(self, request, *args, **kwargs):
        data = []
        queryset = Player.objects.all()

        for player in queryset:
            playerDict = {}
            playerDict["name"] = player.playerName
            playerDict["draftOrder"] = player.getAverageDraftOrder()
            if playerDict["draftOrder"] is None:
                continue
            playerDict["playerID"] = player.id
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })

class ExpectedDraftOrderWinrateTable(View):

    def get(self, request, *args, **kwargs):
        data = []
        queryset = Player.objects.all()

        for player in queryset:
            playerDict = {}
            playerDict["name"] = player.playerName
            playerDict["minWinrate"] = player.getMinConfidenceWinrate(None)
            if playerDict["minWinrate"] is None:
                continue
            playerDict["playerID"] = player.id
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })
class ExpectedDraftOrderWinrateLaneTable(View):

    def get(self, request, *args, **kwargs):
        data = []
        queryset = Player.objects.all()
        laneName = kwargs['lane']

        lane = Lane.objects.filter(laneName__exact=laneName).get()

        for player in queryset:
            playerDict = {}
            playerDict["name"] = player.playerName
            playerDict["minWinrate"] = player.getMinConfidenceWinrate(lane)
            if playerDict["minWinrate"] is None:
                continue
            playerDict["playerID"] = player.id
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })

class NewGameView(FormView, BaseTenMansContextMixin):
    template_name = 'tenMans/new_game.html'
    form_class = NewGameForm
    success_url = '/ten_mans/'

    @transaction.atomic
    def form_valid(self, form: NewGameForm):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        try:
            form.submit_game()
        except Error:
            return super().form_invalid(form)


        return super().form_valid(form)

class UpdateGameView(FormView, BaseTenMansContextMixin):
    template_name = 'tenMans/updateGame.html'
    form_class = UpdateGameForm
    success_url = '/ten_mans/'

    @transaction.atomic
    def form_valid(self, form: UpdateGameForm):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        try:
            form.updateGame()
        except Error:
            return super().form_invalid(form)

        return super().form_valid(form)



class UpdateAllGamesView(FormView, BaseTenMansContextMixin):
    template_name = 'tenMans/updateAllGames.html'
    form_class = UpdateAllGamesForm
    success_url = '/ten_mans/'

    @transaction.atomic
    def form_valid(self, form: UpdateAllGamesForm):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        try:
            form.updateGame()
        except Error:
            return super().form_invalid(form)

        return super().form_valid(form)


class GameListView(ListView, BaseTenMansContextMixin):
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GameDetailView(DetailView, BaseTenMansContextMixin):
    model = Game
    object: Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeString'] = str(datetime.timedelta(seconds=self.get_object().gameDuration))
        if self.get_object().gameBlueWins:
            blueTeamWinString = "Win"
            redTeamWinString = "Loss"
        else:
            blueTeamWinString = "Loss"
            redTeamWinString = "Win"
        context['blueTeamWinString'] = blueTeamWinString
        context['redTeamWinString'] = redTeamWinString

        if(self.get_object().gameMemeStatus):
            #get list of players involved
            players = GameLaner.objects.filter(game__exact=self.object.id)
            playerNames = []
            reasons = []
            for player in players:
                playerNames.append(player.player.playerName)
                reasons.append(player.champion.championName)
            context['players'] = ','.join(playerNames)
            context['reasons'] = ','.join(reasons)
        return context

class BlueTeamTable(DetailView):
    model= Game
    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Game
        gameLaners = GameLaner.objects.filter(game__exact=self.object.id, blueTeam__exact=True)
        stats = GameLanerStats.objects.filter(gameLaner__in=gameLaners)

        config_object = ConfigParser()
        config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
        apiKey = config_object['general']['RIOT_API_KEY']

        lolWatcher = LolWatcher(apiKey)
        region = 'na1'
        versionNumber = lolWatcher.data_dragon.versions_for_region(region)['n']['champion']

        for statLine in stats:
            playerDict = {}
            playerDict["playerName"] = statLine.gameLaner.player.playerName
            playerDict['champion'] = statLine.gameLaner.champion.championName
            playerDict['lane'] = statLine.gameLaner.lane.laneName
            playerDict['kills'] = statLine.kills
            playerDict['deaths'] = statLine.deaths
            playerDict['assists'] = statLine.assists
            playerDict['largestKillingSpree'] = statLine.largestKillingSpree
            playerDict['largestMultiKill'] = statLine.largestMultiKill
            playerDict['doubleKills'] = statLine.doubleKills
            playerDict['tripleKills'] = statLine.tripleKills
            playerDict['quadraKills'] = statLine.quadraKills
            playerDict['pentaKills'] = statLine.pentaKills
            playerDict['totalDamageDealtToChampions'] = statLine.totalDamageDealtToChampions
            playerDict['visionScore'] = statLine.visionScore
            playerDict['crowdControlScore'] = statLine.crowdControlScore
            playerDict['totalDamageTaken'] = statLine.totalDamageTaken
            playerDict['goldEarned'] = statLine.goldEarned
            playerDict['turretKills'] = statLine.turretKills
            playerDict['inhibitorKills'] = statLine.inhibitorKills
            playerDict['cs'] = statLine.laneMinionsKilled + statLine.neutralMinionsKilled
            playerDict['teamJungleMinionsKilled'] = statLine.teamJungleMinionsKilled
            playerDict['enemyJungleMinionsKilled'] = statLine.enemyJungleMinionsKilled
            playerDict['controlWardsPurchased'] = statLine.controlWardsPurchased
            playerDict['firstBlood'] = statLine.firstBlood
            playerDict['firstTower'] = statLine.firstTower
            playerDict['csRateFirstTen'] = statLine.csRateFirstTen
            playerDict['csRateSecondTen'] = (statLine.csRateSecondTen + statLine.csRateFirstTen)/2
            playerDict["draftOrder"] = statLine.gameLaner.getDraftString()
            playerDict['playerID'] = statLine.gameLaner.player.id
            playerDict['championID'] = statLine.gameLaner.champion.id
            playerDict['riotChampionName'] = statLine.gameLaner.champion.riotName
            playerDict['championVersion'] = versionNumber
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })

class RedTeamTable(DetailView):
    model= Game
    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Game
        gameLaners = GameLaner.objects.filter(game__exact=self.object.id, blueTeam__exact=False)
        stats = GameLanerStats.objects.filter(gameLaner__in=gameLaners)

        config_object = ConfigParser()
        config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
        apiKey = config_object['general']['RIOT_API_KEY']

        lolWatcher = LolWatcher(apiKey)
        region = 'na1'
        versionNumber = lolWatcher.data_dragon.versions_for_region(region)['n']['champion']

        for statLine in stats:
            playerDict = {}
            playerDict["playerName"] = statLine.gameLaner.player.playerName
            playerDict['champion'] = statLine.gameLaner.champion.championName
            playerDict['lane'] = statLine.gameLaner.lane.laneName
            playerDict['kills'] = statLine.kills
            playerDict['deaths'] = statLine.deaths
            playerDict['assists'] = statLine.assists
            playerDict['largestKillingSpree'] = statLine.largestKillingSpree
            playerDict['largestMultiKill'] = statLine.largestMultiKill
            playerDict['doubleKills'] = statLine.doubleKills
            playerDict['tripleKills'] = statLine.tripleKills
            playerDict['quadraKills'] = statLine.quadraKills
            playerDict['pentaKills'] = statLine.pentaKills
            playerDict['totalDamageDealtToChampions'] = statLine.totalDamageDealtToChampions
            playerDict['visionScore'] = statLine.visionScore
            playerDict['crowdControlScore'] = statLine.crowdControlScore
            playerDict['totalDamageTaken'] = statLine.totalDamageTaken
            playerDict['goldEarned'] = statLine.goldEarned
            playerDict['turretKills'] = statLine.turretKills
            playerDict['inhibitorKills'] = statLine.inhibitorKills
            playerDict['cs'] = statLine.laneMinionsKilled + statLine.neutralMinionsKilled
            playerDict['teamJungleMinionsKilled'] = statLine.teamJungleMinionsKilled
            playerDict['enemyJungleMinionsKilled'] = statLine.enemyJungleMinionsKilled
            playerDict['controlWardsPurchased'] = statLine.controlWardsPurchased
            playerDict['firstBlood'] = statLine.firstBlood
            playerDict['firstTower'] = statLine.firstTower
            playerDict['csRateFirstTen'] = statLine.csRateFirstTen
            playerDict['csRateSecondTen'] = (statLine.csRateSecondTen + statLine.csRateFirstTen)/2
            playerDict["draftOrder"] = statLine.gameLaner.getDraftString()
            playerDict['playerID'] = statLine.gameLaner.player.id
            playerDict['championID'] = statLine.gameLaner.champion.id
            playerDict['riotChampionName'] = statLine.gameLaner.champion.riotName
            playerDict['championVersion'] = versionNumber
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })

class ChampionListView(ListView, BaseTenMansContextMixin):
    model = Champion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config_object = ConfigParser()
        config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
        apiKey = config_object['general']['RIOT_API_KEY']

        lolWatcher = LolWatcher(apiKey)
        region = 'na1'
        context['naChampVersion'] = lolWatcher.data_dragon.versions_for_region(region)['n']['champion']

        return context

class ChampionDetailView(DetailView, BaseTenMansContextMixin):
    model = Champion
    object: Champion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config_object = ConfigParser()
        config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
        apiKey = config_object['general']['RIOT_API_KEY']

        lolWatcher = LolWatcher(apiKey)
        region = 'na1'
        context['naChampVersion'] = lolWatcher.data_dragon.versions_for_region(region)['n']['champion']
        context['mostPlayedLane'] = self.object.getMainLaneString()

        context['overallWinrate'] = self.object.getWinrate(None)
        context['blueSideWinrate'] = self.object.getSideWinrate("Blue")
        context['redSideWinrate'] = self.object.getSideWinrate("Red")
        context['pickRate'] = self.object.getPickRate()
        context['banRate'] = self.object.getBanRate()
        context['pickBanRate'] = round(context['pickRate'] + context['banRate'], 2)
        context['overallAverageKDA'] = self.object.getAverageKDALaneString(None)

        return context

class ChampionPlaytimeChartView(DetailView):
    model = Champion
    def get(self, request, *args, **kwargs):
        labels, overallData, topData, jungData, midData, botData, suppData = ([] for i in range(7))
        self.object = self.get_object()
        self.object: Champion

        labels.append("Overall")
        overallData.append(self.object.getLaneCount(None))
        topData.append(self.object.getLaneCount(Lane.objects.get(laneName__exact="Top")))
        jungData.append(self.object.getLaneCount(Lane.objects.get(laneName__exact="Jungle")))
        midData.append(self.object.getLaneCount(Lane.objects.get(laneName__exact="Mid")))
        botData.append(self.object.getLaneCount(Lane.objects.get(laneName__exact="Bot")))
        suppData.append(self.object.getLaneCount(Lane.objects.get(laneName__exact="Support")))


        return JsonResponse(data={
            'labels': labels,
            'overall': overallData,
            'top': topData,
            'jungle': jungData,
            'mid': midData,
            'bot': botData,
            'support': suppData
        })
class ChampionPlayerCountTableView(DetailView):
    model = Champion
    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        queryset = Player.objects.all()
        playersPlayed = self.object.getPlayersPlayed()

        for player in queryset:
            playerDict = {}
            playerDict["name"] = player.playerName
            if player.playerName not in playersPlayed:
                continue
            else:
                playerDict["playCount"] = playersPlayed[player.playerName]
                playerDict["winrate"] = player.getWinrateOnChampion(self.object)
                playerDict["averageKDA"] = player.getAverageKDAChampionString(self.object)
                playerDict['playerID'] = player.id
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })

class ChampionGamesTable(DetailView):
    model = Champion

    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Champion
        gamesPlayed = GameLaner.objects.filter(champion__exact=self.object.id)
        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)
        for stat in stats:
            stat: GameLanerStats
            statDict = {}
            statDict['gameNum'] = stat.gameLaner.game.gameNumber
            if stat.gameLaner.blueTeam:
                teamString = "Blue"
                if stat.gameLaner.game.gameBlueWins:
                    win = "W"
                else:
                    win = "L"
            else:
                teamString = "Red"
                if not stat.gameLaner.game.gameBlueWins:
                    win = "W"
                else:
                    win = "L"
            statDict['team'] = teamString
            statDict['player'] = stat.gameLaner.player.playerName
            statDict['lane'] = stat.gameLaner.lane.laneName
            statDict['winLoss'] = win
            statDict['duration'] = stat.gameLaner.game.gameDuration
            statDict['kills'] = stat.kills
            statDict['deaths'] = stat.deaths
            statDict['assists'] = stat.assists
            statDict['largestKillingSpree'] = stat.largestKillingSpree
            statDict['largestMultiKill'] = stat.largestMultiKill
            statDict['doubleKills'] = stat.doubleKills
            statDict['tripleKills'] = stat.tripleKills
            statDict['quadraKills'] = stat.quadraKills
            statDict['pentaKills'] = stat.pentaKills
            statDict['totalDamageDealtToChampions'] = stat.totalDamageDealtToChampions
            statDict['visionScore'] = stat.visionScore
            statDict['crowdControlScore'] = stat.crowdControlScore
            statDict['totalDamageTaken'] = stat.totalDamageTaken
            statDict['goldEarned'] = stat.goldEarned
            statDict['turretKills'] = stat.turretKills
            statDict['inhibitorKills'] = stat.inhibitorKills
            statDict['cs'] = stat.laneMinionsKilled + stat.neutralMinionsKilled
            statDict['teamJungleMinionsKilled'] = stat.teamJungleMinionsKilled
            statDict['enemyJungleMinionsKilled'] = stat.enemyJungleMinionsKilled
            statDict['controlWardsPurchased'] = stat.controlWardsPurchased
            statDict['firstBlood'] = stat.firstBlood
            statDict['firstTower'] = stat.firstTower
            statDict['csRateFirstTen'] = stat.csRateFirstTen
            statDict['csRateSecondTen'] = (stat.csRateSecondTen + stat.csRateFirstTen)/2
            statDict['gameID'] = stat.gameLaner.game.id
            statDict['playerID'] = stat.gameLaner.player.id

            data.append(statDict)

        return JsonResponse(
            data={
                'data':data
            }
        )

class NewPlayerView(FormView, BaseTenMansContextMixin):
    template_name = 'tenMans/new_player.html'
    form_class = CreatePlayer
    success_url = '/ten_mans/'

    @transaction.atomic
    def form_valid(self, form: CreatePlayer):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        try:
            form.submit_player()
        except Error:
            return super().form_invalid(form)


        return super().form_valid(form)