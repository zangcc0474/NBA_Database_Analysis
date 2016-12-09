
class Team(object):
	def __init__(self, abr,location="",name="",playerList=[],imageURl=""):
		self.abr = abr
		self.__location = location
		self.__name = name
		self.__playerList = playerList
		self.__imageURL = imageURl


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