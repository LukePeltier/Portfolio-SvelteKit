from bootstrap_datepicker_plus import DateTimePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (ButtonHolder, Column, Fieldset, Layout, Row,
                                 Submit)
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db.models import Max
from django_cassiopeia import cassiopeia as cass

from tenMans.models import (Champion, Game, GameBan, GameLaner, GameLanerStats,
                            Lane, Player)


class NewGameForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())

    didBlueWin = forms.BooleanField(label="Did Blue Win?", required=False)
    randomTeams = forms.BooleanField(label="Random Teams", required=False)
    memeGame = forms.BooleanField(label="Meme Game", required=False)
    gameDate = forms.DateTimeField(label="Date of Game", widget=DateTimePickerInput())
    remoteGameID = forms.IntegerField(label="Riot Game ID", widget=forms.TextInput, required=False)

    blueTopLaner = forms.ModelChoiceField(label="Blue Top Laner", queryset=Player.objects.all().order_by('playerName'))
    blueJungLaner = forms.ModelChoiceField(label="Blue Jungler", queryset=Player.objects.all().order_by('playerName'))
    blueMidLaner = forms.ModelChoiceField(label="Blue Mid Laner", queryset=Player.objects.all().order_by('playerName'))
    blueBotLaner = forms.ModelChoiceField(label="Blue Bot Laner", queryset=Player.objects.all().order_by('playerName'))
    blueSuppLaner = forms.ModelChoiceField(label="Blue Support", queryset=Player.objects.all().order_by('playerName'))

    redTopLaner = forms.ModelChoiceField(label="Red Top Laner", queryset=Player.objects.all().order_by('playerName'))
    redJungLaner = forms.ModelChoiceField(label="Red Jungler", queryset=Player.objects.all().order_by('playerName'))
    redMidLaner = forms.ModelChoiceField(label="Red Mid Laner", queryset=Player.objects.all().order_by('playerName'))
    redBotLaner = forms.ModelChoiceField(label="Red Bot Laner", queryset=Player.objects.all().order_by('playerName'))
    redSuppLaner = forms.ModelChoiceField(label="Red Support", queryset=Player.objects.all().order_by('playerName'))

    bluePlayerPickTop = forms.CharField(label="Player Pick", max_length=1, required=False)
    bluePlayerPickJung = forms.CharField(label="Player Pick", max_length=1, required=False)
    bluePlayerPickMid = forms.CharField(label="Player Pick", max_length=1, required=False)
    bluePlayerPickBot = forms.CharField(label="Player Pick", max_length=1, required=False)
    bluePlayerPickSupp = forms.CharField(label="Player Pick", max_length=1, required=False)

    redPlayerPickTop = forms.CharField(label="Player Pick", max_length=1, required=False)
    redPlayerPickJung = forms.CharField(label="Player Pick", max_length=1, required=False)
    redPlayerPickMid = forms.CharField(label="Player Pick", max_length=1, required=False)
    redPlayerPickBot = forms.CharField(label="Player Pick", max_length=1, required=False)
    redPlayerPickSupp = forms.CharField(label="Player Pick", max_length=1, required=False)

    blueTopChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))
    blueJungChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))
    blueMidChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))
    blueBotChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))
    blueSuppChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))

    redTopChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))
    redJungChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))
    redMidChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))
    redBotChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))
    redSuppChamp = forms.ModelChoiceField(label="Champion", queryset=Champion.objects.all().order_by('championName'))

    blueChampPickTop = forms.CharField(label="Champ Pick", max_length=1)
    blueChampPickJung = forms.CharField(label="Champ Pick", max_length=1)
    blueChampPickMid = forms.CharField(label="Champ Pick", max_length=1)
    blueChampPickBot = forms.CharField(label="Champ Pick", max_length=1)
    blueChampPickSupp = forms.CharField(label="Champ Pick", max_length=1)

    redChampPickTop = forms.CharField(label="Champ Pick", max_length=1)
    redChampPickJung = forms.CharField(label="Champ Pick", max_length=1)
    redChampPickMid = forms.CharField(label="Champ Pick", max_length=1)
    redChampPickBot = forms.CharField(label="Champ Pick", max_length=1)
    redChampPickSupp = forms.CharField(label="Champ Pick", max_length=1)

    blueBan1 = forms.ModelChoiceField(label="Blue Ban 1", queryset=Champion.objects.all().order_by('championName'))
    blueBan2 = forms.ModelChoiceField(label="Blue Ban 2", queryset=Champion.objects.all().order_by('championName'))
    blueBan3 = forms.ModelChoiceField(label="Blue Ban 3", queryset=Champion.objects.all().order_by('championName'))
    blueBan4 = forms.ModelChoiceField(label="Blue Ban 4", queryset=Champion.objects.all().order_by('championName'))
    blueBan5 = forms.ModelChoiceField(label="Blue Ban 5", queryset=Champion.objects.all().order_by('championName'))

    redBan1 = forms.ModelChoiceField(label="Red Ban 1", queryset=Champion.objects.all().order_by('championName'))
    redBan2 = forms.ModelChoiceField(label="Red Ban 2", queryset=Champion.objects.all().order_by('championName'))
    redBan3 = forms.ModelChoiceField(label="Red Ban 3", queryset=Champion.objects.all().order_by('championName'))
    redBan4 = forms.ModelChoiceField(label="Red Ban 4", queryset=Champion.objects.all().order_by('championName'))
    redBan5 = forms.ModelChoiceField(label="Red Ban 5", queryset=Champion.objects.all().order_by('championName'))

    blueTargetBan1 = forms.ModelChoiceField(label="Blue Ban 1 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))
    blueTargetBan2 = forms.ModelChoiceField(label="Blue Ban 2 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))
    blueTargetBan3 = forms.ModelChoiceField(label="Blue Ban 3 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))
    blueTargetBan4 = forms.ModelChoiceField(label="Blue Ban 4 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))
    blueTargetBan5 = forms.ModelChoiceField(label="Blue Ban 5 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))

    redTargetBan1 = forms.ModelChoiceField(label="Red Ban 1 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))
    redTargetBan2 = forms.ModelChoiceField(label="Red Ban 2 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))
    redTargetBan3 = forms.ModelChoiceField(label="Red Ban 3 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))
    redTargetBan4 = forms.ModelChoiceField(label="Red Ban 4 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))
    redTargetBan5 = forms.ModelChoiceField(label="Red Ban 5 Target Player", required=False, queryset=Player.objects.all().order_by('playerName'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-newGameForm'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            Fieldset(
                'Password',
                Row(
                    Column('password', css_class='col-2')
                )
            ),
            Fieldset(
                'Basic Game Info',
                Row(
                    Column('didBlueWin', css_class='col-xs-4'),
                    Column('randomTeams', css_class='col-xs-4'),
                    Column('memeGame', css_class='col-xs-4')
                ),
                Row(
                    Column('gameDate', css_class='col-2')
                ),
                Row(
                    Column('remoteGameID', css_class='col-2')
                ),
            ),
            Fieldset(
                'Players/Champions<br><small><i>C for Captain, blank for random teams</i></small>',
                Row(
                    Column(
                        Row(
                            Column('blueTopLaner', css_class='col-3'),
                            Column('bluePlayerPickTop', css_class='col-3'),
                            Column('blueTopChamp', css_class='col-3'),
                            Column('blueChampPickTop', css_class='col-3'),
                        ),
                        Row(
                            Column('blueJungLaner', css_class='col-3'),
                            Column('bluePlayerPickJung', css_class='col-3'),
                            Column('blueJungChamp', css_class='col-3'),
                            Column('blueChampPickJung', css_class='col-3'),
                        ),
                        Row(
                            Column('blueMidLaner', css_class='col-3'),
                            Column('bluePlayerPickMid', css_class='col-3'),
                            Column('blueMidChamp', css_class='col-3'),
                            Column('blueChampPickMid', css_class='col-3'),
                        ),
                        Row(
                            Column('blueBotLaner', css_class='col-3'),
                            Column('bluePlayerPickBot', css_class='col-3'),
                            Column('blueBotChamp', css_class='col-3'),
                            Column('blueChampPickBot', css_class='col-3'),
                        ),
                        Row(
                            Column('blueSuppLaner', css_class='col-3'),
                            Column('bluePlayerPickSupp', css_class='col-3'),
                            Column('blueSuppChamp', css_class='col-3'),
                            Column('blueChampPickSupp', css_class='col-3'),
                        ),
                        css_class='col-xl-6 border-end border-5'
                    ),
                    Column(
                        Row(
                            Column('redTopLaner', css_class='col-3'),
                            Column('redPlayerPickTop', css_class='col-3'),
                            Column('redTopChamp', css_class='col-3'),
                            Column('redChampPickTop', css_class='col-3'),
                        ),
                        Row(
                            Column('redJungLaner', css_class='col-3'),
                            Column('redPlayerPickJung', css_class='col-3'),
                            Column('redJungChamp', css_class='col-3'),
                            Column('redChampPickJung', css_class='col-3'),
                        ),
                        Row(
                            Column('redMidLaner', css_class='col-3'),
                            Column('redPlayerPickMid', css_class='col-3'),
                            Column('redMidChamp', css_class='col-3'),
                            Column('redChampPickMid', css_class='col-3'),
                        ),
                        Row(
                            Column('redBotLaner', css_class='col-3'),
                            Column('redPlayerPickBot', css_class='col-3'),
                            Column('redBotChamp', css_class='col-3'),
                            Column('redChampPickBot', css_class='col-3'),
                        ),
                        Row(
                            Column('redSuppLaner', css_class='col-3'),
                            Column('redPlayerPickSupp', css_class='col-3'),
                            Column('redSuppChamp', css_class='col-3'),
                            Column('redChampPickSupp', css_class='col-3'),
                        ),
                        css_class='col-xl-6'
                    ),
                )
            ),
            Fieldset(
                'Champion Bans',
                Row(
                    Column('blueBan1', css_class='col-3'),
                    Column('blueTargetBan1', css_class='col-3 border-end border-5'),
                    Column('redBan1', css_class='col-3'),
                    Column('redTargetBan1', css_class='col-3'),
                ),
                Row(
                    Column('blueBan2', css_class='col-3'),
                    Column('blueTargetBan2', css_class='col-3 border-end border-5'),
                    Column('redBan2', css_class='col-3'),
                    Column('redTargetBan2', css_class='col-3'),
                ),
                Row(
                    Column('blueBan3', css_class='col-3'),
                    Column('blueTargetBan3', css_class='col-3 border-end border-5'),
                    Column('redBan3', css_class='col-3'),
                    Column('redTargetBan3', css_class='col-3'),
                ),
                Row(
                    Column('blueBan4', css_class='col-3'),
                    Column('blueTargetBan4', css_class='col-3 border-end border-5'),
                    Column('redBan4', css_class='col-3'),
                    Column('redTargetBan4', css_class='col-3'),
                ),
                Row(
                    Column('blueBan5', css_class='col-3'),
                    Column('blueTargetBan5', css_class='col-3 border-end border-5'),
                    Column('redBan5', css_class='col-3'),
                    Column('redTargetBan5', css_class='col-3'),
                )
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

    def submit_game(self):
        gameNumber = Game.objects.aggregate(Max('gameNumber'))['gameNumber__max'] + 1
        gameBlueWins = self.cleaned_data.get('didBlueWin')
        gameRandomTeams = self.cleaned_data.get('randomTeams')
        gameMemeStatus = self.cleaned_data.get('memeGame')
        gameDate = self.cleaned_data.get('gameDate')
        game = Game(gameNumber=gameNumber, gameBlueWins=gameBlueWins, gameRandomTeams=gameRandomTeams, gameMemeStatus=gameMemeStatus, gameDate=gameDate, gameDuration=0)
        game.save()

        playerNameLaneDict = {}
        playerNameLaneDict['BlueTop'] = self.cleaned_data.get('blueTopLaner')
        playerNameLaneDict['BlueJungle'] = self.cleaned_data.get('blueJungLaner')
        playerNameLaneDict['BlueMid'] = self.cleaned_data.get('blueMidLaner')
        playerNameLaneDict['BlueBot'] = self.cleaned_data.get('blueBotLaner')
        playerNameLaneDict['BlueSupport'] = self.cleaned_data.get('blueSuppLaner')
        playerNameLaneDict['RedTop'] = self.cleaned_data.get('redTopLaner')
        playerNameLaneDict['RedJungle'] = self.cleaned_data.get('redJungLaner')
        playerNameLaneDict['RedMid'] = self.cleaned_data.get('redMidLaner')
        playerNameLaneDict['RedBot'] = self.cleaned_data.get('redBotLaner')
        playerNameLaneDict['RedSupport'] = self.cleaned_data.get('redSuppLaner')

        champLaneDict = {}
        champLaneDict['BlueTop'] = self.cleaned_data.get('blueTopChamp')
        champLaneDict['BlueJungle'] = self.cleaned_data.get('blueJungChamp')
        champLaneDict['BlueMid'] = self.cleaned_data.get('blueMidChamp')
        champLaneDict['BlueBot'] = self.cleaned_data.get('blueBotChamp')
        champLaneDict['BlueSupport'] = self.cleaned_data.get('blueSuppChamp')
        champLaneDict['RedTop'] = self.cleaned_data.get('redTopChamp')
        champLaneDict['RedJungle'] = self.cleaned_data.get('redJungChamp')
        champLaneDict['RedMid'] = self.cleaned_data.get('redMidChamp')
        champLaneDict['RedBot'] = self.cleaned_data.get('redBotChamp')
        champLaneDict['RedSupport'] = self.cleaned_data.get('redSuppChamp')

        playerPickLaneDict = {}
        playerPickLaneDict['BlueTop'] = self.cleaned_data.get('bluePlayerPickTop')
        playerPickLaneDict['BlueJungle'] = self.cleaned_data.get('bluePlayerPickJung')
        playerPickLaneDict['BlueMid'] = self.cleaned_data.get('bluePlayerPickMid')
        playerPickLaneDict['BlueBot'] = self.cleaned_data.get('bluePlayerPickBot')
        playerPickLaneDict['BlueSupport'] = self.cleaned_data.get('bluePlayerPickSupp')
        playerPickLaneDict['RedTop'] = self.cleaned_data.get('redPlayerPickTop')
        playerPickLaneDict['RedJungle'] = self.cleaned_data.get('redPlayerPickJung')
        playerPickLaneDict['RedMid'] = self.cleaned_data.get('redPlayerPickMid')
        playerPickLaneDict['RedBot'] = self.cleaned_data.get('redPlayerPickBot')
        playerPickLaneDict['RedSupport'] = self.cleaned_data.get('redPlayerPickSupp')

        champPickLaneDict = {}
        champPickLaneDict['BlueTop'] = self.cleaned_data.get('blueChampPickTop')
        champPickLaneDict['BlueJungle'] = self.cleaned_data.get('blueChampPickJung')
        champPickLaneDict['BlueMid'] = self.cleaned_data.get('blueChampPickMid')
        champPickLaneDict['BlueBot'] = self.cleaned_data.get('blueChampPickBot')
        champPickLaneDict['BlueSupport'] = self.cleaned_data.get('blueChampPickSupp')
        champPickLaneDict['RedTop'] = self.cleaned_data.get('redChampPickTop')
        champPickLaneDict['RedJungle'] = self.cleaned_data.get('redChampPickJung')
        champPickLaneDict['RedMid'] = self.cleaned_data.get('redChampPickMid')
        champPickLaneDict['RedBot'] = self.cleaned_data.get('redChampPickBot')
        champPickLaneDict['RedSupport'] = self.cleaned_data.get('redChampPickSupp')

        playersInGame = []

        for laneName, player in playerNameLaneDict.items():
            playersInGame.append(player)

            gameLanerBlueTeam = laneName.startswith('Blue')
            gameLanerLane = Lane.objects.filter(laneName__exact=laneName.replace('Blue', '').replace('Red', '')).get()
            gameLanerChamp = champLaneDict[laneName]
            gameLanerDraftOrder = playerPickLaneDict[laneName]
            if not gameLanerDraftOrder.isdigit():
                gameLanerDraftOrder = None
            else:
                gameLanerDraftOrder = int(gameLanerDraftOrder)
            gameLanerChampionSelectOrder = champPickLaneDict[laneName]

            gameLane = GameLaner(game=game, lane=gameLanerLane, blueTeam=gameLanerBlueTeam, player=player, champion=gameLanerChamp, draftOrder=gameLanerDraftOrder, championSelectOrder=gameLanerChampionSelectOrder)
            gameLane.save()

        champBansNumDict = {}
        champBansNumDict['Blue1'] = self.cleaned_data.get('blueBan1')
        champBansNumDict['Blue2'] = self.cleaned_data.get('blueBan2')
        champBansNumDict['Blue3'] = self.cleaned_data.get('blueBan3')
        champBansNumDict['Blue4'] = self.cleaned_data.get('blueBan4')
        champBansNumDict['Blue5'] = self.cleaned_data.get('blueBan5')

        champBansNumDict['Red1'] = self.cleaned_data.get('redBan1')
        champBansNumDict['Red2'] = self.cleaned_data.get('redBan2')
        champBansNumDict['Red3'] = self.cleaned_data.get('redBan3')
        champBansNumDict['Red4'] = self.cleaned_data.get('redBan4')
        champBansNumDict['Red5'] = self.cleaned_data.get('redBan5')

        banTargetNumDict = {}
        banTargetNumDict['Blue1'] = self.cleaned_data.get('blueTargetBan1').playerName
        banTargetNumDict['Blue2'] = self.cleaned_data.get('blueTargetBan2').playerName
        banTargetNumDict['Blue3'] = self.cleaned_data.get('blueTargetBan3').playerName
        banTargetNumDict['Blue4'] = self.cleaned_data.get('blueTargetBan4').playerName
        banTargetNumDict['Blue5'] = self.cleaned_data.get('blueTargetBan5').playerName

        banTargetNumDict['Red1'] = self.cleaned_data.get('redTargetBan1').playerName
        banTargetNumDict['Red2'] = self.cleaned_data.get('redTargetBan2').playerName
        banTargetNumDict['Red3'] = self.cleaned_data.get('redTargetBan3').playerName
        banTargetNumDict['Red4'] = self.cleaned_data.get('redTargetBan4').playerName
        banTargetNumDict['Red5'] = self.cleaned_data.get('redTargetBan5').playerName

        for i in range(1, 6):
            gameBanChampBlue = champBansNumDict['Blue{}'.format(i)]
            gameBanChampPlayerBlue = Player.objects.filter(playerName__exact=banTargetNumDict['Blue{}'.format(i)]).get()

            gameBanBlue = GameBan(game=game, champion=gameBanChampBlue, targetPlayer=gameBanChampPlayerBlue)
            gameBanBlue.save()

            gameBanChampRed = champBansNumDict['Red{}'.format(i)]
            gameBanChampPlayerRed = Player.objects.filter(playerName__exact=banTargetNumDict['Red{}'.format(i)]).get()

            gameBanRed = GameBan(game=game, champion=gameBanChampRed, targetPlayer=gameBanChampPlayerRed)
            gameBanRed.save()

        remoteGameID = self.cleaned_data['remoteGameID']
        if remoteGameID is not None:
            champMap = {champion.id: champion.name for champion in cass.get_champions()}
            match = cass.get_match(remoteGameID)

            game.gameRiotID = remoteGameID

            game.gameDuration = match.duration.total_seconds()
            game.save()

            GameLanerStats.provideStats(game, champMap, match)

    def clean(self):
        cleaned_data = super().clean()

        # region Player Name Duplicates
        playerNameList = []
        playerNameList.append(cleaned_data.get('blueTopLaner'))
        playerNameList.append(cleaned_data.get('blueJungLaner'))
        playerNameList.append(cleaned_data.get('blueMidLaner'))
        playerNameList.append(cleaned_data.get('blueBotLaner'))
        playerNameList.append(cleaned_data.get('blueSuppLaner'))
        playerNameList.append(cleaned_data.get('redTopLaner'))
        playerNameList.append(cleaned_data.get('redJungLaner'))
        playerNameList.append(cleaned_data.get('redMidLaner'))
        playerNameList.append(cleaned_data.get('redBotLaner'))
        playerNameList.append(cleaned_data.get('redSuppLaner'))
        if len(playerNameList) != len(set(playerNameList)):
            raise ValidationError("Duplicate player name", code="Duplicate player")
        # endregion

        # region PlayerPickOrder duplicates

        playerPickOrder = []
        playerPickOrder.append(cleaned_data.get('bluePlayerPickTop'))
        playerPickOrder.append(cleaned_data.get('bluePlayerPickJung'))
        playerPickOrder.append(cleaned_data.get('bluePlayerPickMid'))
        playerPickOrder.append(cleaned_data.get('bluePlayerPickBot'))
        playerPickOrder.append(cleaned_data.get('bluePlayerPickSupp'))
        playerPickOrder.append(cleaned_data.get('redPlayerPickTop'))
        playerPickOrder.append(cleaned_data.get('redPlayerPickJung'))
        playerPickOrder.append(cleaned_data.get('redPlayerPickMid'))
        playerPickOrder.append(cleaned_data.get('redPlayerPickBot'))
        playerPickOrder.append(cleaned_data.get('redPlayerPickSupp'))
        cleanedPlayerPickOrder = [x for x in playerPickOrder if x.isdigit()]
        if len(cleanedPlayerPickOrder) != len(set(cleanedPlayerPickOrder)):
            raise ValidationError("Duplicate player pick order", code="Duplicate Player Pick")
        # endregion

        # region Champion Duplicates
        championNames = []
        championNames.append(cleaned_data.get('blueTopChamp').championName)
        championNames.append(cleaned_data.get('blueJungChamp').championName)
        championNames.append(cleaned_data.get('blueMidChamp').championName)
        championNames.append(cleaned_data.get('blueBotChamp').championName)
        championNames.append(cleaned_data.get('blueSuppChamp').championName)
        championNames.append(cleaned_data.get('redTopChamp').championName)
        championNames.append(cleaned_data.get('redJungChamp').championName)
        championNames.append(cleaned_data.get('redMidChamp').championName)
        championNames.append(cleaned_data.get('redBotChamp').championName)
        championNames.append(cleaned_data.get('redSuppChamp').championName)
        championNames.append(cleaned_data.get('blueBan1').championName)
        championNames.append(cleaned_data.get('blueBan2').championName)
        championNames.append(cleaned_data.get('blueBan3').championName)
        championNames.append(cleaned_data.get('blueBan4').championName)
        championNames.append(cleaned_data.get('blueBan5').championName)
        championNames.append(cleaned_data.get('redBan1').championName)
        championNames.append(cleaned_data.get('redBan2').championName)
        championNames.append(cleaned_data.get('redBan3').championName)
        championNames.append(cleaned_data.get('redBan4').championName)
        championNames.append(cleaned_data.get('redBan5').championName)
        if len(championNames) != len(set(championNames)):
            raise ValidationError("Duplicate champion in picks and/or bans", code="Duplicate champ")
        # endregion

        # region Check Target Bans
        bluePlayers = []
        bluePlayers.append(cleaned_data.get('blueTopLaner'))
        bluePlayers.append(cleaned_data.get('blueJungLaner'))
        bluePlayers.append(cleaned_data.get('blueMidLaner'))
        bluePlayers.append(cleaned_data.get('blueBotLaner'))
        bluePlayers.append(cleaned_data.get('blueSuppLaner'))

        redPlayers = []
        redPlayers.append(cleaned_data.get('redTopLaner'))
        redPlayers.append(cleaned_data.get('redJungLaner'))
        redPlayers.append(cleaned_data.get('redMidLaner'))
        redPlayers.append(cleaned_data.get('redBotLaner'))
        redPlayers.append(cleaned_data.get('redSuppLaner'))

        blueTargetsToRed = []
        blueTargetsToRed.append(cleaned_data.get('blueTargetBan1'))
        blueTargetsToRed.append(cleaned_data.get('blueTargetBan2'))
        blueTargetsToRed.append(cleaned_data.get('blueTargetBan3'))
        blueTargetsToRed.append(cleaned_data.get('blueTargetBan4'))
        blueTargetsToRed.append(cleaned_data.get('blueTargetBan5'))

        redTargetsToBlue = []
        redTargetsToBlue.append(cleaned_data.get('redTargetBan1'))
        redTargetsToBlue.append(cleaned_data.get('redTargetBan2'))
        redTargetsToBlue.append(cleaned_data.get('redTargetBan3'))
        redTargetsToBlue.append(cleaned_data.get('redTargetBan4'))
        redTargetsToBlue.append(cleaned_data.get('redTargetBan5'))

        for possibleRedPlayer in blueTargetsToRed:
            if possibleRedPlayer not in redPlayers:
                raise ValidationError("Target Ban Target %(value)s not valid, not on other team", params={'value', possibleRedPlayer.playerName})
        for possibleBluePlayer in redTargetsToBlue:
            if possibleBluePlayer not in bluePlayers:
                raise ValidationError("Target Ban Target %(value)s not valid, not on other team", params={'value', possibleBluePlayer.playerName})
        # endregion

        # region Random Draft verify blanks
        if not cleaned_data.get('randomTeams'):
            for pick in playerPickOrder:
                if pick == '' or pick is None:
                    raise ValidationError("Cannot leave blank player pick orders if teams not random")
        # endregion

        return cleaned_data

    def clean_password(self):
        data = self.cleaned_data['password']
        user = authenticate(username='gameSubmitter', password=data)
        if user is None:
            raise ValidationError("Incorrect Password")
        return data

    def clean_remoteGameID(self):
        data = self.cleaned_data['remoteGameID']

        match = cass.get_match(data)
        if match is None:
            raise ValidationError("Match not found")
        if(match.queue != cass.Queue.custom):
            raise ValidationError("Match not a custom game")
        return data


class UpdateGameForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    localGame = forms.ModelChoiceField(label="Game to Update", queryset=Game.objects.all())
    remoteGameID = forms.IntegerField(label="Riot Game ID", widget=forms.TextInput, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-newGameForm'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            Fieldset(
                'Password',
                Row(
                    Column('password', css_class='col-2')
                )
            ),
            Fieldset(
                'Game',
                Row(
                    Column('localGame', css_class='col-2')
                ),
                Row(
                    Column('remoteGameID', css_class='col-2')
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

    def updateGame(self):
        remoteGameID = self.cleaned_data['remoteGameID']
        localGame = self.cleaned_data['localGame']

        localGame: Game

        remoteGameID = self.cleaned_data['remoteGameID']
        if remoteGameID is not None:
            champMap = {champion.id: champion.name for champion in cass.get_champions()}
            match = cass.get_match(remoteGameID)
            if match is None:
                raise ValidationError("Match not found")
            if match.queue != cass.Queue.custom:
                raise ValidationError("Match not a custom game")

        localGame.gameRiotID = remoteGameID

        localGame.gameDuration = match.duration.total_seconds()
        localGame.save()

        GameLanerStats.provideStats(localGame, champMap, match)

    def clean_remoteGameID(self):
        data = self.cleaned_data['remoteGameID']
        if data is None:
            # Check if game already has remoteID
            existingGame = self.cleaned_data['localGame']
            if existingGame.gameRiotID is None:
                raise ValidationError('Riot ID not supplied, and no existing riot id found')
            else:
                data = existingGame.gameRiotID

        match = cass.get_match(data)
        if match is None:
            raise ValidationError("Match not found")
        if match.queue != cass.Queue.custom:
            raise ValidationError("Match not a custom game")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        user = authenticate(username='gameSubmitter', password=data)
        if user is None:
            raise ValidationError("Incorrect Password")
        return data


class UpdateAllGamesForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-newGameForm'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            Fieldset(
                'Password',
                Row(
                    Column('password', css_class='col-2')
                )
            ),
            ButtonHolder(
                Submit('submit', 'Update All Games with Riot IDs')
            )
        )

    def updateGame(self):
        games = Game.objects.exclude(gameRiotID__isnull=True)
        for localGame in games:
            localGame: Game

            remoteGameID = localGame.gameRiotID
            if remoteGameID is not None:
                champMap = {champion.id: champion.name for champion in cass.get_champions()}

            match = cass.get_match(remoteGameID)
            if match is None:
                raise ValidationError("Match not found")
            if match.queue != cass.Queue.custom:
                raise ValidationError("Match not a custom game")

            localGame.gameDuration = match.duration.total_seconds()
            localGame.save()

            GameLanerStats.provideStats(localGame, champMap, match)

    def clean_password(self):
        data = self.cleaned_data['password']
        user = authenticate(username='gameSubmitter', password=data)
        if user is None:
            raise ValidationError("Incorrect Password")
        return data


class CreatePlayer(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())

    playerName = forms.CharField(label="Unique Player Name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-newPlayerForm'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            Fieldset(
                'Password',
                Row(
                    Column('password', css_class='col-2')
                )
            ),
            Fieldset(
                'Player',
                Row(
                    Column('playerName', css_class='col-2')
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

    def create_player(self):
        # Make new player
        player = Player(playerName=self.cleaned_data['playerName'])
        player.save()

    def clean_password(self):
        data = self.cleaned_data['password']
        user = authenticate(username='gameSubmitter', password=data)
        if user is None:
            raise ValidationError("Incorrect Password")
        return data

    def clean_playerName(self):
        data = self.cleaned_data['playerName']
        cleanName = data.strip()
        cleanName = cleanName.replace('.', '')
        foundPlayer = Player.objects.filter(playerName__exact=cleanName).exists()
        if foundPlayer:
            raise ValidationError('Player with same name already exists: {}'.format(Player.objects.filter(playerName__exact=cleanName).get().playerName))
        return cleanName


class LaneMatchup(forms.Form):
    player1 = forms.ModelChoiceField(label="Player", queryset=Player.objects.all().order_by('playerName'))
    player2 = forms.ModelChoiceField(label="Player", queryset=Player.objects.all().order_by('playerName'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-laneMatchupForm'
        self.helper.form_method = 'get'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            Fieldset(
                'Players',
                Row(
                    Column('player1', css_class='col-12')
                ),
                Row(
                    Column('player2', css_class='col-12')
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['player1'] == cleaned_data['player2']:
            raise ValidationError('Cannot input same player twice')
        return cleaned_data


class DuoForm(forms.Form):
    player1 = forms.ModelChoiceField(label="Player", queryset=Player.objects.all().order_by('playerName'))
    player2 = forms.ModelChoiceField(label="Player", queryset=Player.objects.all().order_by('playerName'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-laneMatchupForm'
        self.helper.form_method = 'get'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            Fieldset(
                'Players',
                Row(
                    Column('player1', css_class='col-12')
                ),
                Row(
                    Column('player2', css_class='col-12')
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['player1'] == cleaned_data['player2']:
            raise ValidationError('Cannot input same player twice')
        return cleaned_data
