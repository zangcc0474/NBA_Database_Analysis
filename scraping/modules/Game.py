
class Game(object):
	"""docstring for Game"""
	def __init__(self, gameId, date=None,host="",guest="",host_score=-1,guest_score=-1):
		self.id= gameId
		self.__date = date
		self.__host = host
		self.__guest = guest
		self.__host_score = host_score
		self.__guest_score = guest_score

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




