
class Game(object):

	# four_Factors_tile = ["Pace","eFG%","TOV%","ORB%","FT/FGA","ORtg"]
	"""docstring for Game"""
	def __init__(self, gameId, date=None,host=None,guest=None,host_score=-1,guest_score=-1,host_Basic_Stats={},host_Advanced_Stats={},guest_Basic_Stats={},guest_Advanced_Stats={}):
		self.id= gameId
		self.date = date
		self.host = host
		self.guest = guest
		self.host_score = host_score
		self.guest_score = guest_score
		self.host_Basic_Stats = host_Basic_Stats
		self.host_Advanced_Stats = host_Advanced_Stats
		self.guest_Basic_Stats = guest_Basic_Stats
		self.guest_Advanced_Stats = guest_Advanced_Stats


	def setData(self,attr,data):
		# check valid
		setattr(self,attr,data)
	def getData(self,attr):
		return getattr(self,attr,None)

	# def setDate(self,date):
	# 	self.__date = date
	# def getDate(self):
	# 	return self.__date

	# def setHost(self,host):
	# 	self.__host= host
	# def getHost(self):
	# 	return self.__host

	# def setGuest(self,guest):
	# 	self.__guest= guest
	# def getGuest(self):
	# 	return self.__guest

	# def setHostScore(self,host_score):
	# 	self.__host_score= host_score
	# def getHost(self):
	# 	return self.__host_score





from abc import ABCMeta, abstractmethod
class People(object):
	"""docstring for Player"""
	__metaclass__ = ABCMeta

	def __init__(self, peopleId,name=""):
		self.id = peopleId
		self.name = name

	# Override equal method
	def __eq__(self, other):
		if isinstance(other,People):
			return self.peopleId == other.peopleId
		return NotImplemented
	def __ne__(self,other):
		result = self.__eq__(other)
		if result is NotImplemented:
			return result
		return not result

	def setData(self,attr,data):
		# check valid
		setattr(self,attr,data)
	def getData(self,attr):
		return getattr(self,attr,None)


class Player(People):
	def __init__(self,playerId,name="",game_basic_stats={},playerURL="",game_adv_stats={}):
		super(Player,self).__init__(playerId,name)
		self.game_basic_stats = game_basic_stats
		self.game_adv_stats = game_adv_stats
		self.playerURL = playerURL

	




class Team(object):
	def __init__(self, abr,name="",location="",playerList=[],imageURl="",teamURL=""):
		self.abr = abr
		self.location = location
		self.name = name
		self.playerList = playerList
		self.imageURL = imageURl
		self.teamURL = teamURL
	def setData(self,attr,data):
		# check valid
		setattr(self,attr,data)
	def getData(self,attr):
		return getattr(self,attr,None)


   	# def setLocation(self,location):
   	# 	self.__location = location
   	# def getLocation(self):
   	# 	return self.__location

   	# def setName(self,name):
   	# 	self.__name = name
   	# def getName(self):
   	# 	return self.__name

   	# def addPlayer(player):
   	# 	self.__playerList.append(player)

   	# def setImageURL(imageURl):
   	# 	self.__imageURL = imageURl
   	# def getImageURL(imageURl):
   	# 	sreturn self.__imageURL

   	# def searchPlayer(id):
   	# 	for player in self.__playerList:
   	# 		if player.id == id:
   	# 			return player
   	# 	return -1
