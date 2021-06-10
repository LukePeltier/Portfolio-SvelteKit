from django.views.generic.base import ContextMixin, TemplateView
# from marioGolf.models import Player, Game


class BaseMarioGolfContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMarioGolfContextMixin, self).get_context_data(*args, **kwargs)
        # context['player_list'] = Player.objects.all().order_by('playerName')
        return context


class Dashboard(TemplateView, BaseMarioGolfContextMixin):
    template_name = "marioGolf/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['gameTotal'] = Game.objects.all().count()
        # context['memeTotal'] = Game.objects.all().filter(gameMemeStatus=True).count()
        return context
