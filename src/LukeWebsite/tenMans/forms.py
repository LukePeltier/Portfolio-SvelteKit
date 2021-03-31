from django import forms

from tenMans.models import Champion, Lane

class NewGameForm(forms.Form):
    didBlueWin = forms.BooleanField(label="Did Blue Win?")
    randomTeams = forms.BooleanField(label="Random Teams")
    memeGame = forms.BooleanField()
    gameDate = forms.DateTimeField()

    blueTopLaner = forms.CharField()
    blueJungLaner = forms.CharField()
    blueMidLaner = forms.CharField()
    blueBotLaner = forms.CharField()
    blueSuppLaner = forms.CharField()

    redTopLaner = forms.CharField()
    redJungLaner = forms.CharField()
    redMidLaner = forms.CharField()
    redBotLaner = forms.CharField()
    redSuppLaner = forms.CharField()

    bluePlayerPick1 = forms.ModelChoiceField(queryset=Lane.objects.all())
    bluePlayerPick2 = forms.ModelChoiceField(queryset=Lane.objects.all())
    bluePlayerPick3 = forms.ModelChoiceField(queryset=Lane.objects.all())
    bluePlayerPick4 = forms.ModelChoiceField(queryset=Lane.objects.all())
    bluePlayerPick5 = forms.ModelChoiceField(queryset=Lane.objects.all())

    redPlayerPick1 = forms.ModelChoiceField(queryset=Lane.objects.all())
    redPlayerPick2 = forms.ModelChoiceField(queryset=Lane.objects.all())
    redPlayerPick3 = forms.ModelChoiceField(queryset=Lane.objects.all())
    redPlayerPick4 = forms.ModelChoiceField(queryset=Lane.objects.all())
    redPlayerPick5 = forms.ModelChoiceField(queryset=Lane.objects.all())

    blueTopChamp = forms.ModelChoiceField(queryset=Champion.objects.all())
    blueJungChamp = forms.ModelChoiceField(queryset=Champion.objects.all())
    blueMidChamp = forms.ModelChoiceField(queryset=Champion.objects.all())
    blueBotChamp = forms.ModelChoiceField(queryset=Champion.objects.all())
    blueSuppChamp = forms.ModelChoiceField(queryset=Champion.objects.all())

    redTopChamp = forms.ModelChoiceField(queryset=Champion.objects.all())
    redJungChamp = forms.ModelChoiceField(queryset=Champion.objects.all())
    redMidChamp = forms.ModelChoiceField(queryset=Champion.objects.all())
    redBotChamp = forms.ModelChoiceField(queryset=Champion.objects.all())
    redSuppChamp = forms.ModelChoiceField(queryset=Champion.objects.all())

    blueChampPick1 = forms.ModelChoiceField(queryset=Lane.objects.all())
    blueChampPick2 = forms.ModelChoiceField(queryset=Lane.objects.all())
    blueChampPick3 = forms.ModelChoiceField(queryset=Lane.objects.all())
    blueChampPick4 = forms.ModelChoiceField(queryset=Lane.objects.all())
    blueChampPick5 = forms.ModelChoiceField(queryset=Lane.objects.all())

    redChampPick1 = forms.ModelChoiceField(queryset=Lane.objects.all())
    redChampPick2 = forms.ModelChoiceField(queryset=Lane.objects.all())
    redChampPick3 = forms.ModelChoiceField(queryset=Lane.objects.all())
    redChampPick4 = forms.ModelChoiceField(queryset=Lane.objects.all())
    redChampPick5 = forms.ModelChoiceField(queryset=Lane.objects.all())

    blueBan1 = forms.ModelChoiceField(queryset=Champion.objects.all())
    blueBan2 = forms.ModelChoiceField(queryset=Champion.objects.all())
    blueBan3 = forms.ModelChoiceField(queryset=Champion.objects.all())
    blueBan4 = forms.ModelChoiceField(queryset=Champion.objects.all())
    blueBan5 = forms.ModelChoiceField(queryset=Champion.objects.all())

    redBan1 = forms.ModelChoiceField(queryset=Champion.objects.all())
    redBan2 = forms.ModelChoiceField(queryset=Champion.objects.all())
    redBan3 = forms.ModelChoiceField(queryset=Champion.objects.all())
    redBan4 = forms.ModelChoiceField(queryset=Champion.objects.all())
    redBan5 = forms.ModelChoiceField(queryset=Champion.objects.all())

    blueTargetBan1 = forms.CharField()
    blueTargetBan2 = forms.CharField()
    blueTargetBan3 = forms.CharField()
    blueTargetBan4 = forms.CharField()
    blueTargetBan5 = forms.CharField()

    redTargetBan1 = forms.CharField()
    redTargetBan2 = forms.CharField()
    redTargetBan3 = forms.CharField()
    redTargetBan4 = forms.CharField()
    redTargetBan5 = forms.CharField()

    password = forms.CharField(widget = forms.PasswordInput())

    def submit_game(self, form):
        pass