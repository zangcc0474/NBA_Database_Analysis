from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Game(models.Model):
	# only display the date
	game_date = models.DateField('game date',primary_key= True)

	# display both date an time
	# game_date = models.DateTimeField('game date')
	host = models.CharField(max_length=100)
	guest = models.CharField(max_length=100)
	host_score = models.IntegerField()
	guest_score = models.IntegerField()

class Player(models.Model):
	player_id = models.IntegerField(primary_key= True)
	player_name = models.CharField(max_length=100)

class Player_Stats(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	player = models.ForeignKey(Player,on_delete=models.CASCADE)
	assistant = models.IntegerField()
	block = models.IntegerField()







