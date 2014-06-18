from django.db import models
from django.forms import ModelForm
from django import forms
class Player1(models.Model):
	name = models.CharField(max_length=40)
	age = models.IntegerField()
	nationality = models.CharField(max_length=40)
	speed = models.IntegerField()
	driblle_ability = models.IntegerField()
	def __unicode__(self):
		return self.name
class PlayerForm(ModelForm):
	
	class Meta:
		model = Player1
		fields= ('name','age','nationality','speed','driblle_ability') 	
			
		
	
	
