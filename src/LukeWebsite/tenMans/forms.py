from crispy_forms.layout import ButtonHolder, Column, Div, Fieldset, HTML, Layout, MultiField, Row, Submit
from django import forms

from tenMans.models import Champion
from bootstrap_datepicker_plus import DateTimePickerInput
from crispy_forms.helper import FormHelper
from django.contrib.auth import authenticate

class NewGameForm(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput())

    didBlueWin = forms.BooleanField(label="Did Blue Win?", required=False)
    randomTeams = forms.BooleanField(label="Random Teams", required=False)
    memeGame = forms.BooleanField(label="Meme Game", required=False)
    gameDate = forms.DateTimeField(label="Date of Game", widget=DateTimePickerInput())

    blueTopLaner = forms.CharField(label="Blue Top Laner")
    blueJungLaner = forms.CharField(label="Blue Jungler")
    blueMidLaner = forms.CharField(label="Blue Mid Laner")
    blueBotLaner = forms.CharField(label="Blue Bot Laner")
    blueSuppLaner = forms.CharField(label="Blue Support")

    redTopLaner = forms.CharField(label="Red Top Laner")
    redJungLaner = forms.CharField(label="Red Jungler")
    redMidLaner = forms.CharField(label="Red Mid Laner")
    redBotLaner = forms.CharField(label="Red Bot Laner")
    redSuppLaner = forms.CharField(label="Red Support")

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

    blueTopChamp = forms.ModelChoiceField(label="Blue Top Champion", queryset=Champion.objects.all())
    blueJungChamp = forms.ModelChoiceField(label="Blue Jungle Champion", queryset=Champion.objects.all())
    blueMidChamp = forms.ModelChoiceField(label="Blue Middle Champion", queryset=Champion.objects.all())
    blueBotChamp = forms.ModelChoiceField(label="Blue Bottom Champion", queryset=Champion.objects.all())
    blueSuppChamp = forms.ModelChoiceField(label="Blue Support Champion", queryset=Champion.objects.all())

    redTopChamp = forms.ModelChoiceField(label="Red Top Champion", queryset=Champion.objects.all())
    redJungChamp = forms.ModelChoiceField(label="Red Jungle Champion", queryset=Champion.objects.all())
    redMidChamp = forms.ModelChoiceField(label="Red Middle Champion", queryset=Champion.objects.all())
    redBotChamp = forms.ModelChoiceField(label="Red Bottom Champion", queryset=Champion.objects.all())
    redSuppChamp = forms.ModelChoiceField(label="Red Support Champion", queryset=Champion.objects.all())

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

    blueBan1 = forms.ModelChoiceField(label="Blue Ban 1", queryset=Champion.objects.all())
    blueBan2 = forms.ModelChoiceField(label="Blue Ban 2", queryset=Champion.objects.all())
    blueBan3 = forms.ModelChoiceField(label="Blue Ban 3", queryset=Champion.objects.all())
    blueBan4 = forms.ModelChoiceField(label="Blue Ban 4", queryset=Champion.objects.all())
    blueBan5 = forms.ModelChoiceField(label="Blue Ban 5", queryset=Champion.objects.all())

    redBan1 = forms.ModelChoiceField(label="Red Ban 1", queryset=Champion.objects.all())
    redBan2 = forms.ModelChoiceField(label="Red Ban 2", queryset=Champion.objects.all())
    redBan3 = forms.ModelChoiceField(label="Red Ban 3", queryset=Champion.objects.all())
    redBan4 = forms.ModelChoiceField(label="Red Ban 4", queryset=Champion.objects.all())
    redBan5 = forms.ModelChoiceField(label="Red Ban 5", queryset=Champion.objects.all())

    blueTargetBan1 = forms.CharField(label="Blue Ban 1 Target Player", required=False)
    blueTargetBan2 = forms.CharField(label="Blue Ban 2 Target Player", required=False)
    blueTargetBan3 = forms.CharField(label="Blue Ban 3 Target Player", required=False)
    blueTargetBan4 = forms.CharField(label="Blue Ban 4 Target Player", required=False)
    blueTargetBan5 = forms.CharField(label="Blue Ban 5 Target Player", required=False)

    redTargetBan1 = forms.CharField(label="Red Ban 1 Target Player", required=False)
    redTargetBan2 = forms.CharField(label="Red Ban 2 Target Player", required=False)
    redTargetBan3 = forms.CharField(label="Red Ban 3 Target Player", required=False)
    redTargetBan4 = forms.CharField(label="Red Ban 4 Target Player", required=False)
    redTargetBan5 = forms.CharField(label="Red Ban 5 Target Player", required=False)

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
        return False

    def getCleanField(self, fieldName):
        data = self.cleaned_data.get(fieldName)
        return data