
from urllib2 import urlopen 
from urllib2 import HTTPError 
from bs4 import BeautifulSoup

from app.scraping import models

import datetime

import pytz

ERROR_MESSAGE = "ERROR:"

# the default time zone is Eastern
local = pytz.timezone ("US/Eastern")


baseURL = "http://www.basketball-reference.com"

Basic_Box_Score_Stats_header = {}
Advanced_Box_Score_Stats_header = {}

# return a list of gamelinks by given date 
def paresGameLinks(year,month,day):
	boxScoreURL = baseURL+"/boxscores//index.cgi?month="+str(month)+"&day="+str(day)+"&year="+str(year)
	bsObj = getSource(boxScoreURL)

	# if gameData is null means the no game on that day
	gameData=bsObj.find(class_="game_summaries")
	link = []
	if(gameData == None):
		print("No Game on this Day")
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
	# assign score box
	gameMeta = scoreBox.find(class_="scorebox_meta").get_text().split('\n')[1:-1]
	guestTeam = models.Team(teams[0][0],teams[0][1])
	hostTeam = models.Team(teams[1][0],teams[1][1])
	game.setData('host',hostTeam)
	game.setData('guest',guestTeam)
	game.setData('host_score',scores[1])
	game.setData('guest_score',scores[0])


	# convert string date to datetime
	try:
	# localize the time zone 
	# http://stackoverflow.com/questions/79797/how-do-i-convert-local-time-to-utc-in-python
		naive = datetime.datetime.strptime(gameMeta[0],'%I:%M %p, %B %d, %Y')
		gameDate = local.localize(naive, is_dst=None)
		game.setData('date',gameDate)
	except Exception:
		print("INVALID GAMEDATE")

	# print game info 
	# print(hostTeam.getData("name"),":",guestTeam.getData("name"),game.getData('host_score'),":",game.getData('guest_score'))

	# generate the header description dictionary
	parse_Basic_Box_Score_Stats_header(bsObj)
	parse_Advanced_Box_Score_Stats_header(bsObj)

	guest_Starters,guest_Reserves = parse_Box_Score_Stats(bsObj,guestTeam)
	host_Starters,host_Reserves = parse_Box_Score_Stats(bsObj,hostTeam)
	return game


# parse the basic score data for each player
def parse_Box_Score_Stats(resource,team):
	# assign detial score, and team factors
	basic_data = resource.find("table",{"id":"box_"+team.getData("abr").lower()+"_basic"}).findAll("tr")
	adv_data = resource.find("table",{"id":"box_"+team.getData("abr").lower()+"_advanced"}).findAll("tr")
	Starters,Reserves = parse_Box_Score_Stats_helper(basic_data,{},{})
	Starters,Reserves = parse_Box_Score_Stats_helper(adv_data,Starters,Reserves)

	# display the output 

	# for player in Starters:
	# 	print(Starters[player].getData("name")," ",Starters[player].getData("id")," ",Starters[player].getData("playerURL"))
	# 	print(Starters[player].getData("game_basic_stats"))
	# 	print(Starters[player].getData("game_adv_stats"))


	# for player in Reserves:
	# 	print(Reserves[player].getData("name")," ",Reserves[player].getData("id")," ",Reserves[player].getData("playerURL"))
	# 	print(Reserves[player].getData("game_basic_stats"))
	# 	print(Starters[player].getData("game_adv_stats"))

	return Starters,Reserves


# parse the player info 
def parse_player_info(resource,flag):
	player_info = resource.find("th",{"data-stat":"player"})
	if(player_info!=None and player_info.a !=None):
		player_url= player_info.a.get("href")
		player_id = ""
		for ele in player_url.split("/"):
			if(".html" in ele):
				player_id = ele.replace(".html","")
		player_name = player_info.a.get_text()
		# print(player_name," ",player_id)

		assert(player_id != "")
		player = models.Player(player_id,player_name)
		player.setData('playerURL',player_url)
		if(flag == 0):
			return player
		else:
			return player_id
	else:
		return None


# parse adv_data and basic_data
def parse_Box_Score_Stats_helper(resource,Starters,Reserves):
	flag = 1
	if len(Starters)==0 and len(Reserves)==0 : 
		flag = 0
	for row in resource:
		player = parse_player_info(row,flag)
		player_data = row.findAll("td")
		player_game_stats = {}
		if(player != None):
			if(flag == 1):
			# assert the player exist in Advanced should already be initialized in Basic
				assert((player in Reserves) or (player in Starters))

			for data in player_data:
				player_game_stats[data.get("data-stat")] = data.get_text()
			if(flag==0):
				player.setData('game_basic_stats',player_game_stats)
			if(flag==1):
				if(player in Starters):
					Starters[player].setData('game_adv_stats',player_game_stats)
				else:
					Reserves[player].setData('game_adv_stats',player_game_stats)
			if(flag == 0):
				if(len(Starters)<5):
					Starters[player.getData('id')] = player
				else:
					Reserves[player.getData('id')] = player
	return Starters,Reserves






def parse_Basic_Box_Score_Stats_header(resource):
	if(len(Basic_Box_Score_Stats_header)==0):
		for key in resource.findAll("th",{"data-over-header":"Basic Box Score Stats"}):
			Basic_Box_Score_Stats_header[key.get("data-stat")] = key.get("aria-label")
	

def parse_Advanced_Box_Score_Stats_header(resource):
	if(len(Advanced_Box_Score_Stats_header)==0):
		for key in resource.findAll("th",{"data-over-header":"Advanced Box Score Stats"}):
			Advanced_Box_Score_Stats_header[key.get("data-stat")] = key.get("data-tip")



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

def scrape_Game(date):
	result = []
	d = date.strftime('%Y,%m,%d').split(',')
	assert(len(d)==3)
	for link in paresGameLinks(d[0],d[1],d[2]):
		result.append(parseGame(link))
	return result



# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.PhantomJS(executable_path='') driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html") try:
#         element = WebDriverWait(driver, 10).until(
#                            EC.presence_of_element_located((By.ID, "loadedButton")))
# finally: print(driver.find_element_by_id("content").text) driver.close()



