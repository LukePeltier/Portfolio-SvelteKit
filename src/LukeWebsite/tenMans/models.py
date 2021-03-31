from django.db import models
from django.db.models.query_utils import Q

# Create your models here.
class Game(models.Model):
    gameNumber = models.PositiveIntegerField(unique=True)
    gameBlueWins = models.BooleanField()
    gameRandomTeams = models.BooleanField()
    gameMemeStatus = models.BooleanField(default=0)
    gameDate = models.DateTimeField(default='current_timestamp()')
    def getTotalGames():
        return Game.objects.all().count()

    class Meta:
        ordering = ["gameNumber"]
        verbose_name_plural = "games"

class Player(models.Model):
    playerName = models.TextField(unique=True)

    def getWinrate(self, lane):
        if(lane is None):
            #Overall winrate
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id)
            totalGameCount = gamesPlayed.count()
            winningCount = 0
            for gameLane in gamesPlayed.iterator():
                gameLane: GameLaner
                blueTeam = gameLane.blueTeam
                blueWin = gameLane.game.gameBlueWins
                if(blueTeam==blueWin):
                    winningCount+=1

            return round((winningCount/totalGameCount)*100, 2)
        else:
            #Lane winrate
            gamesPlayed = GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id)
            totalGameCount = gamesPlayed.count()
            if totalGameCount==0:
                return "N/A"
            winningCount = 0
            for gameLane in gamesPlayed.iterator():
                gameLane: GameLaner
                blueTeam = gameLane.blueTeam
                blueWin = gameLane.game.gameBlueWins
                if(blueTeam==blueWin):
                    winningCount+=1

            return round((winningCount/totalGameCount)*100, 2)
    def getLaneRate(self, lane):
            players = Player.objects.all()
            topNumber = 0
            for player in players:
                count = player.getLaneCount(lane)
                if(count>topNumber):
                    topNumber = count
            playerNumber = self.getLaneCount(lane)
            return round(playerNumber/topNumber, 1)

    def getLaneCount(self, lane):
        if(lane is None):
            return GameLaner.objects.filter(player__exact=self.id).count()
        else:
            return GameLaner.objects.filter(player__exact=self.id, lane__exact=lane.id).count()




class Champion(models.Model):
    championName = models.TextField(unique=True)

class Lane(models.Model):
    laneName = models.TextField(unique=True)

class GameLaner(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    lane = models.ForeignKey(Lane, on_delete=models.CASCADE)
    blueTeam = models.BooleanField(default=1)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    draftOrder = models.PositiveIntegerField(null=True)
    championSelectOrder = models.PositiveIntegerField(null=True)

    class Meta:
        unique_together = (('game', 'lane', 'blueTeam'))

class GameBan(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    targetPlayer = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)