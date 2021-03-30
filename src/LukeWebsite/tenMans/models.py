from django.db import models

# Create your models here.
class Game(models.Model):
    gameNumber = models.PositiveIntegerField(unique=True)
    gameBlueWins = models.BooleanField()
    gameRandomTeams = models.BooleanField()
    gameMemeStatus = models.BooleanField(default=0)
    gameDate = models.DateTimeField(default='current_timestamp()')

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
        if(lane is None):
            topPlayer = Player.objects.all().annotate(num_games=models.Count('gamelaner')).order_by('num_games').first()
            topNumber = topPlayer.num_games
            playerNumber = GameLaner.objects.filter(player__exact=self.id).count()
            laneRate = round(playerNumber/topNumber, 1)




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