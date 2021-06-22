from django.conf import settings
from django.db import models
from django.utils import timezone

class Strategy(models.Model):
	raceType = models.TextChoices('Race', 'Terran Zerg Protoss') # 테 프 저
	difficultyType = models.TextChoices('difficulty', 'Easy Normal Hard') # 쉬움 보통 어려움
	
	title = models.CharField(max_length=200) # 전략명
	playerRace = models.CharField(blank=False, choices=raceType.choices, max_length=10) # 플레이어 종족
	enemyRace = models.CharField(blank=False, choices=raceType.choices, max_length=10) # 상대 종족
	keyUnit = models.TextField() # 핵심 유닛
	strategyType = models.TextField() # 전략 형태(타이밍, 올인, ...)
	difficulty = models.CharField(blank=True, choices=difficultyType.choices, max_length=10) # 난이도
	mapname = models.TextField() # 맵
	text = models.TextField() # 전략 상세 내용
	created_date = models.DateTimeField(default=timezone.now) # 전략을 작성한 날짜
	modified_date = models.DateTimeField(blank=True, null=True) # 전략을 수정한 날짜
	
	def create(self):
		self.created_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
