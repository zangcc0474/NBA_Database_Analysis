from __future__ import unicode_literals

from django.db import models

from app.scraping import scrape

import datetime


#################### Manager ####################
class GameManager(models.Manager):

    def create_game(self,game_date):
    	for game in scrape.scrape_Game(game_date):
			hostTeam = game.getData('host')
			guestTeam = game.getData('guest')
			host_score = game.getData('host_score')
			guest_score = game.getData('guest_score')
			game_date = game.getData('date')
			game_id = game.getData('id')
			print(game_date)
			if hostTeam == None or guestTeam == None:
				return -1
			else:
				hostTeamName = hostTeam.getData('name')
				guestTeamName = guestTeam.getData('name')
				if hostTeamName != None and guestTeamName != None and host_score != None and guest_score != None and game_date!= None and game_id != None :
					game = self.create(host=hostTeamName,guest=guestTeamName,host_score=int(host_score),guest_score=int(guest_score),game_date=game_date,game_id=game_id)
					game.save()
				else:
					return -1


#################### Team ####################

class Team(models.Model):
	team_id = models.IntegerField(primary_key= True)
	name = models.CharField(max_length=100)


#################### Player ####################
class Player(models.Model):
	player_id = models.IntegerField(primary_key= True)
	name = models.CharField(max_length=100)
	def __str__(self):              
		return self.player_name


#################### Game ####################
class Game(models.Model):

	game_id = models.CharField(max_length=100, primary_key = True, default='-1')
	# only display the date
	game_date = models.DateTimeField('game date', auto_now_add=False)

	# display both date an time
	# game_date = models.DateTimeField('game date')
	host = models.CharField(max_length=100)
	guest = models.CharField(max_length=100)
	host_score = models.IntegerField()
	guest_score = models.IntegerField()

	host_team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='host_team')
	guest_team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='guest_team')

	objects = GameManager()

	def __str__(self):              
		return self.game_id

class Player_Game_Stats(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	player = models.ForeignKey(Player,on_delete=models.CASCADE)
	assistant = models.IntegerField()
	block = models.IntegerField()

class Player_Game_Adv_Stats(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	player = models.ForeignKey(Player,on_delete=models.CASCADE)





class Contract(models.Model):
	year = models.DateField()
	Salary = models.BigIntegerField()
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)



date = datetime.datetime(2016,1,24)
# result = Game.objects.create_game(date)






