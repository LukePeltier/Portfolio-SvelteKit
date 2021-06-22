from django.views.generic.base import ContextMixin, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from marioGolf.models import Character, Player
from django.core.exceptions import ObjectDoesNotExist


class BaseMarioGolfContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMarioGolfContextMixin, self).get_context_data(*args, **kwargs)
        context['player_list'] = Player.objects.all().order_by('playerName')
        return context


class Dashboard(TemplateView, BaseMarioGolfContextMixin):
    template_name = "marioGolf/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
