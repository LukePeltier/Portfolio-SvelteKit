from django.test import TestCase
from django.urls import reverse
from tenMans.factory import ChampionFactory, GameBanFactory, GameFactory, GameLanerFactory, GameLanerNoSupport, GameLanerRandomGameFactory, GameLanerStatsFactory, LaneFactory, PlayerFactory
from tenMans.models import Champion, Game, GameLaner, Lane, Player


class BasicViewsTest(TestCase):
    def test_dashboard_view(self):
        url = reverse("tenMansHome")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class GameTest(TestCase):

    def setUp(self):
        self.game = GameFactory()

    def test_game_creation(self):
        self.assertIsInstance(self.game, Game)
        self.assertEqual(self.game.__str__(), str(self.game.gameNumber))
        self.assertEqual(Game.getTotalGames(), 1)


class PlayerTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.lanes = []
        cls.lanes.append(LaneFactory(laneName='Top'))
        cls.lanes.append(LaneFactory(laneName='Jungle'))
        cls.lanes.append(LaneFactory(laneName='Mid'))
        cls.lanes.append(LaneFactory(laneName='Bot'))
        cls.lanes.append(LaneFactory(laneName='Support'))
        cls.games = GameFactory.create_batch(size=50)
        cls.randomGames = GameFactory.create_batch(size=50, gameRandomTeams=True)
        cls.champions = ChampionFactory.create_batch(size=100)
        cls.players = []

        # top only player
        topBluePlayer = PlayerFactory()
        GameLanerFactory.create_batch(size=20, blueTeam=True, lane=Lane.objects.get(laneName__exact="Top"), player=topBluePlayer)
        cls.players.append(topBluePlayer)

        # any lane except support
        flexRedPlayer = PlayerFactory()
        GameLanerNoSupport.create_batch(size=20, blueTeam=False, player=flexRedPlayer)
        cls.players.append(flexRedPlayer)

        # random teams guy
        randomTeamsPlayer = PlayerFactory()
        GameLanerRandomGameFactory.create_batch(size=20, blueTeam=False, player=randomTeamsPlayer, lane=Lane.objects.get(laneName__exact="Support"))
        cls.players.append(randomTeamsPlayer)

        # zero game andy
        noGames = PlayerFactory()
        cls.players.append(noGames)

        # champion one trick
        oneChampion = PlayerFactory()
        GameLanerFactory.create(blueTeam=True, lane=Lane.objects.get(laneName__exact="Mid"), champion=Champion.objects.all()[2], player=oneChampion)
        GameLanerFactory.create_batch(size=20, blueTeam=True, lane=Lane.objects.get(laneName__exact="Mid"), champion=Champion.objects.all().first(), player=oneChampion)
        GameLanerFactory.create(blueTeam=True, lane=Lane.objects.get(laneName__exact="Mid"), champion=Champion.objects.all()[1], player=oneChampion)
        cls.players.append(oneChampion)

        # target banned ommegies
        alwaysBanned = PlayerFactory()
        GameLanerFactory.create_batch(size=20, blueTeam=True, lane=Lane.objects.get(laneName__exact="Bot"), player=alwaysBanned)
        GameBanFactory.create_batch(size=20, targetPlayer=alwaysBanned)
        cls.players.append(alwaysBanned)

        # target banned for one champ ommegies
        alwaysBanned = PlayerFactory()
        GameLanerFactory.create_batch(size=20, blueTeam=True, lane=Lane.objects.get(laneName__exact="Bot"), player=alwaysBanned)
        GameBanFactory.create(targetPlayer=alwaysBanned, champion=Champion.objects.all()[2])
        GameBanFactory.create_batch(size=20, targetPlayer=alwaysBanned, champion=Champion.objects.all().first())
        GameBanFactory.create(targetPlayer=alwaysBanned, champion=Champion.objects.all()[1])
        cls.players.append(alwaysBanned)

        cls.gameLaners = GameLaner.objects.all()
        for gl in cls.gameLaners:
            GameLanerStatsFactory(gameLaner=gl)

        cls.allGames = Game.objects.all()

        cls.lanesLists = []
        cls.lanesLists.append(None)
        cls.lanesLists.append([Lane.objects.get(laneName__exact="Top")])
        cls.lanesLists.append([Lane.objects.get(laneName__exact="Jungle")])
        cls.lanesLists.append([Lane.objects.get(laneName__exact="Mid")])
        cls.lanesLists.append([Lane.objects.get(laneName__exact="Bot"), Lane.objects.get(laneName__exact="Support")])

    def test_player_creation(self):
        for player in self.players:
            self.assertIsInstance(player, Player)
            self.assertEqual(player.__str__(), player.playerName)

    def test_player_winrate(self):
        for player in self.players:
            player.getWinrate(None)

            for lane in self.lanes:
                player.getWinrate(lane)

    def test_player_lanecount(self):
        for player in self.players:
            player.getLaneCount(None)

            for lane in self.lanes:
                player.getLaneCount(lane)

    def test_player_averagedraftorder(self):
        for player in self.players:
            player.getAverageDraftOrder()

    def test_player_minconfidencewinrate(self):
        for player in self.players:
            player.getMinConfidenceWinrate(None)

            for lane in self.lanes:
                player.getMinConfidenceWinrate(lane)

    def test_player_mostplayedlanestring(self):
        for player in self.players:
            player.getMostPlayedLaneString()

    def test_player_winratehistorical(self):
        for player in self.players:
            for game in self.allGames:
                player.getWinrateHistorical(game, None)

                for lane in self.lanes:
                    player.getWinrateHistorical(game, lane)

    def test_player_lanerate(self):
        for player in self.players:
            for lane in self.lanes:
                player.getLaneRate(lane)

    def test_player_mostplayedchampionstring(self):
        for player in self.players:
            player.getMostPlayedChampionString()

    def test_player_getwinrateonchampion(self):
        for player in self.players:
            for champion in Champion.objects.all():
                player.getWinrateOnChampion(champion)

    def test_player_gethighestwinratechampionstring(self):
        for player in self.players:
            player.getHighestWinrateChampionString()

    def test_player_participatedingame(self):
        for player in self.players:
            for game in self.allGames:
                player.playerParticipatedInGame(game)

    def test_player_getaveragepulledbans(self):
        for player in self.players:
            player.getAveragePulledBans()

    def test_player_getmostbannedchampionstring(self):
        for player in self.players:
            player.getMostBannedChampionString()

    def test_player_getSideWinrate(self):
        for player in self.players:
            for side in ["Blue", "Red"]:
                player.getSideWinrate(side)

    def test_player_getAverageKDALaneString(self):
        for player in self.players:
            player.getAverageKDALaneString(None)
            for lane in self.lanes:
                player.getAverageKDALaneString(lane)

    def test_player_getAverageKDAChampionString(self):
        for player in self.players:
            player.getAverageKDAChampionString(None)
            for champion in self.champions:
                player.getAverageKDAChampionString(champion)

    def test_player_getUniqueChampionCount(self):
        for player in self.players:
            player.getUniqueChampionCount()

    def test_player_getMatchupWinrate(self):
        for player in self.players:
            for secondPlayer in self.players:
                if player == secondPlayer:
                    continue
                for lane in self.lanesLists:
                    player.getMatchupWinrate(secondPlayer, lane)

    def test_player_getDuoWinrate(self):
        for player in self.players:
            for secondPlayer in self.players:
                if player == secondPlayer:
                    continue
                player.getDuoWinrate(secondPlayer)

    def test_player_getHighestKillCountGameLaneStats(self):
        for player in self.players:
            player.getHighestKillCountGameLaneStats(None)
            for lane in self.lanes:
                player.getHighestKillCountGameLaneStats(lane)

    def test_player_getHighestDeathCountGameLaneStats(self):
        for player in self.players:
            player.getHighestDeathCountGameLaneStats(None)
            for lane in self.lanes:
                player.getHighestDeathCountGameLaneStats(lane)

    def test_player_getHighestAssistCountGameLaneStats(self):
        for player in self.players:
            player.getHighestAssistCountGameLaneStats(None)
            for lane in self.lanes:
                player.getHighestAssistCountGameLaneStats(lane)
