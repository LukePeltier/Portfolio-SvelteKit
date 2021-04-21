from django.db import models
from scipy import stats
import numpy as np

# Create your models here.


class Game(models.Model):
    gameNumber = models.PositiveIntegerField(unique=True)
    gameBlueWins = models.BooleanField()
    gameRandomTeams = models.BooleanField()
    gameMemeStatus = models.BooleanField(default=0)
    gameDate = models.DateTimeField(default='current_timestamp()')
    gameDuration = models.PositiveIntegerField()
    gameRiotID = models.PositiveBigIntegerField(null=True)

    def getTotalGames():
        return Game.objects.all().count()

    def __str__(self):
        return str(self.gameNumber)

    class Meta:
        ordering = ["gameNumber"]
        verbose_name_plural = "games"


class Player(models.Model):
    playerName = models.TextField(unique=True)

    def getWinrate(self, lane):
        if(lane is None):
            # Overall winrate
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
            totalGameCount = gamesPlayed.count()
            totalGameCount = gamesPlayed.count()
            if totalGameCount == 0:
                return "N/A"
            winningCount = 0
            for gameLane in gamesPlayed.iterator():
                gameLane: GameLaner
                blueTeam = gameLane.blueTeam
                blueWin = gameLane.game.gameBlueWins
                if blueTeam == blueWin:
                    winningCount += 1

            return round((winningCount / totalGameCount) * 100, 2)
        else:
            # Lane winrate
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, lane__exact=lane.id)
            totalGameCount = gamesPlayed.count()
            if totalGameCount == 0:
                return "N/A"
            winningCount = 0
            for gameLane in gamesPlayed.iterator():
                gameLane: GameLaner
                blueTeam = gameLane.blueTeam
                blueWin = gameLane.game.gameBlueWins
                if blueTeam == blueWin:
                    winningCount += 1

            return round((winningCount / totalGameCount) * 100, 2)

    def getLaneRate(self, lane):
        players = Player.objects.all()
        topNumber = 0
        for player in players:
            count = player.getLaneCount(lane)
            if(count > topNumber):
                topNumber = count
        playerNumber = self.getLaneCount(lane)
        return round(playerNumber / topNumber, 1)

    def getLaneCount(self, lane):
        if(lane is None):
            return GameLaner.objects.filter(player__exact=self.id).count()
        else:
            return GameLaner.objects.filter(
                player__exact=self.id, lane__exact=lane.id).count()

    def getWinrateHistorical(self, maxGame, lane):
        if(lane is None):
            # Overall winrate
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id, game__gameNumber__lte=maxGame.gameNumber)
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
        else:
            # Lane winrate
            gamesPlayed = GameLaner.objects.filter(
                player__exact=self.id,
                lane__exact=lane.id,
                game__gameNumber__lte=maxGame.gameNumber)
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
        if self.getWinrate(lane) == 'N/A' or self.getLaneCount(lane) < 3:
            return None
        conf_int = stats.norm.interval(0.5, self.getWinrate(
            lane) / 100, (0.5 / np.sqrt(self.getLaneCount(lane))))
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
        totalGameCount = gamesPlayed.count()
        if totalGameCount == 0:
            return "N/A"
        winningCount = 0
        for gameLane in gamesPlayed.iterator():
            gameLane: GameLaner
            blueTeam = gameLane.blueTeam
            blueWin = gameLane.game.gameBlueWins
            if blueTeam == blueWin:
                winningCount += 1

        return round((winningCount / totalGameCount) * 100, 2)

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
        bansTargeted = GameBan.objects.filter(
            targetPlayer__exact=self.id).count()
        gamesWithBans = GameBan.objects.values('game').distinct()
        totalGameCount = gamesWithBans.count()
        if totalGameCount == 0:
            return "N/A"
        playerGamesWithBansCount = 0
        for gameBanDict in gamesWithBans:
            gameObject = Game.objects.get(id__exact=gameBanDict['game'])
            if(self.playerParticipatedInGame(gameObject)):
                playerGamesWithBansCount += 1
        return round(bansTargeted / playerGamesWithBansCount, 2)

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
        totalGameCount = gamesPlayed.count()
        if(totalGameCount == 0):
            return "N/A"
        winningCount = 0
        for gameLane in gamesPlayed.iterator():
            gameLane: GameLaner
            blueTeam = gameLane.blueTeam
            blueWin = gameLane.game.gameBlueWins
            if blueTeam == blueWin:
                winningCount += 1

        return round((winningCount / totalGameCount) * 100, 2)

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

        totalGameCount = gamesPlayed.count()
        if totalGameCount == 0:
            return "N/A"
        winningCount = 0
        for gameLane in gamesPlayed.iterator():
            gameLane: GameLaner
            blueTeam = gameLane.blueTeam
            blueWin = gameLane.game.gameBlueWins
            if blueTeam == blueWin:
                winningCount += 1

        return round((winningCount / totalGameCount) * 100, 2)

    def getSideWinrate(self, side):
        blueTeamDetermine = side == "Blue"
        gamesPlayed = GameLaner.objects.filter(
            champion__exact=self.id, blueTeam__exact=blueTeamDetermine)
        totalGameCount = gamesPlayed.count()
        if totalGameCount == 0:
            return "N/A"
        winningCount = 0
        for gameLane in gamesPlayed.iterator():
            gameLane: GameLaner
            blueTeam = gameLane.blueTeam
            blueWin = gameLane.game.gameBlueWins
            if blueTeam == blueWin:
                winningCount += 1

        return round((winningCount / totalGameCount) * 100, 2)

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

    def provideStats(self, localGame, championList, match):
        for participant in match['participants']:
            # find champ
            championDataName = championList['keys'][str(participant['championId'])]
            championTrueName = championList['data'][championDataName]['name']
            championObject = Champion.objects.filter(championName__exact=championTrueName).get()
            gameLaner = GameLaner.objects.filter(champion__exact=championObject, game__exact=localGame).get()
            # check for existing statsObject
            statsObject = GameLanerStats.objects.get(gameLaner__exact=gameLaner)
            if statsObject is not None:
                statsObject: GameLanerStats
                statsObject.gameLaner = gameLaner
                statsObject.kills = participant['stats']['kills']
                statsObject.deaths = participant['stats']['deaths']
                statsObject.assists = participant['stats']['assists']
                statsObject.largestKillingSpree = participant['stats']['largestKillingSpree']
                statsObject.largestMultiKill = participant['stats']['largestMultiKill']
                statsObject.doubleKills = participant['stats']['doubleKills']
                statsObject.tripleKills = participant['stats']['tripleKills']
                statsObject.quadraKills = participant['stats']['quadraKills']
                statsObject.pentaKills = participant['stats']['pentaKills']
                statsObject.totalDamageDealtToChampions = participant['stats']['totalDamageDealtToChampions']
                statsObject.visionScore = participant['stats']['visionScore']
                statsObject.crowdControlScore = participant['stats']['timeCCingOthers']
                statsObject.totalDamageTaken = participant['stats']['totalDamageTaken']
                statsObject.goldEarned = participant['stats']['goldEarned']
                statsObject.turretKills = participant['stats']['turretKills']
                statsObject.inhibitorKills = participant['stats']['inhibitorKills']
                statsObject.laneMinionsKilled = participant['stats']['totalMinionsKilled']
                statsObject.neutralMinionsKilled = participant['stats']['neutralMinionsKilled']
                statsObject.teamJungleMinionsKilled = participant['stats']['neutralMinionsKilledTeamJungle']
                statsObject.enemyJungleMinionsKilled = participant['stats']['neutralMinionsKilledEnemyJungle']
                statsObject.controlWardsPurchased = participant['stats']['visionWardsBoughtInGame']
                statsObject.firstBlood = participant['stats']['firstBloodKill']
                statsObject.firstTower = participant['stats']['firstTowerKill']
                statsObject.csRateFirstTen = participant['timeline']['creepsPerMinDeltas']['0-10']
                statsObject.csRateSecondTen = participant['timeline']['creepsPerMinDeltas']['10-20']
            else:
                statsObject = GameLanerStats(
                    gameLaner=gameLaner,
                    kills=participant['stats']['kills'],
                    deaths=participant['stats']['deaths'],
                    assists=participant['stats']['assists'],
                    largestKillingSpree=participant['stats']['largestKillingSpree'],
                    largestMultiKill=participant['stats']['largestMultiKill'],
                    doubleKills=participant['stats']['doubleKills'],
                    tripleKills=participant['stats']['tripleKills'],
                    quadraKills=participant['stats']['quadraKills'],
                    pentaKills=participant['stats']['pentaKills'],
                    totalDamageDealtToChampions=participant['stats']['totalDamageDealtToChampions'],
                    visionScore=participant['stats']['visionScore'],
                    crowdControlScore=participant['stats']['timeCCingOthers'],
                    totalDamageTaken=participant['stats']['totalDamageTaken'],
                    goldEarned=participant['stats']['goldEarned'],
                    turretKills=participant['stats']['turretKills'],
                    inhibitorKills=participant['stats']['inhibitorKills'],
                    laneMinionsKilled=participant['stats']['totalMinionsKilled'],
                    neutralMinionsKilled=participant['stats']['neutralMinionsKilled'],
                    teamJungleMinionsKilled=participant['stats']['neutralMinionsKilledTeamJungle'],
                    enemyJungleMinionsKilled=participant['stats']['neutralMinionsKilledEnemyJungle'],
                    controlWardsPurchased=participant['stats']['visionWardsBoughtInGame'],
                    firstBlood=participant['stats']['firstBloodKill'],
                    firstTower=participant['stats']['firstTowerKill'],
                    csRateFirstTen=participant['timeline']['creepsPerMinDeltas']['0-10'],
                    csRateSecondTen=participant['timeline']['creepsPerMinDeltas']['10-20'])
            statsObject.save()


class GameBan(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    targetPlayer = models.ForeignKey(
        Player, on_delete=models.CASCADE, null=True)
