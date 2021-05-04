import datetime
import factory
from tenMans.models import Champion, Game, GameBan, GameLaner, Lane, Player
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
