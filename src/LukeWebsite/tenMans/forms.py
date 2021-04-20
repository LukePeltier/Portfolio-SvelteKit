import os
import requests
from bootstrap_datepicker_plus import DateTimePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, ButtonHolder, Column, Div, Fieldset,
                                 Layout, MultiField, Row, Submit)
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db.models import Max
from django.db.utils import Error, IntegrityError
from configparser import ConfigParser
from riotwatcher import LolWatcher, ApiError

from tenMans.models import Champion, Game, GameBan, GameLaner, GameLanerStats, Lane, Player


class NewGameForm(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput())

    didBlueWin = forms.BooleanField(label="Did Blue Win?", required=False)
    randomTeams = forms.BooleanField(label="Random Teams", required=False)
    memeGame = forms.BooleanField(label="Meme Game", required=False)
    gameDate = forms.DateTimeField(label="Date of Game", widget=DateTimePickerInput())
    remoteGameID = forms.IntegerField(label = "Riot Game ID", widget=forms.TextInput, required=False)

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

    bluePlayerPickTop = forms.CharField(label="Blue Top Player Pick Order", max_length=1, required=False)
    bluePlayerPickJung = forms.CharField(label="Blue Jungle Player Pick Order", max_length=1, required=False)
    bluePlayerPickMid = forms.CharField(label="Blue Mid Player Pick Order", max_length=1, required=False)
    bluePlayerPickBot = forms.CharField(label="Blue Bot Player Pick Order", max_length=1, required=False)
    bluePlayerPickSupp = forms.CharField(label="Blue Support Player Pick Order", max_length=1, required=False)

    redPlayerPickTop = forms.CharField(label="Red Top Player Pick Order", max_length=1, required=False)
    redPlayerPickJung = forms.CharField(label="Red Jungle Player Pick Order", max_length=1, required=False)
    redPlayerPickMid = forms.CharField(label="Red Mid Player Pick Order", max_length=1, required=False)
    redPlayerPickBot = forms.CharField(label="Red Bot Player Pick Order", max_length=1, required=False)
    redPlayerPickSupp = forms.CharField(label="Red Support Player Pick Order", max_length=1, required=False)

    blueTopChamp = forms.ModelChoiceField(label="Blue Top Champion", queryset=Champion.objects.all().order_by('championName'))
    blueJungChamp = forms.ModelChoiceField(label="Blue Jungle Champion", queryset=Champion.objects.all().order_by('championName'))
    blueMidChamp = forms.ModelChoiceField(label="Blue Middle Champion", queryset=Champion.objects.all().order_by('championName'))
    blueBotChamp = forms.ModelChoiceField(label="Blue Bottom Champion", queryset=Champion.objects.all().order_by('championName'))
    blueSuppChamp = forms.ModelChoiceField(label="Blue Support Champion", queryset=Champion.objects.all().order_by('championName'))

    redTopChamp = forms.ModelChoiceField(label="Red Top Champion", queryset=Champion.objects.all().order_by('championName'))
    redJungChamp = forms.ModelChoiceField(label="Red Jungle Champion", queryset=Champion.objects.all().order_by('championName'))
    redMidChamp = forms.ModelChoiceField(label="Red Middle Champion", queryset=Champion.objects.all().order_by('championName'))
    redBotChamp = forms.ModelChoiceField(label="Red Bottom Champion", queryset=Champion.objects.all().order_by('championName'))
    redSuppChamp = forms.ModelChoiceField(label="Red Support Champion", queryset=Champion.objects.all().order_by('championName'))

    blueChampPickTop = forms.CharField(label="Blue Top Champ Pick Order", max_length=1)
    blueChampPickJung = forms.CharField(label="Blue Jungle Champ Pick Order", max_length=1)
    blueChampPickMid = forms.CharField(label="Blue Mid Champ Pick Order", max_length=1)
    blueChampPickBot = forms.CharField(label="Blue Bot Champ Pick Order", max_length=1)
    blueChampPickSupp = forms.CharField(label="Blue Support Champ Pick Order", max_length=1)

    redChampPickTop = forms.CharField(label="Red Top Champ Pick Order", max_length=1)
    redChampPickJung = forms.CharField(label="Red Jungle Champ Pick Order", max_length=1)
    redChampPickMid = forms.CharField(label="Red Mid Champ Pick Order", max_length=1)
    redChampPickBot = forms.CharField(label="Red Bot Champ Pick Order", max_length=1)
    redChampPickSupp = forms.CharField(label="Red Support Champ Pick Order", max_length=1)

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
                'Players',
                Row(
                    Column('blueTopLaner', css_class='col-3'),
                    Column('redTopLaner', css_class='col-3'),
                ),
                Row(
                    Column('blueJungLaner', css_class='col-3'),
                    Column('redJungLaner', css_class='col-3'),
                ),
                Row(
                    Column('blueMidLaner', css_class='col-3'),
                    Column('redMidLaner', css_class='col-3'),
                ),
                Row(
                    Column('blueBotLaner', css_class='col-3'),
                    Column('redBotLaner', css_class='col-3'),
                ),
                Row(
                    Column('blueSuppLaner', css_class='col-3'),
                    Column('redSuppLaner', css_class='col-3'),
                )
            ),
            Fieldset(
                'Player Pick Order<br><small>C for Captain, blank for random teams</small>',
                Row(
                    Column('bluePlayerPickTop', css_class='col-3'),
                    Column('redPlayerPickTop', css_class='col-3'),
                ),
                Row(
                    Column('bluePlayerPickJung', css_class='col-3'),
                    Column('redPlayerPickJung', css_class='col-3'),
                ),
                Row(
                    Column('bluePlayerPickMid', css_class='col-3'),
                    Column('redPlayerPickMid', css_class='col-3'),
                ),
                Row(
                    Column('bluePlayerPickBot', css_class='col-3'),
                    Column('redPlayerPickBot', css_class='col-3'),
                ),
                Row(
                    Column('bluePlayerPickSupp', css_class='col-3'),
                    Column('redPlayerPickSupp', css_class='col-3'),
                )
            ),
            Fieldset(
                'Champions',
                Row(
                    Column('blueTopChamp', css_class='col-3'),
                    Column('redTopChamp', css_class='col-3'),
                ),
                Row(
                    Column('blueJungChamp', css_class='col-3'),
                    Column('redJungChamp', css_class='col-3'),
                ),
                Row(
                    Column('blueMidChamp', css_class='col-3'),
                    Column('redMidChamp', css_class='col-3'),
                ),
                Row(
                    Column('blueBotChamp', css_class='col-3'),
                    Column('redBotChamp', css_class='col-3'),
                ),
                Row(
                    Column('blueSuppChamp', css_class='col-3'),
                    Column('redSuppChamp', css_class='col-3'),
                )
            ),
            Fieldset(
                'Champion Pick Order',
                Row(
                    Column('blueChampPickTop', css_class='col-3'),
                    Column('redChampPickTop', css_class='col-3'),
                ),
                Row(
                    Column('blueChampPickJung', css_class='col-3'),
                    Column('redChampPickJung', css_class='col-3'),
                ),
                Row(
                    Column('blueChampPickMid', css_class='col-3'),
                    Column('redChampPickMid', css_class='col-3'),
                ),
                Row(
                    Column('blueChampPickBot', css_class='col-3'),
                    Column('redChampPickBot', css_class='col-3'),
                ),
                Row(
                    Column('blueChampPickSupp', css_class='col-3'),
                    Column('redChampPickSupp', css_class='col-3'),
                )
            ),
            Fieldset(
                'Champion Bans',
                Row(
                    Column('blueBan1', css_class='col-3'),
                    Column('redBan1', css_class='col-3'),
                ),
                Row(
                    Column('blueBan2', css_class='col-3'),
                    Column('redBan2', css_class='col-3'),
                ),
                Row(
                    Column('blueBan3', css_class='col-3'),
                    Column('redBan3', css_class='col-3'),
                ),
                Row(
                    Column('blueBan4', css_class='col-3'),
                    Column('redBan4', css_class='col-3'),
                ),
                Row(
                    Column('blueBan5', css_class='col-3'),
                    Column('redBan5', css_class='col-3'),
                )
            ),
            Fieldset(
                'Ban Player Target',
                Row(
                    Column('blueTargetBan1', css_class='col-3'),
                    Column('redTargetBan1', css_class='col-3'),
                ),
                Row(
                    Column('blueTargetBan2', css_class='col-3'),
                    Column('redTargetBan2', css_class='col-3'),
                ),
                Row(
                    Column('blueTargetBan3', css_class='col-3'),
                    Column('redTargetBan3', css_class='col-3'),
                ),
                Row(
                    Column('blueTargetBan4', css_class='col-3'),
                    Column('redTargetBan4', css_class='col-3'),
                ),
                Row(
                    Column('blueTargetBan5', css_class='col-3'),
                    Column('redTargetBan5', css_class='col-3'),
                )
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

    def submit_game(self):
        gameNumber = Game.objects.aggregate(Max('gameNumber'))['gameNumber__max']+1
        gameBlueWins = self.cleaned_data.get('didBlueWin')
        gameRandomTeams = self.cleaned_data.get('randomTeams')
        gameMemeStatus = self.cleaned_data.get('memeGame')
        gameDate = self.cleaned_data.get('gameDate')
        game = Game(gameNumber=gameNumber, gameBlueWins=gameBlueWins,gameRandomTeams=gameRandomTeams,gameMemeStatus=gameMemeStatus,gameDate=gameDate)
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
        banTargetNumDict['Blue1'] = self.cleaned_data.get('blueTargetBan1')
        banTargetNumDict['Blue2'] = self.cleaned_data.get('blueTargetBan2')
        banTargetNumDict['Blue3'] = self.cleaned_data.get('blueTargetBan3')
        banTargetNumDict['Blue4'] = self.cleaned_data.get('blueTargetBan4')
        banTargetNumDict['Blue5'] = self.cleaned_data.get('blueTargetBan5')

        banTargetNumDict['Red1'] = self.cleaned_data.get('redTargetBan1')
        banTargetNumDict['Red2'] = self.cleaned_data.get('redTargetBan2')
        banTargetNumDict['Red3'] = self.cleaned_data.get('redTargetBan3')
        banTargetNumDict['Red4'] = self.cleaned_data.get('redTargetBan4')
        banTargetNumDict['Red5'] = self.cleaned_data.get('redTargetBan5')

        for i in range(1, 6):
            gameBanChampBlue = champBansNumDict['Blue{}'.format(i)]
            gameBanChampPlayerBlue = Player.objects.filter(playerName__exact=banTargetNumDict['Blue{}'.format(i)]).get()

            gameBanBlue = GameBan(game=game, champion=gameBanChampBlue,targetPlayer=gameBanChampPlayerBlue)
            gameBanBlue.save()


            gameBanChampRed = champBansNumDict['Red{}'.format(i)]
            gameBanChampPlayerRed = Player.objects.filter(playerName__exact=banTargetNumDict['Red{}'.format(i)]).get()

            gameBanRed = GameBan(game=game, champion=gameBanChampRed,targetPlayer=gameBanChampPlayerRed)
            gameBanRed.save()

        remoteGameID = self.cleaned_data['remoteGameID']
        if remoteGameID is not None:
            config_object = ConfigParser()
            config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
            apiKey = config_object['general']['RIOT_API_KEY']

            lolWatcher = LolWatcher(apiKey)
            region = 'na1'
            naChampVersion = lolWatcher.data_dragon.versions_for_region(region)['n']['champion']
            championList = lolWatcher.data_dragon.champions(naChampVersion, True)
            try:
                match = lolWatcher.match.by_id(region, remoteGameID)
            except ApiError as err:
                if err.response.status_code == 404:
                    raise ValidationError("Match not found")
                else:
                    raise

            for participant in match['participants']:
                #find a matching game laner
                blueTeam = participant['teamId']==100
                #find champ

                championDataName = championList['keys'][str(participant['championId'])]
                championTrueName = championList['data'][championDataName]['name']
                championObject = Champion.objects.filter(championName__exact=championTrueName).get()
                gameLaner = GameLaner.objects.filter(champion__exact=championObject, game__exact=game).get()

                statsObject = GameLanerStats(gameLaner=gameLaner,
                                            kills=participant['stats']['kills'],
                                            deaths=participant['stats']['deaths'],
                                            assists=participant['stats']['assists'],
                                            largestKillingSpree=participant['stats']['largestKillingSpree'],
                                            largestMultiKill=participant['stats']['largestMultiKill'],
                                            doubleKills=participant['stats']['doubleKills'],
                                            tripleKills=participant['stats']['tripleKills'],
                                            quadraKills=participant['stats']['quadraKills'],
                                            pentaKills=participant['stats']['pentaKills'],
                                            totalDamageDealtToChampions=participant['stats']['totalDamageDealtToChampions'],
                                            visionScore=participant['stats']['visionScore'],
                                            crowdControlScore=participant['stats']['timeCCingOthers'],
                                            totalDamageTaken=participant['stats']['totalDamageTaken'],
                                            goldEarned=participant['stats']['goldEarned'],
                                            turretKills=participant['stats']['turretKills'],
                                            inhibitorKills=participant['stats']['inhibitorKills'],
                                            laneMinionsKilled=participant['stats']['totalMinionsKilled'],
                                            neutralMinionsKilled=participant['stats']['neutralMinionsKilled'],
                                            teamJungleMinionsKilled=participant['stats']['neutralMinionsKilledTeamJungle'],
                                            enemyJungleMinionsKilled=participant['stats']['neutralMinionsKilledEnemyJungle'],
                                            controlWardsPurchased=participant['stats']['visionWardsBoughtInGame'],
                                            firstBlood=participant['stats']['firstBloodKill'],
                                            firstTower=participant['stats']['firstTowerKill'],
                                            csRateFirstTen=participant['timeline']['creepsPerMinDeltas']['0-10'],
                                            csRateSecondTen=participant['timeline']['creepsPerMinDeltas']['10-20'])

                statsObject.save()


    def clean(self):
        cleaned_data = super().clean()

        #region Player Name Duplicates
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
        #endregion

        #region PlayerPickOrder duplicates

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
        cleanedPlayerPickOrder = [ x for x in playerPickOrder if x.isdigit()]
        if len(cleanedPlayerPickOrder) != len(set(cleanedPlayerPickOrder)):
            raise ValidationError("Duplicate player pick order", code="Duplicate Player Pick")
        #endregion

        #region Champion Duplicates
        championNames=[]
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
        #endregion

        #region Check Target Bans
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
                raise ValidationError("Target Ban Target %(value)s not valid, not on other team", params={'value', possibleRedPlayer})
        for possibleBluePlayer in redTargetsToBlue:
            if possibleBluePlayer not in bluePlayers:
                raise ValidationError("Target Ban Target %(value)s not valid, not on other team", params={'value', possibleBluePlayer})
        #endregion

        #region Random Draft verify blanks
        if not cleaned_data.get('randomTeams'):
            for pick in playerPickOrder:
                if pick=='' or pick is None:
                    raise ValidationError("Cannot leave blank player pick orders if teams not random")
        #endregion

        return cleaned_data

    def clean_password(self):
        data = self.cleaned_data['password']
        user = authenticate(username='gameSubmitter', password=data)
        if user is None:
            raise ValidationError("Incorrect Password")
        return data

    def clean_remoteGameID(self):
        data = self.cleaned_data['remoteGameID']

        config_object = ConfigParser()
        config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
        apiKey = config_object['general']['RIOT_API_KEY']

        lolWatcher = LolWatcher(apiKey)
        region = 'na1'
        try:
            match = lolWatcher.match.by_id(region, data)
        except ApiError as err:
            if err.response.status_code == 404:
                raise ValidationError("Match not found")
            else:
                raise
        if(match['queueId']!=0):
            raise ValidationError("Match not a custom game")
        return data

class UpdateGameForm(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput())
    localGame = forms.ModelChoiceField(label = "Game to Update", queryset=Game.objects.all())
    remoteGameID = forms.IntegerField(label = "Riot Game ID", widget=forms.TextInput, required=False)

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

        config_object = ConfigParser()
        config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
        apiKey = config_object['general']['RIOT_API_KEY']

        lolWatcher = LolWatcher(apiKey)
        region = 'na1'
        naChampVersion = lolWatcher.data_dragon.versions_for_region(region)['n']['champion']
        championList = lolWatcher.data_dragon.champions(naChampVersion, True)
        try:
            match = lolWatcher.match.by_id(region, remoteGameID)
        except ApiError as err:
            if err.response.status_code == 404:
                raise ValidationError("Match not found")
            else:
                raise

        gameDuration = match['gameDuration']
        localGame.gameDuration = gameDuration
        localGame.save()

        for participant in match['participants']:
            #find a matching game laner
            blueTeam = participant['teamId']==100
            #find champ

            championDataName = championList['keys'][str(participant['championId'])]
            championTrueName = championList['data'][championDataName]['name']
            championObject = Champion.objects.filter(championName__exact=championTrueName).get()
            gameLaner = GameLaner.objects.filter(champion__exact=championObject, game__exact=localGame).get()

            #check for existing statsObject
            statsObject = GameLanerStats.objects.get(gameLaner__exact=gameLaner)
            if statsObject is not None:
                statsObject: GameLanerStats
                statsObject.gameLaner=gameLaner
                statsObject.kills=participant['stats']['kills']
                statsObject.deaths=participant['stats']['deaths']
                statsObject.assists=participant['stats']['assists']
                statsObject.largestKillingSpree=participant['stats']['largestKillingSpree']
                statsObject.largestMultiKill=participant['stats']['largestMultiKill']
                statsObject.doubleKills=participant['stats']['doubleKills']
                statsObject.tripleKills=participant['stats']['tripleKills']
                statsObject.quadraKills=participant['stats']['quadraKills']
                statsObject.pentaKills=participant['stats']['pentaKills']
                statsObject.totalDamageDealtToChampions=participant['stats']['totalDamageDealtToChampions']
                statsObject.visionScore=participant['stats']['visionScore']
                statsObject.crowdControlScore=participant['stats']['timeCCingOthers']
                statsObject.totalDamageTaken=participant['stats']['totalDamageTaken']
                statsObject.goldEarned=participant['stats']['goldEarned']
                statsObject.turretKills=participant['stats']['turretKills']
                statsObject.inhibitorKills=participant['stats']['inhibitorKills']
                statsObject.laneMinionsKilled=participant['stats']['totalMinionsKilled']
                statsObject.neutralMinionsKilled=participant['stats']['neutralMinionsKilled']
                statsObject.teamJungleMinionsKilled=participant['stats']['neutralMinionsKilledTeamJungle']
                statsObject.enemyJungleMinionsKilled=participant['stats']['neutralMinionsKilledEnemyJungle']
                statsObject.controlWardsPurchased=participant['stats']['visionWardsBoughtInGame']
                statsObject.firstBlood=participant['stats']['firstBloodKill']
                statsObject.firstTower=participant['stats']['firstTowerKill']
                statsObject.csRateFirstTen=participant['timeline']['creepsPerMinDeltas']['0-10']
                statsObject.csRateSecondTen=participant['timeline']['creepsPerMinDeltas']['10-20']
            else:
                statsObject = GameLanerStats(
                                        gameLaner=gameLaner,
                                        kills=participant['stats']['kills'],
                                        deaths=participant['stats']['deaths'],
                                        assists=participant['stats']['assists'],
                                        largestKillingSpree=participant['stats']['largestKillingSpree'],
                                        largestMultiKill=participant['stats']['largestMultiKill'],
                                        doubleKills=participant['stats']['doubleKills'],
                                        tripleKills=participant['stats']['tripleKills'],
                                        quadraKills=participant['stats']['quadraKills'],
                                        pentaKills=participant['stats']['pentaKills'],
                                        totalDamageDealtToChampions=participant['stats']['totalDamageDealtToChampions'],
                                        visionScore=participant['stats']['visionScore'],
                                        crowdControlScore=participant['stats']['timeCCingOthers'],
                                        totalDamageTaken=participant['stats']['totalDamageTaken'],
                                        goldEarned=participant['stats']['goldEarned'],
                                        turretKills=participant['stats']['turretKills'],
                                        inhibitorKills=participant['stats']['inhibitorKills'],
                                        laneMinionsKilled=participant['stats']['totalMinionsKilled'],
                                        neutralMinionsKilled=participant['stats']['neutralMinionsKilled'],
                                        teamJungleMinionsKilled=participant['stats']['neutralMinionsKilledTeamJungle'],
                                        enemyJungleMinionsKilled=participant['stats']['neutralMinionsKilledEnemyJungle'],
                                        controlWardsPurchased=participant['stats']['visionWardsBoughtInGame'],
                                        firstBlood=participant['stats']['firstBloodKill'],
                                        firstTower=participant['stats']['firstTowerKill'],
                                        csRateFirstTen=participant['timeline']['creepsPerMinDeltas']['0-10'],
                                        csRateSecondTen=participant['timeline']['creepsPerMinDeltas']['10-20'])

            statsObject.save()


    def clean_remoteGameID(self):
        data = self.cleaned_data['remoteGameID']
        if data is None:
            #Check if game already has remoteID
            existingGame = self.cleaned_data['localGame']
            if existingGame.gameRiotID is None:
                raise ValidationError('Riot ID not supplied, and no existing riot id found')
            else:
                data = existingGame.gameRiotID

        config_object = ConfigParser()
        config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
        apiKey = config_object['general']['RIOT_API_KEY']

        lolWatcher = LolWatcher(apiKey)
        region = 'na1'
        try:
            match = lolWatcher.match.by_id(region, data)
        except ApiError as err:
            if err.response.status_code == 404:
                raise ValidationError("Match not found")
            else:
                raise
        if(match['queueId']!=0):
            raise ValidationError("Match not a custom game")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        user = authenticate(username='gameSubmitter', password=data)
        if user is None:
            raise ValidationError("Incorrect Password")
        return data

class UpdateAllGamesForm(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput())

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

            config_object = ConfigParser()
            config_object.read(os.path.join(os.path.dirname(__file__), 'conf', 'api.ini'))
            apiKey = config_object['general']['RIOT_API_KEY']

            lolWatcher = LolWatcher(apiKey)
            region = 'na1'
            naChampVersion = lolWatcher.data_dragon.versions_for_region(region)['n']['champion']
            championList = lolWatcher.data_dragon.champions(naChampVersion, True)
            try:
                match = lolWatcher.match.by_id(region, remoteGameID)
            except ApiError as err:
                if err.response.status_code == 404:
                    raise ValidationError("Match not found")
                else:
                    raise

            gameDuration = match['gameDuration']
            localGame.gameDuration = gameDuration
            localGame.save()

            for participant in match['participants']:
                #find a matching game laner
                blueTeam = participant['teamId']==100
                #find champ

                championDataName = championList['keys'][str(participant['championId'])]
                championTrueName = championList['data'][championDataName]['name']
                championObject = Champion.objects.filter(championName__exact=championTrueName).get()
                gameLaner = GameLaner.objects.filter(champion__exact=championObject, game__exact=localGame).get()

                #check for existing statsObject
                statsObject = GameLanerStats.objects.get(gameLaner__exact=gameLaner)
                if statsObject is not None:
                    statsObject: GameLanerStats
                    statsObject.gameLaner=gameLaner
                    statsObject.kills=participant['stats']['kills']
                    statsObject.deaths=participant['stats']['deaths']
                    statsObject.assists=participant['stats']['assists']
                    statsObject.largestKillingSpree=participant['stats']['largestKillingSpree']
                    statsObject.largestMultiKill=participant['stats']['largestMultiKill']
                    statsObject.doubleKills=participant['stats']['doubleKills']
                    statsObject.tripleKills=participant['stats']['tripleKills']
                    statsObject.quadraKills=participant['stats']['quadraKills']
                    statsObject.pentaKills=participant['stats']['pentaKills']
                    statsObject.totalDamageDealtToChampions=participant['stats']['totalDamageDealtToChampions']
                    statsObject.visionScore=participant['stats']['visionScore']
                    statsObject.crowdControlScore=participant['stats']['timeCCingOthers']
                    statsObject.totalDamageTaken=participant['stats']['totalDamageTaken']
                    statsObject.goldEarned=participant['stats']['goldEarned']
                    statsObject.turretKills=participant['stats']['turretKills']
                    statsObject.inhibitorKills=participant['stats']['inhibitorKills']
                    statsObject.laneMinionsKilled=participant['stats']['totalMinionsKilled']
                    statsObject.neutralMinionsKilled=participant['stats']['neutralMinionsKilled']
                    statsObject.teamJungleMinionsKilled=participant['stats']['neutralMinionsKilledTeamJungle']
                    statsObject.enemyJungleMinionsKilled=participant['stats']['neutralMinionsKilledEnemyJungle']
                    statsObject.controlWardsPurchased=participant['stats']['visionWardsBoughtInGame']
                    statsObject.firstBlood=participant['stats']['firstBloodKill']
                    statsObject.firstTower=participant['stats']['firstTowerKill']
                    statsObject.csRateFirstTen=participant['timeline']['creepsPerMinDeltas']['0-10']
                    statsObject.csRateSecondTen=participant['timeline']['creepsPerMinDeltas']['10-20']
                else:
                    statsObject = GameLanerStats(
                                            gameLaner=gameLaner,
                                            kills=participant['stats']['kills'],
                                            deaths=participant['stats']['deaths'],
                                            assists=participant['stats']['assists'],
                                            largestKillingSpree=participant['stats']['largestKillingSpree'],
                                            largestMultiKill=participant['stats']['largestMultiKill'],
                                            doubleKills=participant['stats']['doubleKills'],
                                            tripleKills=participant['stats']['tripleKills'],
                                            quadraKills=participant['stats']['quadraKills'],
                                            pentaKills=participant['stats']['pentaKills'],
                                            totalDamageDealtToChampions=participant['stats']['totalDamageDealtToChampions'],
                                            visionScore=participant['stats']['visionScore'],
                                            crowdControlScore=participant['stats']['timeCCingOthers'],
                                            totalDamageTaken=participant['stats']['totalDamageTaken'],
                                            goldEarned=participant['stats']['goldEarned'],
                                            turretKills=participant['stats']['turretKills'],
                                            inhibitorKills=participant['stats']['inhibitorKills'],
                                            laneMinionsKilled=participant['stats']['totalMinionsKilled'],
                                            neutralMinionsKilled=participant['stats']['neutralMinionsKilled'],
                                            teamJungleMinionsKilled=participant['stats']['neutralMinionsKilledTeamJungle'],
                                            enemyJungleMinionsKilled=participant['stats']['neutralMinionsKilledEnemyJungle'],
                                            controlWardsPurchased=participant['stats']['visionWardsBoughtInGame'],
                                            firstBlood=participant['stats']['firstBloodKill'],
                                            firstTower=participant['stats']['firstTowerKill'],
                                            csRateFirstTen=participant['timeline']['creepsPerMinDeltas']['0-10'],
                                            csRateSecondTen=participant['timeline']['creepsPerMinDeltas']['10-20'])

                statsObject.save()


    def clean_password(self):
        data = self.cleaned_data['password']
        user = authenticate(username='gameSubmitter', password=data)
        if user is None:
            raise ValidationError("Incorrect Password")
        return data

class CreatePlayer(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput())

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
        #Make new player
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