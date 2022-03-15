from django.db import models
from django.db.utils import ProgrammingError
from scipy import stats
import numpy as np
from django_cassiopeia import cassiopeia as cass
import importlib
from django.db.models import Max
# Create your models here.


class Season(models.Model):
    seasonNumber = models.PositiveIntegerField(unique=True)

    def getCurrentSeason():
        try:
            maxSeason = Game.objects.aggregate(Max('season__seasonNumber'))['season__seasonNumber__max']
            if maxSeason is None:
                return 1
            return maxSeason
        except ProgrammingError:
            return 1

    def getCurrentSeasonObject():
        return Season.objects.get(seasonNumber__exact=Season.getCurrentSeason())


class Leaderboard(models.Model):
    leaderboardName = models.TextField(unique=True)
    leaderboardValueName = models.TextField()
    leaderboardEmoji = models.TextField()
    leaderboardIsLifetime = models.BooleanField()
    leaderboardURLName = models.TextField(default='')
    leaderboardViewClassName = models.TextField(null=False)

    def getTrophyHolder(self):
        # from  import (MostKillsGameTable)  # noqa: F401
        mod = importlib.import_module('tenMans.views.leaderboard_tables')
        leaderboardclass_ = getattr(mod, self.leaderboardViewClassName)
        instance = leaderboardclass_()
        results = instance.get(None, objectReturn=True)
        if not results:
            return None
        playerID = results[0]['playerID']
        return playerID


class Game(models.Model):
    gameNumber = models.PositiveIntegerField(unique=True)
    gameBlueWins = models.BooleanField()
    gameRandomTeams = models.BooleanField()
    gameMemeStatus = models.BooleanField(default=0)
    gameDate = models.DateTimeField(auto_now_add=True)
    gameDuration = models.PositiveIntegerField()
    gameRiotID = models.PositiveBigIntegerField(null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, default=1)
    gameEndedInSurrender = models.BooleanField(default=0)
    gameEndedInEarlySurrender = models.BooleanField(default=0)

    def getTotalGames():
        return Game.objects.all().count()

    def __str__(self):
        return str(self.gameNumber)

    class Meta:
        ordering = ["gameNumber"]
        verbose_name_plural = "games"


class Player(models.Model):
    playerName = models.TextField(unique=True)

    def getWinrate(self, lane, season):
        if(lane is None and season is None):
            # Overall winrate
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        elif(lane is None):
            # season winrate
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, game__season__exact=season.id)
        elif(season is None):
            # Overall lane winrate
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, lane__exact=lane.id)
        else:
            # Lane winrate
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, lane__exact=lane.id, game__season__exact=season.id)
        winrate = Player.getWinrateOnList(gamesPlayed)
        if winrate is None:
            return "N/A"
        return winrate

    def getLaneRate(self, lane, season):
        players = Player.objects.all()
        topNumber = 0
        for player in players:
            count = player.getLaneCount(lane, season)
            if(count > topNumber):
                topNumber = count
        playerNumber = self.getLaneCount(lane, season)
        return round(playerNumber / topNumber, 1)

    def getLaneCount(self, lane, season):
        if(lane is None and season is None):
            # Overall
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        elif(lane is None):
            # season
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, game__season__exact=season.id)
        elif(season is None):
            # Overall lane
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, lane__exact=lane.id)
        else:
            # Season Lane
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, lane__exact=lane.id, game__season__exact=season.id)
        return gamesPlayed.count()

    def getWinrateHistorical(self, maxGame, lane):
        if(lane is None):
            # Overall winrate
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, game__gameNumber__lte=maxGame.gameNumber)
        else:
            # Lane winrate
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id,
                lane__exact=lane.id,
                game__gameNumber__lte=maxGame.gameNumber)
        winrate = Player.getWinrateOnList(gamesPlayed)
        if winrate is None:
            return "N/A"
        return winrate

    def getAverageDraftOrder(self):
        totalDraftSum = 0
        gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        totalDraftDivisor = gamesPlayed.count()
        if totalDraftDivisor < 3:
            return None
        for gameLane in gamesPlayed:
            if(gameLane.draftOrder is None):
                totalDraftDivisor -= 1
                continue
            totalDraftSum += gameLane.draftOrder
        if totalDraftDivisor == 0:
            return None
        return round(totalDraftSum / totalDraftDivisor, 2)

    def getMinConfidenceWinrate(self, lane):
        if self.getWinrate(lane, None) == 'N/A' or self.getLaneCount(lane, None) < 3:
            return None
        conf_int = stats.norm.interval(0.5, self.getWinrate(
            lane, None) / 100, (0.5 / np.sqrt(self.getLaneCount(lane, None))))
        return round(max(conf_int[0], 0) * 100, 2)

    def getMinConfidenceCaptainWinrate(self):
        if self.getCaptainGamesPlayed() < 3:
            return None
        conf_int = stats.norm.interval(0.5, self.getCaptainWinrate() / 100, (0.5 / np.sqrt(self.getCaptainGamesPlayed())))
        return round(max(conf_int[0], 0) * 100, 2)

    def getMostPlayedLaneString(self):
        gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        laneCounts = {"Top": 0, "Jungle": 0, "Mid": 0, "Bot": 0, "Support": 0}
        for gameLane in gamesPlayed:
            laneCounts[gameLane.lane.laneName] += 1
        laneNames = []
        currentMax = 0
        for lane, count in laneCounts.items():
            if(count < currentMax):
                continue
            elif(count == currentMax):
                laneNames.append(lane)
            elif(count > currentMax):
                currentMax = count
                laneNames.clear()
                laneNames.append(lane)
        return "/".join(laneNames) + " ({} games)".format(currentMax)

    def getMostPlayedChampionString(self):
        champCounts = self.championsPlayed()
        champNames = []
        currentMax = 0
        for champ, count in champCounts.items():
            if(count < currentMax):
                continue
            elif(count == currentMax):
                champNames.append(champ)
            elif(count > currentMax):
                currentMax = count
                champNames.clear()
                champNames.append(champ)
        return "/".join(sorted(champNames)) + " ({} games)".format(currentMax)

    def getWinrateOnChampion(self, champion):
        # Lane winrate
        gamesPlayed = GameLaner.objects.filter(
            player__exact=self.id, champion__exact=champion.id)
        winrate = Player.getWinrateOnList(gamesPlayed)
        if winrate is None:
            return "N/A"
        return winrate

    def getHighestWinrateChampionString(self):
        gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        champsPlayed = []
        for gameLane in gamesPlayed:
            champion = gameLane.champion
            if(champion not in champsPlayed):
                champsPlayed.append(champion)
        currentMax = 0
        champString = []
        for champ in champsPlayed:
            winrate = self.getWinrateOnChampion(champ)
            if(winrate < currentMax):
                continue
            elif(winrate == currentMax):
                champString.append(champ.championName)
            elif(winrate > currentMax):
                currentMax = winrate
                champString.clear()
                champString.append(champ.championName)
        return "/".join(sorted(champString)) + \
            " ({}% winrate)".format(currentMax)

    def playerParticipatedInGame(self, game):
        return GameLaner.objects.filter(
            player__exact=self.id, game__exact=game.id).exists()

    def getAveragePulledBans(self):
        bansTargeted = GameBan.objects.filter(targetPlayer__exact=self.id).count()
        gamesWithBans = GameBan.objects.filter(targetPlayer__exact=self.id).values('game').distinct()
        totalGameCount = gamesWithBans.count()
        if totalGameCount == 0:
            return "N/A"
        return round(bansTargeted / totalGameCount, 2)

    def getMostBannedChampionString(self):
        bansTotal = GameBan.objects.filter(targetPlayer__exact=self.id)
        champCounts = {}
        for gameBan in bansTotal:
            gameBan: GameBan
            championName = gameBan.champion.championName
            if(championName in champCounts):
                champCounts[championName] += 1
            else:
                champCounts[championName] = 1
        champNames = []
        currentMax = 0
        for champ, count in champCounts.items():
            if(count < currentMax):
                continue
            elif(count == currentMax):
                champNames.append(champ)
            elif(count > currentMax):
                currentMax = count
                champNames.clear()
                champNames.append(champ)
        return "/".join(sorted(champNames)) + " ({} bans)".format(currentMax)

    def getSideWinrate(self, side):
        blueTeamDetermine = side == "Blue"
        gamesPlayed = GameLaner.objects.filter(
            player__exact=self.id, blueTeam__exact=blueTeamDetermine)

        winrate = Player.getWinrateOnList(gamesPlayed)
        if winrate is None:
            return "N/A"
        return winrate

    def getAverageKDALaneString(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, lane__exact=lane.id)
        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)
        gameCount = gamesPlayed.count()
        if(gameCount == 0):
            return None
        kills = 0
        deaths = 0
        assists = 0
        for stat in stats:
            stat: GameLanerStats
            kills += stat.kills
            deaths += stat.deaths
            assists += stat.assists
        return "{}/{}/{}".format(round(kills / gameCount, 2),
                                 round(deaths / gameCount, 2), round(assists / gameCount, 2))

    def getAverageKDAChampionString(self, champion):
        if champion is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, champion__exact=champion.id)
        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)
        gameCount = gamesPlayed.count()
        if(gameCount == 0):
            return None
        kills = 0
        deaths = 0
        assists = 0
        for stat in stats:
            stat: GameLanerStats
            kills += stat.kills
            deaths += stat.deaths
            assists += stat.assists
        return "{}/{}/{}".format(round(kills / gameCount, 2),
                                 round(deaths / gameCount, 2), round(assists / gameCount, 2))

    def championsPlayed(self):
        gamesPlayed = GameLaner.objects.filter(
            player__exact=self.id, game__gameMemeStatus__exact=0)
        champCounts = {}
        for gameLane in gamesPlayed:
            championName = gameLane.champion.championName
            if(championName in champCounts):
                champCounts[championName] += 1
            else:
                champCounts[championName] = 1
        return champCounts

    def getUniqueChampionCount(self):
        champCounts = self.championsPlayed()
        return len(champCounts)

    def getMatchupWinrate(self, player, lanes):
        trueMatchups = self.getGameLanerMatchupList(player, lanes)

        totalGameCount = len(trueMatchups)
        if totalGameCount == 0:
            return None
        winningCount = 0
        for gameLane in trueMatchups:
            gameLane: GameLaner
            blueTeam = gameLane.blueTeam
            blueWin = gameLane.game.gameBlueWins
            if blueTeam == blueWin:
                winningCount += 1

        return round((winningCount / totalGameCount) * 100, 2)

    def getGameLanerMatchupList(self, player, lanes):
        trueMatchups = []
        if(lanes is None):
            # Overall winrate
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
            # find games opponent was also in
            for gameLane in gamesPlayed:
                opponentGame = GameLaner.objects.filter(player__exact=player.id, game__exact=gameLane.game.id, blueTeam__exact=(not gameLane.blueTeam))
                if opponentGame.exists():
                    trueMatchups.append(gameLane)

        else:
            # Lane winrate
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, lane__in=[lane.id for lane in lanes])
            # find games opponent was also in
            for gameLane in gamesPlayed:
                opponentGame = GameLaner.objects.filter(player__exact=player.id, game__exact=gameLane.game.id, blueTeam__exact=(not gameLane.blueTeam), lane__in=[lane.id for lane in lanes])
                if opponentGame.exists():
                    trueMatchups.append(gameLane)
        return trueMatchups

    def getGameLanerDuoList(self, player):
        trueDuos = []
        # Overall winrate
        gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        # find games opponent was also in
        for gameLane in gamesPlayed:
            opponentGame = GameLaner.objects.filter(player__exact=player.id, game__exact=gameLane.game.id, blueTeam__exact=gameLane.blueTeam)
            if opponentGame.exists():
                trueDuos.append(gameLane)
        return trueDuos

    def getDuoWinrate(self, player):
        trueDuos = self.getGameLanerDuoList(player)

        totalGameCount = len(trueDuos)
        if totalGameCount == 0:
            return None
        winningCount = 0
        for gameLane in trueDuos:
            gameLane: GameLaner
            blueTeam = gameLane.blueTeam
            blueWin = gameLane.game.gameBlueWins
            if blueTeam == blueWin:
                winningCount += 1

        return round((winningCount / totalGameCount) * 100, 2)

    def getHighestKillCountGameLaneStats(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        maxKills = -1
        currentBestStats = None
        for stat in stats:
            stat: GameLanerStats
            if stat.kills > maxKills:
                currentBestStats = stat
                maxKills = stat.kills
        return currentBestStats

    def getHighestDeathCountGameLaneStats(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        maxDeaths = -1
        currentBestStats = None
        for stat in stats:
            stat: GameLanerStats
            if stat.deaths > maxDeaths:
                currentBestStats = stat
                maxDeaths = stat.deaths
        return currentBestStats

    def getHighestAssistCountGameLaneStats(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        maxAssists = -1
        currentBestStats = None
        for stat in stats:
            stat: GameLanerStats
            if stat.assists > maxAssists:
                currentBestStats = stat
                maxAssists = stat.assists
        return currentBestStats

    def getHighestDamageCountGameLaneStats(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        maxDamage = -1
        currentBestStats = None
        for stat in stats:
            stat: GameLanerStats
            if stat.totalDamageDealtToChampions > maxDamage:
                currentBestStats = stat
                maxDamage = stat.totalDamageDealtToChampions
        return currentBestStats

    def getHighestSpreeCountGameLaneStats(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        maxSpree = -1
        currentBestStats = None
        for stat in stats:
            stat: GameLanerStats
            if stat.largestKillingSpree > maxSpree:
                currentBestStats = stat
                maxSpree = stat.largestKillingSpree
        return currentBestStats

    def getHighestCSGameLaneStats(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        maxCS = -1
        currentBestStats = None
        for stat in stats:
            stat: GameLanerStats
            if stat.getTotalCS() > maxCS:
                currentBestStats = stat
                maxCS = stat.getTotalCS()
        return currentBestStats

    def getHighestCSFirstTwentyGameLaneStats(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        maxCS = -1
        currentBestStats = None
        for stat in stats:
            stat: GameLanerStats
            if stat.getFirstTwentyCSRate() > maxCS:
                currentBestStats = stat
                maxCS = stat.getFirstTwentyCSRate()
        return currentBestStats

    def getHighestVisionGameLaneStats(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        maxVision = -1
        currentBestStats = None
        for stat in stats:
            stat: GameLanerStats
            if stat.visionScore > maxVision:
                currentBestStats = stat
                maxVision = stat.visionScore
        return currentBestStats

    def getHighestControlWardGameLaneStats(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        maxCW = -1
        currentBestStats = None
        for stat in stats:
            stat: GameLanerStats
            if stat.controlWardsPurchased > maxCW:
                currentBestStats = stat
                maxCW = stat.controlWardsPurchased
        return currentBestStats

    def getHighestBanGame(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        maxBans = -1
        currentBestGameID = None
        for gameLane in gamesPlayed:
            numOfBans = GameBan.objects.filter(game__exact=gameLane.game.id, targetPlayer__exact=self.id).count()
            if numOfBans > maxBans:
                currentBestGameID = gameLane.game.id
                maxBans = numOfBans
        return {"bans": maxBans, "game.id": currentBestGameID}

    def getCaptainWinrate(self):
        gamesPlayed = GameLaner.objects.filter(player__exact=self.id, draftOrder__isnull=True, game__gameRandomTeams__exact=False)

        winrate = Player.getWinrateOnList(gamesPlayed)
        if winrate is None:
            return "N/A"
        return winrate

    def getCaptainGamesPlayed(self):
        return GameLaner.objects.filter(player__exact=self.id, draftOrder__isnull=True, game__gameRandomTeams__exact=False).count()

    def getRandomsWinrate(self):
        gamesPlayed = GameLaner.objects.filter(player__exact=self.id, game__gameRandomTeams__exact=True)

        winrate = Player.getWinrateOnList(gamesPlayed)
        if winrate is None:
            return "N/A"
        return winrate

    def getRandomGamesPlayed(self):
        return GameLaner.objects.filter(player__exact=self.id, game__gameRandomTeams__exact=True).count()

    def getPentakills(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        totalPentas = 0
        for stat in stats:
            stat: GameLanerStats
            totalPentas += stat.pentaKills

        return totalPentas

    def getQuadrakills(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        totalQuadras = 0
        for stat in stats:
            stat: GameLanerStats
            totalQuadras += stat.quadraKills

        return totalQuadras

    def getTriplekills(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        totalTriples = 0
        for stat in stats:
            stat: GameLanerStats
            totalTriples += stat.tripleKills

        return totalTriples

    def getDoublekills(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)

        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)

        totalDoubles = 0
        for stat in stats:
            stat: GameLanerStats
            totalDoubles += stat.doubleKills

        return totalDoubles

    def getHighestWinstreak(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id).order_by('game__gameDate')
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id).order_by('game__gameDate')

        totalGameCount = gamesPlayed.count()
        if totalGameCount == 0:
            return (0, True)

        currentWinstreak = 0
        maxWinstreak = 0
        for gameLane in gamesPlayed.iterator():
            gameLane: GameLaner
            blueTeam = gameLane.blueTeam
            blueWin = gameLane.game.gameBlueWins
            if blueTeam == blueWin:
                currentWinstreak += 1
                if maxWinstreak < currentWinstreak:
                    maxWinstreak = currentWinstreak
            else:
                currentWinstreak = 0
        onStreak = bool(maxWinstreak == currentWinstreak)
        return (maxWinstreak, onStreak)

    def getHighestLossstreak(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id).order_by('game__gameDate')
        else:
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id).order_by('game__gameDate')

        totalGameCount = gamesPlayed.count()
        if totalGameCount == 0:
            return (0, True)

        currentLossstreak = 0
        maxLossstreak = 0
        for gameLane in gamesPlayed.iterator():
            gameLane: GameLaner
            blueTeam = gameLane.blueTeam
            blueWin = gameLane.game.gameBlueWins
            if blueTeam != blueWin:
                currentLossstreak += 1
                if maxLossstreak < currentLossstreak:
                    maxLossstreak = currentLossstreak
            else:
                currentLossstreak = 0
        onStreak = bool(maxLossstreak == currentLossstreak)
        return (maxLossstreak, onStreak)

    def getWinrateOnList(gamesPlayed):
        totalGameCount = gamesPlayed.count()
        if totalGameCount == 0:
            return None
        winningCount = 0
        for gameLane in gamesPlayed.iterator():
            gameLane: GameLaner
            blueTeam = gameLane.blueTeam
            blueWin = gameLane.game.gameBlueWins
            if blueTeam == blueWin:
                winningCount += 1

        return round((winningCount / totalGameCount) * 100, 2)

    def getTrophyCase(self):
        leaderboards = Leaderboard.objects.all()
        trophyArray = []
        for leaderboard in leaderboards:
            if leaderboard.getTrophyHolder() == self.id:
                trophyArray.append(leaderboard)

        return trophyArray

    def __str__(self):
        return self.playerName


class Champion(models.Model):
    championName = models.TextField(unique=True)
    riotName = models.TextField(unique=True, null=True)

    def getLaneCount(self, lane):
        if(lane is None):
            return GameLaner.objects.filter(champion__exact=self.id).count()
        else:
            return GameLaner.objects.filter(
                champion__exact=self.id, lane__exact=lane.id).count()

    def getMainLaneString(self):
        gamesPlayed = GameLaner.objects.filter(champion__exact=self.id)
        laneCounts = {"Top": 0, "Jungle": 0, "Mid": 0, "Bot": 0, "Support": 0}
        for gameLane in gamesPlayed:
            laneCounts[gameLane.lane.laneName] += 1
        laneNames = []
        currentMax = 0
        for lane, count in laneCounts.items():
            if(count < currentMax):
                continue
            elif(count == currentMax):
                laneNames.append(lane)
            elif(count > currentMax):
                currentMax = count
                laneNames.clear()
                laneNames.append(lane)
        return "/".join(laneNames) + " ({} games)".format(currentMax)

    def getPlayersPlayed(self):
        gamesPlayed = GameLaner.objects.filter(champion__exact=self.id)
        playerCounts = {}
        for gameLane in gamesPlayed:
            playerName = gameLane.player.playerName
            if(playerName in playerCounts):
                playerCounts[playerName] += 1
            else:
                playerCounts[playerName] = 1
        return playerCounts

    def getWinrate(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(champion__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(
                champion__exact=self.id, lane__exact=lane.id)

        winrate = Player.getWinrateOnList(gamesPlayed)
        if winrate is None:
            return "N/A"
        return winrate

    def getSideWinrate(self, side):
        blueTeamDetermine = side == "Blue"
        gamesPlayed = GameLaner.objects.filter(
            champion__exact=self.id, blueTeam__exact=blueTeamDetermine)
        winrate = Player.getWinrateOnList(gamesPlayed)
        if winrate is None:
            return "N/A"
        return winrate

    def getPickRate(self):
        totalGameCount = Game.objects.filter(
            gameMemeStatus__exact=False, id__gte=3).count()
        if totalGameCount == 0:
            return 0
        champGameCount = GameLaner.objects.filter(
            champion__exact=self.id,
            game__gameMemeStatus__exact=False,
            game__id__gte=3).count()
        return round((champGameCount / totalGameCount) * 100, 2)

    def getBanRate(self):
        totalGameCount = Game.objects.filter(
            gameMemeStatus__exact=False, id__gte=3).count()
        if totalGameCount == 0:
            return 0
        banCount = GameBan.objects.filter(
            champion__exact=self.id,
            game__gameMemeStatus__exact=False,
            game__id__gte=3).count()
        return round((banCount / totalGameCount) * 100, 2)

    def getAverageKDALaneString(self, lane):
        if lane is None:
            gamesPlayed = GameLaner.objects.filter(champion__exact=self.id)
        else:
            gamesPlayed = GameLaner.objects.filter(
                champion__exact=self.id, lane__exact=lane.id)
        stats = GameLanerStats.objects.filter(gameLaner__in=gamesPlayed)
        gameCount = gamesPlayed.count()
        if(gameCount == 0):
            return None
        kills = 0
        deaths = 0
        assists = 0
        for stat in stats:
            stat: GameLanerStats
            kills += stat.kills
            deaths += stat.deaths
            assists += stat.assists
        return "{}/{}/{}".format(round(kills / gameCount, 2),
                                 round(deaths / gameCount, 2), round(assists / gameCount, 2))

    def __str__(self):
        return self.championName

    class Meta:
        ordering = ['championName']


class Lane(models.Model):
    laneName = models.TextField(unique=True)

    def __str__(self):
        return self.laneName


class GameLaner(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    lane = models.ForeignKey(Lane, on_delete=models.CASCADE)
    blueTeam = models.BooleanField(default=1)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    draftOrder = models.PositiveIntegerField(null=True)
    championSelectOrder = models.PositiveIntegerField(null=True)

    def getDraftString(self):
        if self.draftOrder is not None:
            return str(self.draftOrder)
        else:
            if self.game.gameRandomTeams:
                return "R"
            else:
                return "C"

    class Meta:
        unique_together = (('game', 'lane', 'blueTeam'), ('player', 'game'))


class GameLanerStats(models.Model):
    gameLaner = models.OneToOneField(GameLaner, on_delete=models.CASCADE)

    kills = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()

    largestKillingSpree = models.PositiveIntegerField()
    largestMultiKill = models.PositiveIntegerField()
    doubleKills = models.PositiveIntegerField()
    tripleKills = models.PositiveIntegerField()
    quadraKills = models.PositiveIntegerField()
    pentaKills = models.PositiveIntegerField()

    totalDamageDealtToChampions = models.PositiveBigIntegerField()
    visionScore = models.PositiveIntegerField()
    crowdControlScore = models.PositiveIntegerField()
    totalDamageTaken = models.PositiveBigIntegerField()
    goldEarned = models.PositiveBigIntegerField()

    turretKills = models.PositiveIntegerField()
    inhibitorKills = models.PositiveIntegerField()

    laneMinionsKilled = models.PositiveIntegerField()
    neutralMinionsKilled = models.PositiveIntegerField()

    teamJungleMinionsKilled = models.PositiveIntegerField()
    enemyJungleMinionsKilled = models.PositiveIntegerField()

    controlWardsPurchased = models.PositiveIntegerField()

    firstBlood = models.BooleanField()
    firstTower = models.BooleanField()

    csRateFirstTen = models.FloatField()
    csRateSecondTen = models.FloatField()

    # match v5 only
    baronKills = models.PositiveIntegerField(default=0)
    dragonKills = models.PositiveIntegerField(default=0)

    goldSpent = models.PositiveIntegerField(default=0)

    largestCriticalStrike = models.PositiveIntegerField(default=0)
    longestTimeSpentLiving = models.PositiveIntegerField(default=0)
    killedNexus = models.BooleanField(default=0)
    objectivesStolen = models.PositiveIntegerField(default=0)
    numberOfFlashes = models.PositiveIntegerField(default=0)
    totalTimeSpentDead = models.PositiveIntegerField(default=0)
    timePlayed = models.PositiveIntegerField(default=0)

    def getTotalCS(self):
        return self.laneMinionsKilled + self.neutralMinionsKilled

    def getFirstTwentyCSRate(self):
        return (self.csRateFirstTen + self.csRateSecondTen) / 2

    def provideStats(localGame, champMap, match: cass.Match):
        if localGame.season.seasonNumber < 3:
            return
        for participant in match.participants:
            participant: cass.core.match.Participant
            # find champ
            championTrueName = champMap[participant.champion.id]
            championObject = Champion.objects.filter(championName__exact=championTrueName).get()
            gameLaner = GameLaner.objects.filter(champion__exact=championObject, game__exact=localGame).get()

            stats = participant.stats
            stats: cass.core.match.ParticipantStats
            foundkills = stats.kills
            founddeaths = stats.deaths
            foundassists = stats.assists
            foundlargestKillingSpree = stats.largest_killing_spree
            foundlargestMultiKill = stats.largest_multi_kill
            founddoubleKills = stats.double_kills
            foundtripleKills = stats.triple_kills
            foundquadraKills = stats.quadra_kills
            foundpentaKills = stats.penta_kills
            foundtotalDamageDealtToChampions = stats.total_damage_dealt_to_champions
            foundvisionScore = stats.vision_score
            foundcrowdControlScore = stats.time_CCing_others
            foundtotalDamageTaken = stats.total_damage_taken
            foundgoldEarned = stats.gold_earned
            foundturretKills = stats.turret_kills
            foundinhibitorKills = stats.inhibitor_kills
            foundlaneMinionsKilled = stats.total_minions_killed
            foundneutralMinionsKilled = stats.neutral_minions_killed
            foundteamJungleMinionsKilled = 0
            foundenemyJungleMinionsKilled = 0
            foundcontrolWardsPurchased = stats.vision_wards_bought
            foundfirstBlood = stats.first_blood_kill
            foundfirstTower = stats.first_tower_kill

            # match v5
            foundbaronKills = stats.baron_kills
            founddragonKills = stats.dragon_kills
            foundgoldSpent = stats.gold_spent
            foundlargestCriticalStrike = stats.largest_critical_strike
            foundlongestTimeSpentLiving = stats.longest_time_spent_living
            foundkilledNexus = stats.nexus_kills >= 0
            foundobjectivesStolen = stats.objectives_stolen
            foundnumberOfFlashes = 0

            # determine flash
            flashId = cass.SummonerSpell(name="Flash", region="NA").key
            if participant.summoner_spell_d == flashId:
                foundnumberOfFlashes = stats.summoner_spell_1_casts

            if participant.summoner_spell_f == flashId:
                foundnumberOfFlashes = stats.summoner_spell_2_casts

            foundtotalTimeSpentDead = stats.total_time_spent_dead
            foundtimePlayed = stats.time_played

            # check for existing statsObject
            try:
                statsObject = GameLanerStats.objects.get(gameLaner__exact=gameLaner)
            except GameLanerStats.DoesNotExist:
                statsObject = None

            if statsObject is not None:
                statsObject.kills = foundkills
                statsObject.deaths = founddeaths
                statsObject.assists = foundassists
                statsObject.largestKillingSpree = foundlargestKillingSpree
                statsObject.largestMultiKill = foundlargestMultiKill
                statsObject.doubleKills = founddoubleKills
                statsObject.tripleKills = foundtripleKills
                statsObject.quadraKills = foundquadraKills
                statsObject.pentaKills = foundpentaKills
                statsObject.totalDamageDealtToChampions = foundtotalDamageDealtToChampions
                statsObject.visionScore = foundvisionScore
                statsObject.crowdControlScore = foundcrowdControlScore
                statsObject.totalDamageTaken = foundtotalDamageTaken
                statsObject.goldEarned = foundgoldEarned
                statsObject.turretKills = foundturretKills
                statsObject.inhibitorKills = foundinhibitorKills
                statsObject.laneMinionsKilled = foundlaneMinionsKilled
                statsObject.neutralMinionsKilled = foundneutralMinionsKilled
                statsObject.teamJungleMinionsKilled = foundteamJungleMinionsKilled
                statsObject.enemyJungleMinionsKilled = foundenemyJungleMinionsKilled
                statsObject.controlWardsPurchased = foundcontrolWardsPurchased
                statsObject.firstBlood = foundfirstBlood
                statsObject.firstTower = foundfirstTower
                statsObject.baronKills = foundbaronKills
                statsObject.dragonKills = founddragonKills
                statsObject.goldSpent = foundgoldSpent
                statsObject.largestCriticalStrike = foundlargestCriticalStrike
                statsObject.longestTimeSpentLiving = foundlongestTimeSpentLiving
                statsObject.killedNexus = foundkilledNexus
                statsObject.objectivesStolen = foundobjectivesStolen
                statsObject.numberOfFlashes = foundnumberOfFlashes
                statsObject.totalTimeSpentDead = foundtotalTimeSpentDead
                statsObject.timePlayed = foundtimePlayed
                statsObject.save()

            else:
                statsObject = GameLanerStats(
                    gameLaner=gameLaner,
                    kills=foundkills,
                    deaths=founddeaths,
                    assists=foundassists,
                    largestKillingSpree=foundlargestKillingSpree,
                    largestMultiKill=foundlargestMultiKill,
                    doubleKills=founddoubleKills,
                    tripleKills=foundtripleKills,
                    quadraKills=foundquadraKills,
                    pentaKills=foundpentaKills,
                    totalDamageDealtToChampions=foundtotalDamageDealtToChampions,
                    visionScore=foundvisionScore,
                    crowdControlScore=foundcrowdControlScore,
                    totalDamageTaken=foundtotalDamageTaken,
                    goldEarned=foundgoldEarned,
                    turretKills=foundturretKills,
                    inhibitorKills=foundinhibitorKills,
                    laneMinionsKilled=foundlaneMinionsKilled,
                    neutralMinionsKilled=foundneutralMinionsKilled,
                    teamJungleMinionsKilled=foundteamJungleMinionsKilled,
                    enemyJungleMinionsKilled=foundenemyJungleMinionsKilled,
                    controlWardsPurchased=foundcontrolWardsPurchased,
                    firstBlood=foundfirstBlood,
                    firstTower=foundfirstTower,
                    csRateFirstTen=0,
                    csRateSecondTen=0,
                    baronKills=foundbaronKills,
                    dragonKills=founddragonKills,
                    goldSpent=foundgoldSpent,
                    largestCriticalStrike=foundlargestCriticalStrike,
                    longestTimeSpentLiving=foundlongestTimeSpentLiving,
                    killedNexus=foundkilledNexus,
                    objectivesStolen=foundobjectivesStolen,
                    numberOfFlashes=foundnumberOfFlashes,
                    totalTimeSpentDead=foundtotalTimeSpentDead,
                    timePlayed=foundtimePlayed)
                statsObject.save()


class GameBan(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    targetPlayer = models.ForeignKey(
        Player, on_delete=models.CASCADE, null=True)
