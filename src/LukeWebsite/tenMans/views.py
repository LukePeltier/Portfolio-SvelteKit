import datetime
import logging

from django.db import transaction
from django.db.utils import Error
from django.http.response import JsonResponse
from django.views import View
from django.views.generic.base import ContextMixin, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from tenMans.extras.data import GlobalVars
from tenMans.forms import (CreatePlayer, DuoForm, LaneMatchup, NewGameForm,
                           UpdateAllGamesForm, UpdateGameForm)
from tenMans.models import (Champion, Game, GameBan, GameLaner, GameLanerStats, Lane,
                            Player)


class BaseTenMansContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseTenMansContextMixin, self).get_context_data(*args, **kwargs)
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
                champDict['championVersion'] = GlobalVars.getLoLVersion()
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
        versionNumber = GlobalVars.getLoLVersion()
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
            statDict['csRateSecondTen'] = (stat.csRateSecondTen + stat.csRateFirstTen) / 2
            statDict['gameID'] = stat.gameLaner.game.id
            statDict['championID'] = stat.gameLaner.champion.id
            statDict['riotChampionName'] = stat.gameLaner.champion.riotName
            statDict['championVersion'] = versionNumber

            data.append(statDict)

        return JsonResponse(
            data={
                'data': data
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
        logging.info("Game submit complete")
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
            # get list of players involved
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
    model = Game

    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Game
        gameLaners = GameLaner.objects.filter(game__exact=self.object.id, blueTeam__exact=True)
        stats = GameLanerStats.objects.filter(gameLaner__in=gameLaners)
        versionNumber = GlobalVars.getLoLVersion()

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
            playerDict['csRateSecondTen'] = (statLine.csRateSecondTen + statLine.csRateFirstTen) / 2
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
    model = Game

    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Game
        gameLaners = GameLaner.objects.filter(game__exact=self.object.id, blueTeam__exact=False)
        stats = GameLanerStats.objects.filter(gameLaner__in=gameLaners)
        versionNumber = GlobalVars.getLoLVersion()

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
            playerDict['csRateSecondTen'] = (statLine.csRateSecondTen + statLine.csRateFirstTen) / 2
            playerDict["draftOrder"] = statLine.gameLaner.getDraftString()
            playerDict['playerID'] = statLine.gameLaner.player.id
            playerDict['championID'] = statLine.gameLaner.champion.id
            playerDict['riotChampionName'] = statLine.gameLaner.champion.riotName
            playerDict['championVersion'] = versionNumber
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })


class BlueTeamBanTable(DetailView):
    model = Game

    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Game
        enemyList = GameLaner.objects.filter(game__exact=self.object.id, blueTeam__exact=False)
        gameBans = GameBan.objects.filter(game__exact=self.object.id, targetPlayer__in=[enemy.player for enemy in enemyList])
        versionNumber = GlobalVars.getLoLVersion()

        for ban in gameBans:
            playerDict = {}
            playerDict["playerName"] = ban.targetPlayer.playerName
            playerDict['champion'] = ban.champion.championName
            playerDict['playerID'] = ban.targetPlayer.id
            playerDict['championID'] = ban.champion.id
            playerDict['riotChampionName'] = ban.champion.riotName
            playerDict['championVersion'] = versionNumber
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })


class RedTeamBanTable(DetailView):
    model = Game

    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Game
        enemyList = GameLaner.objects.filter(game__exact=self.object.id, blueTeam__exact=True)
        gameBans = GameBan.objects.filter(game__exact=self.object.id, targetPlayer__in=[enemy.player for enemy in enemyList])
        versionNumber = GlobalVars.getLoLVersion()

        for ban in gameBans:
            playerDict = {}
            playerDict["playerName"] = ban.targetPlayer.playerName
            playerDict['champion'] = ban.champion.championName
            playerDict['playerID'] = ban.targetPlayer.id
            playerDict['championID'] = ban.champion.id
            playerDict['riotChampionName'] = ban.champion.riotName
            playerDict['championVersion'] = versionNumber
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })


class ChampionListView(ListView, BaseTenMansContextMixin):
    model = Champion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['naChampVersion'] = GlobalVars.getLoLVersion()

        return context


class ChampionDetailView(DetailView, BaseTenMansContextMixin):
    model = Champion
    object: Champion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['naChampVersion'] = GlobalVars.getLoLVersion()
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
            statDict['csRateSecondTen'] = (stat.csRateSecondTen + stat.csRateFirstTen) / 2
            statDict['gameID'] = stat.gameLaner.game.id
            statDict['playerID'] = stat.gameLaner.player.id

            data.append(statDict)

        return JsonResponse(
            data={
                'data': data
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
            form.create_player()
        except Error:
            return super().form_invalid(form)

        return super().form_valid(form)


class LaneMatchupView(FormView, BaseTenMansContextMixin):
    template_name = 'tenMans/lane_matchup.html'
    form_class = LaneMatchup

    def get(self, request, *args, **kwargs):
        self.player1 = None
        self.player2 = None
        self.show_results = False
        form = LaneMatchup(self.request.GET or None)
        if form.is_valid():
            self.show_results = True
            self.player1 = form.cleaned_data['player1']
            self.player2 = form.cleaned_data['player2']

        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(LaneMatchupView, self).get_context_data(**kwargs)
        context.update({
            'show_results': self.show_results,
            'player1': self.player1,
            'player2': self.player2
        })
        return context


class LaneMatchupChartView(View):

    def get(self, request, pk1, pk2, *args, **kwargs):
        player1 = Player.objects.get(pk=pk1)
        player1: Player
        player2 = Player.objects.get(pk=pk2)
        player2: Player
        labels, player1Data, player2Data = ([] for i in range(3))

        labels.append("Overall")
        labels.append("Top")
        labels.append("Jungle")
        labels.append("Mid")
        labels.append("Bot/Support")

        player1Data.append(player1.getMatchupWinrate(player2, None))
        player1Data.append(player1.getMatchupWinrate(player2, [Lane.objects.get(laneName__exact="Top")]))
        player1Data.append(player1.getMatchupWinrate(player2, [Lane.objects.get(laneName__exact="Jungle")]))
        player1Data.append(player1.getMatchupWinrate(player2, [Lane.objects.get(laneName__exact="Mid")]))
        player1Data.append(player1.getMatchupWinrate(player2, [Lane.objects.get(laneName__exact="Bot"), Lane.objects.get(laneName__exact="Support")]))

        player2Data.append(player2.getMatchupWinrate(player1, None))
        player2Data.append(player2.getMatchupWinrate(player1, [Lane.objects.get(laneName__exact="Top")]))
        player2Data.append(player2.getMatchupWinrate(player1, [Lane.objects.get(laneName__exact="Jungle")]))
        player2Data.append(player2.getMatchupWinrate(player1, [Lane.objects.get(laneName__exact="Mid")]))
        player2Data.append(player2.getMatchupWinrate(player1, [Lane.objects.get(laneName__exact="Bot"), Lane.objects.get(laneName__exact="Support")]))

        return JsonResponse(data={
            'labels': labels,
            'player1Name': player1.playerName,
            'player2Name': player2.playerName,
            'player1Data': player1Data,
            'player2Data': player2Data
        })


class MatchupGamesTable(View):

    def get(self, request, pk1, pk2, *args, **kwargs):
        data = []
        player1 = Player.objects.get(pk=pk1)
        player1: Player
        player2 = Player.objects.get(pk=pk2)
        player2: Player
        gamesPlayedLeft = player1.getGameLanerMatchupList(player2, None)
        gamesPlayedRight = player2.getGameLanerMatchupList(player1, None)
        statsLeft = GameLanerStats.objects.filter(gameLaner__in=gamesPlayedLeft)
        statsRight = GameLanerStats.objects.filter(gameLaner__in=gamesPlayedRight)
        versionNumber = GlobalVars.getLoLVersion()
        for i in range(len(statsLeft)):
            statLeft = statsLeft[i]
            statRight = statsRight[i]
            statLeft: GameLanerStats
            statRight: GameLanerStats
            statDict = {}
            statDict['gameNum'] = statLeft.gameLaner.game.gameNumber
            if statLeft.gameLaner.blueTeam:
                if statLeft.gameLaner.game.gameBlueWins:
                    leftwin = "W"
                    rightwin = "L"
                else:
                    leftwin = "L"
                    rightwin = "W"
            else:
                if not statLeft.gameLaner.game.gameBlueWins:
                    leftwin = "W"
                    rightwin = "L"
                else:
                    leftwin = "L"
                    rightwin = "W"

            statDict['leftchampion'] = statLeft.gameLaner.champion.championName
            statDict['leftcs'] = statLeft.laneMinionsKilled + statLeft.neutralMinionsKilled
            statDict['leftkda'] = "{}/{}/{}".format(statLeft.kills, statLeft.deaths, statLeft.assists)
            statDict['leftlane'] = statLeft.gameLaner.lane.laneName
            statDict['leftwinLoss'] = leftwin

            statDict['rightchampion'] = statRight.gameLaner.champion.championName
            statDict['rightcs'] = statRight.laneMinionsKilled + statRight.neutralMinionsKilled
            statDict['rightkda'] = "{}/{}/{}".format(statRight.kills, statRight.deaths, statRight.assists)
            statDict['rightlane'] = statRight.gameLaner.lane.laneName
            statDict['rightwinLoss'] = rightwin

            statDict['gameID'] = statLeft.gameLaner.game.id
            statDict['leftchampionID'] = statLeft.gameLaner.champion.id
            statDict['leftriotChampionName'] = statLeft.gameLaner.champion.riotName
            statDict['rightchampionID'] = statRight.gameLaner.champion.id
            statDict['rightriotChampionName'] = statRight.gameLaner.champion.riotName
            statDict['championVersion'] = versionNumber
            statDict['highlightRow'] = False
            if statLeft.gameLaner.lane == statRight.gameLaner.lane or (statLeft.gameLaner.lane.laneName == "Support" and statRight.gameLaner.lane.laneName == "Bot") or statLeft.gameLaner.lane.laneName == "Bot" and statRight.gameLaner.lane.laneName == "Support":
                statDict['highlightRow'] = True

            data.append(statDict)

        return JsonResponse(
            data={
                'data': data
            }
        )


class MatchupCountTable(View):

    def get(self, request, pk1, pk2, *args, **kwargs):
        data = []
        player1 = Player.objects.get(pk=pk1)
        player1: Player
        player2 = Player.objects.get(pk=pk2)
        player2: Player
        laneNames = [["Top"], ["Jungle"], ["Mid"], ["Bot", "Support"]]
        laneDict = {}
        laneDict["lane"] = "Overall"
        laneDict["playCount"] = len(player1.getGameLanerMatchupList(player2, None))
        data.append(laneDict)

        for lane in laneNames:
            laneDict = {}
            laneDict["lane"] = '/'.join(lane)
            laneDict["playCount"] = len(player1.getGameLanerMatchupList(player2, [Lane.objects.get(laneName__exact=x) for x in lane]))
            data.append(laneDict)

        return JsonResponse(data={
            'data': data
        })


class DuoView(FormView, BaseTenMansContextMixin):
    template_name = 'tenMans/duos.html'
    form_class = DuoForm

    def get(self, request, *args, **kwargs):
        self.player1 = None
        self.player2 = None
        self.duoWinrate = None
        self.show_results = False
        form = DuoForm(self.request.GET or None)
        if form.is_valid():
            self.show_results = True
            self.player1 = form.cleaned_data['player1']
            self.player2 = form.cleaned_data['player2']
            self.duoWinrate = self.player1.getDuoWinrate(self.player2)

        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(DuoView, self).get_context_data(**kwargs)
        context.update({
            'show_results': self.show_results,
            'player1': self.player1,
            'player2': self.player2,
            'duoWinrate': self.duoWinrate
        })
        return context


class DuoGamesTable(View):

    def get(self, request, pk1, pk2, *args, **kwargs):
        data = []
        player1 = Player.objects.get(pk=pk1)
        player1: Player
        player2 = Player.objects.get(pk=pk2)
        player2: Player
        gamesPlayedLeft = player1.getGameLanerDuoList(player2)
        gamesPlayedRight = player2.getGameLanerDuoList(player1)
        statsLeft = GameLanerStats.objects.filter(gameLaner__in=gamesPlayedLeft)
        statsRight = GameLanerStats.objects.filter(gameLaner__in=gamesPlayedRight)
        versionNumber = GlobalVars.getLoLVersion()
        for i in range(len(statsLeft)):
            statLeft = statsLeft[i]
            statRight = statsRight[i]
            statLeft: GameLanerStats
            statRight: GameLanerStats
            statDict = {}
            statDict['gameNum'] = statLeft.gameLaner.game.gameNumber
            if statLeft.gameLaner.blueTeam:
                if statLeft.gameLaner.game.gameBlueWins:
                    leftwin = "W"
                else:
                    leftwin = "L"
            else:
                if not statLeft.gameLaner.game.gameBlueWins:
                    leftwin = "W"
                else:
                    leftwin = "L"

            statDict['leftchampion'] = statLeft.gameLaner.champion.championName
            statDict['leftcs'] = statLeft.laneMinionsKilled + statLeft.neutralMinionsKilled
            statDict['leftkda'] = "{}/{}/{}".format(statLeft.kills, statLeft.deaths, statLeft.assists)
            statDict['leftlane'] = statLeft.gameLaner.lane.laneName
            statDict['leftwinLoss'] = leftwin

            statDict['rightchampion'] = statRight.gameLaner.champion.championName
            statDict['rightcs'] = statRight.laneMinionsKilled + statRight.neutralMinionsKilled
            statDict['rightkda'] = "{}/{}/{}".format(statRight.kills, statRight.deaths, statRight.assists)
            statDict['rightlane'] = statRight.gameLaner.lane.laneName

            statDict['gameID'] = statLeft.gameLaner.game.id
            statDict['leftchampionID'] = statLeft.gameLaner.champion.id
            statDict['leftriotChampionName'] = statLeft.gameLaner.champion.riotName
            statDict['rightchampionID'] = statRight.gameLaner.champion.id
            statDict['rightriotChampionName'] = statRight.gameLaner.champion.riotName
            statDict['championVersion'] = versionNumber
            statDict['highlightRow'] = False
            if statLeft.gameLaner.lane == statRight.gameLaner.lane or (statLeft.gameLaner.lane.laneName == "Support" and statRight.gameLaner.lane.laneName == "Bot") or statLeft.gameLaner.lane.laneName == "Bot" and statRight.gameLaner.lane.laneName == "Support":
                statDict['highlightRow'] = True

            data.append(statDict)

        return JsonResponse(
            data={
                'data': data
            }
        )


class Leaderboards(TemplateView, BaseTenMansContextMixin):

    template_name = "tenMans/leaderboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gameTotal'] = Game.objects.all().count()
        context['memeTotal'] = Game.objects.all().filter(gameMemeStatus=True).count()
        return context


class MostKillsGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestKillCountGameLaneStats(None).kills for player in players if player.getHighestKillCountGameLaneStats(None) is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestKillCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestKillCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['kills'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostDeathsGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestDeathCountGameLaneStats(None).deaths for player in players if player.getHighestDeathCountGameLaneStats(None) is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestDeathCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestDeathCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['deaths'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostAssistsGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestAssistCountGameLaneStats(None).assists for player in players if player.getHighestAssistCountGameLaneStats(None) is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestAssistCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestAssistCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['assists'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostDamageGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestDamageCountGameLaneStats(None).totalDamageDealtToChampions for player in players if player.getHighestDamageCountGameLaneStats(None) is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestDamageCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestDamageCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['damage'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostSpreeGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestSpreeCountGameLaneStats(None).largestKillingSpree for player in players if player.getHighestSpreeCountGameLaneStats(None) is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestSpreeCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestSpreeCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['spree'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostCSGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestCSGameLaneStats(None).getTotalCS() for player in players if player.getHighestCSGameLaneStats(None) is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestCSGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestCSGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['cs'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostCSFirstTwentyGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestCSFirstTwentyGameLaneStats(None).getFirstTwentyCSRate() for player in players if player.getHighestCSFirstTwentyGameLaneStats(None) is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestCSFirstTwentyGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestCSFirstTwentyGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['cs'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostVisionGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestVisionGameLaneStats(None).visionScore for player in players if player.getHighestVisionGameLaneStats(None) is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestVisionGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestVisionGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['vision'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostControlWardGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestControlWardGameLaneStats(None).controlWardsPurchased for player in players if player.getHighestControlWardGameLaneStats(None) is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestControlWardGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestControlWardGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['cw'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostBanGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestBanGame(None)['bans'] for player in players if player.getHighestBanGame(None)['game.id'] is not None]
        names = [player.playerName for player in players]
        gameIDs = [player.getHighestBanGame(None)['game.id'] for player in players if player.getHighestBanGame(None)['game.id'] is not None]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, gameIDs, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['ban'] = line[0]
            lineDict['gameID'] = line[2]
            lineDict['playerID'] = line[3]
            lineDict['game'] = Game.objects.get(pk=line[2]).gameNumber
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class MostChampsTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getUniqueChampionCount() for player in players]
        names = [player.playerName for player in players]
        playerIDs = [player.id for player in players]

        leaderboard = sorted(zip(scores, names, playerIDs), reverse=True)[:3]
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['champions'] = line[0]
            lineDict['playerID'] = line[2]
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })
