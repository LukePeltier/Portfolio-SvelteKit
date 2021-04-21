from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from mixer.backend.django import mixer

from tenMans.models import Champion, Game, GameLaner, Lane, Player


class BasicViewsTest(TestCase):
    def test_dashboard_view(self):
        url = reverse("tenMansHome")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class GameTest(TestCase):

    def setUp(self):
        self.game = mixer.blend('tenMans.Game', gameDate=timezone.now())

    def test_game_creation(self):
        self.assertIsInstance(self.game, Game)
        self.assertEqual(self.game.__str__(), str(self.game.gameNumber))
        self.assertEqual(Game.getTotalGames(), 1)


class PlayerTest(TestCase):
    player: Player
    playerZero: Player
    playerTop: Player
    playerJungle: Player
    playerMid: Player
    playerBot: Player
    playerSupport: Player
    playerRandom: Player

    def setUp(self):

        self.player = mixer.blend('tenMans.Player')
        self.playerZero = mixer.blend('tenMans.Player')
        self.playerTop = mixer.blend('tenMans.Player')
        self.playerJungle = mixer.blend('tenMans.Player')
        self.playerMid = mixer.blend('tenMans.Player')
        self.playerBot = mixer.blend('tenMans.Player')
        self.playerSupport = mixer.blend('tenMans.Player')
        self.playerRandom = mixer.blend('tenMans.Player')

        self.lanes = mixer.cycle(5).blend(Lane, laneName=(name for name in ('Top', 'Jungle', 'Mid', 'Bot', 'Support')))
        self.champions = mixer.cycle(3).blend(Champion, championName=mixer.sequence(lambda c: "champion_%s" % c))

        self.games = mixer.cycle(20).blend(Game, gameDate=timezone.now(), gameBlueWins=mixer.RANDOM)
        self.gameLaners = mixer.cycle(20).blend(GameLaner, blueTeam=mixer.RANDOM, champion=mixer.RANDOM(self.champions), lane=mixer.SELECT, game=(game for game in self.games), player=self.player)

        self.topGames = mixer.cycle(4).blend(Game, gameDate=timezone.now(), gameBlueWins=mixer.RANDOM)
        self.gameLanersTop = mixer.cycle(4).blend(GameLaner, blueTeam=mixer.RANDOM, champion=mixer.RANDOM(self.champions), lane=Lane.objects.filter(laneName="Top").get(), game=(game for game in self.topGames), player=self.playerTop)

        self.jungleGames = mixer.cycle(4).blend(Game, gameDate=timezone.now(), gameBlueWins=mixer.RANDOM)
        self.gameLanersJungle = mixer.cycle(4).blend(GameLaner, blueTeam=mixer.RANDOM, champion=mixer.RANDOM(self.champions), lane=Lane.objects.filter(laneName="Jungle").get(), game=(game for game in self.jungleGames), player=self.playerJungle)

        self.midGames = mixer.cycle(4).blend(Game, gameDate=timezone.now(), gameBlueWins=mixer.RANDOM)
        self.gameLanersMid = mixer.cycle(4).blend(GameLaner, blueTeam=mixer.RANDOM, champion=mixer.RANDOM(self.champions), lane=Lane.objects.filter(laneName="Mid").get(), game=(game for game in self.midGames), player=self.playerMid)

        self.botGames = mixer.cycle(4).blend(Game, gameDate=timezone.now(), gameBlueWins=mixer.RANDOM)
        self.gameLanersBot = mixer.cycle(4).blend(GameLaner, blueTeam=mixer.RANDOM, champion=mixer.RANDOM(self.champions), lane=Lane.objects.filter(laneName="Bot").get(), game=(game for game in self.botGames), player=self.playerBot)

        self.supportGames = mixer.cycle(4).blend(Game, gameDate=timezone.now(), gameBlueWins=mixer.RANDOM)
        self.gameLanersSupport = mixer.cycle(4).blend(GameLaner, blueTeam=mixer.RANDOM, champion=mixer.RANDOM(self.champions), lane=Lane.objects.filter(laneName="Support").get(), game=(game for game in self.supportGames), player=self.playerSupport)

        self.randomGames = mixer.cycle(4).blend(Game, gameDate=timezone.now(), gameBlueWins=mixer.RANDOM)
        self.gameLanersRandom = mixer.cycle(4).blend(GameLaner, blueTeam=mixer.RANDOM, champion=mixer.RANDOM(self.champions), lane=mixer.SELECT, game=(game for game in self.randomGames), draftOrder=None, player=self.playerRandom)

        self.allGames = Game.objects.all()

    def test_player_creation(self):
        self.assertIsInstance(self.player, Player)
        self.assertEqual(self.player.__str__(), self.player.playerName)

    def test_player_winrate(self):
        self.player.getWinrate(None)
        self.playerZero.getWinrate(None)
        self.playerTop.getWinrate(None)
        self.playerJungle.getWinrate(None)
        self.playerMid.getWinrate(None)
        self.playerBot.getWinrate(None)
        self.playerSupport.getWinrate(None)

        for lane in self.lanes:
            self.player.getWinrate(lane)
            self.playerZero.getWinrate(lane)
            self.playerTop.getWinrate(lane)
            self.playerJungle.getWinrate(lane)
            self.playerMid.getWinrate(lane)
            self.playerBot.getWinrate(lane)
            self.playerSupport.getWinrate(lane)

    def test_player_lanecount(self):
        self.player.getLaneCount(None)
        self.playerZero.getLaneCount(None)
        self.playerTop.getLaneCount(None)
        self.playerJungle.getLaneCount(None)
        self.playerMid.getLaneCount(None)
        self.playerBot.getLaneCount(None)
        self.playerSupport.getLaneCount(None)

        for lane in self.lanes:
            self.player.getLaneCount(lane)
            self.playerZero.getLaneCount(lane)
            self.playerTop.getLaneCount(lane)
            self.playerJungle.getLaneCount(lane)
            self.playerMid.getLaneCount(lane)
            self.playerBot.getLaneCount(lane)
            self.playerSupport.getLaneCount(lane)

    def test_player_averagedraftorder(self):
        self.player.getAverageDraftOrder()
        self.playerZero.getAverageDraftOrder()
        self.playerTop.getAverageDraftOrder()
        self.playerJungle.getAverageDraftOrder()
        self.playerMid.getAverageDraftOrder()
        self.playerBot.getAverageDraftOrder()
        self.playerSupport.getAverageDraftOrder()
        self.playerRandom.getAverageDraftOrder()

    def test_player_minconfidencewinrate(self):
        self.player.getMinConfidenceWinrate(None)
        self.playerZero.getMinConfidenceWinrate(None)
        self.playerTop.getMinConfidenceWinrate(None)
        self.playerJungle.getMinConfidenceWinrate(None)
        self.playerMid.getMinConfidenceWinrate(None)
        self.playerBot.getMinConfidenceWinrate(None)
        self.playerSupport.getMinConfidenceWinrate(None)

        for lane in self.lanes:
            self.player.getMinConfidenceWinrate(lane)
            self.playerZero.getMinConfidenceWinrate(lane)
            self.playerTop.getMinConfidenceWinrate(lane)
            self.playerJungle.getMinConfidenceWinrate(lane)
            self.playerMid.getMinConfidenceWinrate(lane)
            self.playerBot.getMinConfidenceWinrate(lane)
            self.playerSupport.getMinConfidenceWinrate(lane)

    def test_player_mostplayedlanestring(self):
        self.player.getMostPlayedLaneString()
        self.playerZero.getMostPlayedLaneString()
        self.playerTop.getMostPlayedLaneString()
        self.playerJungle.getMostPlayedLaneString()
        self.playerMid.getMostPlayedLaneString()
        self.playerBot.getMostPlayedLaneString()
        self.playerSupport.getMostPlayedLaneString()

    def test_player_winratehistorical(self):
        for game in self.allGames:
            self.player.getWinrateHistorical(game, None)
            self.playerZero.getWinrateHistorical(game, None)
            self.playerTop.getWinrateHistorical(game, None)
            self.playerJungle.getWinrateHistorical(game, None)
            self.playerMid.getWinrateHistorical(game, None)
            self.playerBot.getWinrateHistorical(game, None)
            self.playerSupport.getWinrateHistorical(game, None)

            for lane in self.lanes:
                self.player.getWinrateHistorical(game, lane)
                self.playerZero.getWinrateHistorical(game, lane)
                self.playerTop.getWinrateHistorical(game, lane)
                self.playerJungle.getWinrateHistorical(game, lane)
                self.playerMid.getWinrateHistorical(game, lane)
                self.playerBot.getWinrateHistorical(game, lane)
                self.playerSupport.getWinrateHistorical(game, lane)

    def test_player_lanerate(self):
        for lane in self.lanes:
            self.player.getLaneRate(lane)
            self.playerZero.getLaneRate(lane)
            self.playerTop.getLaneRate(lane)
            self.playerJungle.getLaneRate(lane)
            self.playerMid.getLaneRate(lane)
            self.playerBot.getLaneRate(lane)
            self.playerSupport.getLaneRate(lane)

    def test_player_mostplayedchampionstring(self):
        self.player.getMostPlayedChampionString()
        self.playerZero.getMostPlayedChampionString()
        self.playerTop.getMostPlayedChampionString()
        self.playerJungle.getMostPlayedChampionString()
        self.playerMid.getMostPlayedChampionString()
        self.playerBot.getMostPlayedChampionString()
        self.playerSupport.getMostPlayedChampionString()

    def test_player_getwinrateonchampion(self):
        for champion in Champion.objects.all():
            self.player.getWinrateOnChampion(champion)
            self.playerZero.getWinrateOnChampion(champion)
            self.playerTop.getWinrateOnChampion(champion)
            self.playerJungle.getWinrateOnChampion(champion)
            self.playerMid.getWinrateOnChampion(champion)
            self.playerBot.getWinrateOnChampion(champion)
            self.playerSupport.getWinrateOnChampion(champion)
