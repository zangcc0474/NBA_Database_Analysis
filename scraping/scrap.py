
from urllib.request import urlopen 
from urllib.error import HTTPError 
from bs4 import BeautifulSoup

import models

import datetime

ERROR_MESSAGE = "ERROR:"


baseURL = "http://www.basketball-reference.com"

# return a list of gamelinks by given date 
def paresGameLinks(year,month,day):
	boxScoreURL = baseURL+"/boxscores//index.cgi?month="+str(month)+"&day="+str(day)+"&year="+str(year)
	bsObj = getSource(boxScoreURL)

	# if gameData is null means the no game on that day
	gameData=bsObj.find(class_="game_summaries")
	link = []
	if(gameData!=None):
		for rows in gameData.findAll("td",{"class":"right gamelink"}):
			link.append(str(rows.find("a").get('href')))
	return link



def parseGame(link):
	gameId = link.replace(".html","").split('/')[-1]
	game = models.Game(gameId)
	gameScoreURL = baseURL+link
	bsObj = getSource(gameScoreURL)
	scoreBox = bsObj.find(class_="scorebox")
	scores = [score.get_text() for score in scoreBox.findAll(class_="score")]
	teams = []
	for team in scoreBox.findAll("a",{"itemprop":"name"}):
		teamAbr = str(team.get('href')).split('/')[2]
		assert len(teamAbr)==3
		teams.append((teamAbr,team.get_text()))
	# make sure the scores and teams are valid
	# assert len(scores)==2 and len(teams) == 2
	gameMeta = scoreBox.find(class_="scorebox_meta").get_text().split('\n')[1:-1]
	guestTeam = models.Team(teams[0][0],teams[0][1])
	hostTeam = models.Team(teams[1][0],teams[1][1])
	game.setData('host',hostTeam)
	game.setData('guest',guestTeam)
	game.setData('host_score',scores[1])
	game.setData('guest_score',scores[0])

	# convert string date to datetime
	try:
		gameDate = datetime.datetime.strptime(gameMeta[0],'%I:%M %p, %B %d, %Y')
		game.setData('date',gameDate)
	except Exception:
		print("INVALID GAMEDATE")
	





# get url request
def getSource(url): 
	try:
		html = urlopen(url) 
	except HTTPError as e:
		return None 
	try:
	    bsObj = BeautifulSoup(html.read(),"html.parser")
	except AttributeError as e:
		return None 
	return bsObj


# def printError (f) :
#     def g (n) :
#         v = f(n)
#         assert v != False
#         return v
#     return g

for link in paresGameLinks(2016,2,8):
	parseGame(link)




