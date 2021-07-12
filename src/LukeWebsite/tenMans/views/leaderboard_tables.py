
from django.http.response import JsonResponse
from django.views import View

from tenMans.models import (Game, Player)


class LeaderboardSorter():

    def getLineDict(scores, names, playerIDs, gameIDs=None):

        unique_top_scores = sorted((list(set(scores))), reverse=True)[:3]

        if gameIDs is None:
            fullList = zip(scores, names, playerIDs)
        else:
            fullList = zip(scores, names, gameIDs, playerIDs)

        leaderboardList = []

        for item in fullList:
            if item[0] in unique_top_scores:
                leaderboardList.append(item)

        leaderboard = sorted(leaderboardList, reverse=True)

        return leaderboard


class MostKillsGameTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        scores = [player.getHighestKillCountGameLaneStats(None).kills for player in players if player.getHighestKillCountGameLaneStats(None) is not None]
        names = [player.playerName for player in players if player.getHighestKillCountGameLaneStats(None) is not None]
        gameIDs = [player.getHighestKillCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestKillCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players if player.getHighestKillCountGameLaneStats(None) is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)

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
        names = [player.playerName for player in players if player.getHighestDeathCountGameLaneStats(None) is not None]
        gameIDs = [player.getHighestDeathCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestDeathCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players if player.getHighestDeathCountGameLaneStats(None) is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)
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
        names = [player.playerName for player in players if player.getHighestAssistCountGameLaneStats(None) is not None]
        gameIDs = [player.getHighestAssistCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestAssistCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players if player.getHighestAssistCountGameLaneStats(None) is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)
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
        names = [player.playerName for player in players if player.getHighestDamageCountGameLaneStats(None) is not None]
        gameIDs = [player.getHighestDamageCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestDamageCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players if player.getHighestDamageCountGameLaneStats(None) is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)
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
        names = [player.playerName for player in players if player.getHighestSpreeCountGameLaneStats(None) is not None]
        gameIDs = [player.getHighestSpreeCountGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestSpreeCountGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players if player.getHighestSpreeCountGameLaneStats(None) is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)
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
        names = [player.playerName for player in players if player.getHighestCSGameLaneStats(None) is not None]
        gameIDs = [player.getHighestCSGameLaneStats(None).gameLaner.game.id for player in players if player.getHighestCSGameLaneStats(None) is not None]
        playerIDs = [player.id for player in players if player.getHighestCSGameLaneStats(None) is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)
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
        playerIDs = [player.id for player in players if player.getHighestCSFirstTwentyGameLaneStats(None) is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)
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
        playerIDs = [player.id for player in players if player.getHighestVisionGameLaneStats(None) is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)
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
        playerIDs = [player.id for player in players if player.getHighestControlWardGameLaneStats(None) is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)
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
        playerIDs = [player.id for player in players if player.getHighestBanGame(None)['game.id'] is not None]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs, gameIDs)
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

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs)
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['champions'] = line[0]
            lineDict['playerID'] = line[2]
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class CaptainWinrateTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        player: Player
        scores = [player.getCaptainWinrate() for player in players if player.getCaptainWinrate() != "N/A" and player.getCaptainGamesPlayed() >= 3]
        names = [player.playerName for player in players if player.getCaptainWinrate() != "N/A" and player.getCaptainGamesPlayed() >= 3]
        playerIDs = [player.id for player in players if player.getCaptainWinrate() != "N/A" and player.getCaptainGamesPlayed() >= 3]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs)
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['winrate'] = line[0]
            lineDict['playerID'] = line[2]
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class CaptainCountTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        player: Player
        scores = [player.getCaptainGamesPlayed() for player in players]
        names = [player.playerName for player in players]
        playerIDs = [player.id for player in players]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs)
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['count'] = line[0]
            lineDict['playerID'] = line[2]
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class WinstreakTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        player: Player
        scores = [player.getHighestWinstreak(None) for player in players]
        names = [player.playerName for player in players]
        playerIDs = [player.id for player in players]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs)
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['count'] = line[0]
            lineDict['playerID'] = line[2]
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })


class PentakillsTable(View):
    def get(self, request, *args, **kwargs):
        data = []
        players = Player.objects.all()

        player: Player
        scores = [player.getHighestWinstreak(None) for player in players]
        names = [player.playerName for player in players]
        playerIDs = [player.id for player in players]

        leaderboard = LeaderboardSorter.getLineDict(scores, names, playerIDs)
        for line in leaderboard:
            lineDict = {}
            lineDict['name'] = line[1]
            lineDict['count'] = line[0]
            lineDict['playerID'] = line[2]
            data.append(lineDict)

        return JsonResponse(data={
            'data': data
        })
