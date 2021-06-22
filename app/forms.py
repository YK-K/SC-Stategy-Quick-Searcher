from django import forms
from .models import Strategy

class StrategyForm(forms.ModelForm):
	class Meta:
		model = Strategy
		fields = ('title', 'playerRace', 'enemyRace', 'keyUnit', 'strategyType', 'difficulty', 'mapname', 'text', 'password')
