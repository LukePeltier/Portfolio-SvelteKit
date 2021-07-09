from datetime import date
from django.http.response import JsonResponse
from django.views.generic.base import ContextMixin, TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from marioGolf.models import Character, Player, Tournament, TournamentEntry, TournamentEntryHole, TournamentHole
from django.core.exceptions import ObjectDoesNotExist


class BaseMarioGolfContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMarioGolfContextMixin, self).get_context_data(*args, **kwargs)
        context['player_list'] = Player.objects.all().order_by('playerName')
        return context


class Dashboard(TemplateView, BaseMarioGolfContextMixin):
    template_name = "marioGolf/index.html"

    def get_context_data(self, **kwargs):
        today = date.today()
        context = super().get_context_data(**kwargs)
        context['currentlyRunning'] = Tournament.objects.filter(startDate__lt=today, endDate__gt=today).exists()
        context['tournamentsPlayed'] = Tournament.objects.count()
        context['registeredMembers'] = Player.objects.count()

        return context


class CharacterList(ListView, BaseMarioGolfContextMixin):
    model = Character

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CharacterDetailView(DetailView, BaseMarioGolfContextMixin):
    model = Character
    object: Character

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['charType'] = self.object.characterstats.characterType
            context['power'] = self.object.characterstats.characterPower
        except ObjectDoesNotExist:
            context['charType'] = "?"
            context['power'] = "?"

        return context


class PlayerDetailView(DetailView, BaseMarioGolfContextMixin):
    model = Player
    object: Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mostPlayedCharacter'] = self.object.getMostPlayedCharacterString()
        context['bestPerformingCharacter'] = self.object.getBestPerformingCharacterString()
        context['totalTournamentsPlayed'] = self.object.getTotalTournamentsPlayed()
        context['uniqueCharactersPlayed'] = self.object.getUniqueCharacterCount()
        context['powerRanking'] = self.object.getPowerRankingPercentage() * 100
        return context


class TournamentListView(ListView, BaseMarioGolfContextMixin):
    model = Tournament

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TournamentDetailView(DetailView, BaseMarioGolfContextMixin):
    model = Tournament
    object: Tournament

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['holes'] = TournamentHole.objects.filter(tournament__exact=self.object)
        return context


class TournamentLeaderboardTable(DetailView):
    model = Tournament

    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Tournament

        rankings = self.object.getPlacementDict()

        for name, (ranking, shotsTaken, score, characterName) in rankings.items():
            playerDict = {}
            playerDict['placement'] = ranking
            playerDict['playerName'] = name
            playerDict['character'] = characterName
            playerDict['score'] = score
            playerDict['shotsTaken'] = shotsTaken
            playerDict['playerID'] = Player.objects.filter(playerName__exact=name).first().id
            playerDict['characterID'] = Character.objects.filter(characterName__exact=characterName).first().id
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })


class PowerRankingsTable(View):

    def get(self, request, *args, **kwargs):
        data = []
        queryset = Player.objects.order_by('playerName')

        for player in queryset:
            # if(player.getTotalTournamentsPlayed() <= 0):
            #     continue
            player: Player
            playerDict = {}
            playerDict["name"] = player.playerName
            playerDict["tournamentsPlayed"] = player.getTotalTournamentsPlayed()
            playerDict["holesPlayed"] = player.getTotalHolesPlayed()
            playerDict["topPercent"] = ("N/A" if (player.getPowerRankingPercentage() is None) else round(player.getPowerRankingPercentage(None) * 100, 3))
            playerDict["topPercentAlpha"] = player.getTournamentRate()
            playerDict["playerID"] = player.id
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })


class TournamentScorecardTable(DetailView):
    model = Tournament

    def get(self, request, *args, **kwargs):
        data = []
        self.object = self.get_object()
        self.object: Tournament

        playerEntries = TournamentEntry.objects.filter(tournament__exact=self.object.id)

        for entry in playerEntries:
            entry: TournamentEntry
            playerDict = {}
            playerDict['playerName'] = entry.player.playerName
            playerDict['character'] = entry.character.characterName
            holesPlayed = TournamentHole.objects.filter(tournament__exact=self.object.id)
            for hole in holesPlayed:
                hole: TournamentHole
                holeEntry = TournamentEntryHole.objects.filter(tournamentHole__exact=hole.id, tournamentEntry__exact=entry.id).first()
                holeEntry: TournamentEntryHole
                if holeEntry is not None and holeEntry.approved:
                    playerDict['hole{}'.format(hole.order + 1)] = holeEntry.shotsTaken
                    playerDict['hole{}ParScore'.format(hole.order + 1)] = holeEntry.shotsTaken - holeEntry.tournamentHole.hole.par
                else:
                    playerDict['hole{}'.format(hole.order + 1)] = None
                    playerDict['hole{}ParScore'.format(hole.order + 1)] = None

                playerDict['hole{}Par'.format(hole.order + 1)] = holeEntry.tournamentHole.hole.par

            playerDict['playerID'] = entry.player.id
            playerDict['characterID'] = entry.character.id
            data.append(playerDict)

        return JsonResponse(data={
            'data': data
        })
