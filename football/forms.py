from django import forms


class Player1(forms.Form):
	nasa = forms.CharField(max_length=40)
	age = forms.CharField(max_length=40)
	nationality = forms.CharField(max_length=40)
	speed = forms.IntegerField()
	driblle_ability = forms.IntegerField()