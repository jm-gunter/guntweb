from django import forms
from . import models

class GameForm(forms.ModelForm):
    class Meta:
        model = models.Game
        fields = ['date', 'imageurl', 'name', 'rounds', 'teams', 'venue']

class TeamGameForm(forms.Form):
    team_name = forms.CharField(label='', max_length=200)

    # all these fields should be generated from number of rounds...
    round1_score = forms.DecimalField(label='', min_value=0.0, max_value=99.9, decimal_places=1)
    round2_score = forms.DecimalField(label='', min_value=0.0, max_value=99.9, decimal_places=1)
    round3_score = forms.DecimalField(label='', min_value=0.0, max_value=99.9, decimal_places=1)
    round4_score = forms.DecimalField(label='', min_value=0.0, max_value=99.9, decimal_places=1)
    round5_score = forms.DecimalField(label='', min_value=0.0, max_value=99.9, decimal_places=1)
    final_score = forms.DecimalField(label='', min_value=0.0, max_value=99.9, decimal_places=1)
