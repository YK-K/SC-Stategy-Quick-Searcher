from django.conf import settings
from django.db import models
from django.utils import timezone

class Strategy(models.Model):
	raceType = models.TextChoices('Race', 'Terran Zerg Protoss') # 테 프 저
	
	title = models.CharField(max_length=200) # 
	playerRace = models.CharField(blank=False, choices=raceType.choices, max_length=10) #
	enemyRace = models.CharField(blank=False, choices=raceType.choices, max_length=10) #
	text = models.TextField() #
	password = models.CharField(max_length=10) #
	created_date = models.DateTimeField(default=timezone.now) #
	modified_date = models.DateTimeField(blank=True, null=True) #
	
	def create(self):
		self.created_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
