import datetime
import factory
from tenMans.models import Champion, Game, GameBan, GameLaner, GameLanerStats, Lane, Player
import factory.fuzzy
from dateutil import tz


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    gameNumber = factory.Sequence(lambda n: '%d' % n)
    gameDate = factory.fuzzy.FuzzyDateTime(datetime.datetime(2020, 6, 1, tzinfo=tz.gettz('US/Central')))
    gameBlueWins = factory.fuzzy.FuzzyChoice([True, False])
    gameRandomTeams = False
    gameMemeStatus = False
    gameDuration = factory.fuzzy.FuzzyInteger(1, 3600)


class LaneFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lane


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Player

    playerName = factory.Faker('name')


class ChampionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Champion

    championName = factory.fuzzy.FuzzyText()


class GameLanerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GameLaner

    game = factory.Iterator(Game.objects.all())
    lane = factory.Iterator(Lane.objects.all())
    blueTeam = factory.fuzzy.FuzzyChoice([True, False])
    player = factory.Iterator(Player.objects.all())
    champion = factory.Iterator(Champion.objects.all())
    draftOrder = factory.fuzzy.FuzzyChoice([None, 1, 2, 3, 4, 5, 6, 7, 8])
    championSelectOrder = factory.fuzzy.FuzzyChoice([None, 1, 2, 3, 4, 5, 6, 7])


class GameLanerNoSupport(GameLanerFactory):
    lane = factory.Iterator(Lane.objects.exclude(laneName__exact="Support"))


class GameLanerRandomGameFactory(GameLanerFactory):
    class Meta:
        model = GameLaner

    game = factory.Iterator(Game.objects.filter(gameRandomTeams=True))
    draftOrder = None


class GameBanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GameBan

    game = factory.Iterator(Game.objects.filter(gameRandomTeams=False))
    champion = factory.Iterator(Champion.objects.all())


class GameLanerStatsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = GameLanerStats

    kills = factory.fuzzy.FuzzyInteger(0)
    deaths = factory.fuzzy.FuzzyInteger(0)
    assists = factory.fuzzy.FuzzyInteger(0)

    largestKillingSpree = factory.fuzzy.FuzzyInteger(0)
    largestMultiKill = factory.fuzzy.FuzzyInteger(0)
    doubleKills = factory.fuzzy.FuzzyInteger(0)
    tripleKills = factory.fuzzy.FuzzyInteger(0)
    quadraKills = factory.fuzzy.FuzzyInteger(0)
    pentaKills = factory.fuzzy.FuzzyInteger(0)

    totalDamageDealtToChampions = factory.fuzzy.FuzzyInteger(0)
    visionScore = factory.fuzzy.FuzzyInteger(0)
    crowdControlScore = factory.fuzzy.FuzzyInteger(0)
    totalDamageTaken = factory.fuzzy.FuzzyInteger(0)
    goldEarned = factory.fuzzy.FuzzyInteger(0)

    turretKills = factory.fuzzy.FuzzyInteger(0)
    inhibitorKills = factory.fuzzy.FuzzyInteger(0)

    laneMinionsKilled = factory.fuzzy.FuzzyInteger(0)
    neutralMinionsKilled = factory.fuzzy.FuzzyInteger(0)

    teamJungleMinionsKilled = factory.fuzzy.FuzzyInteger(0)
    enemyJungleMinionsKilled = factory.fuzzy.FuzzyInteger(0)

    controlWardsPurchased = factory.fuzzy.FuzzyInteger(0)

    firstBlood = factory.fuzzy.FuzzyChoice([True, False])
    firstTower = factory.fuzzy.FuzzyChoice([True, False])

    csRateFirstTen = factory.fuzzy.FuzzyFloat(0, 10, 2)
    csRateSecondTen = factory.fuzzy.FuzzyFloat(0, 10, 2)
