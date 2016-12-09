
from abc import ABCMeta, abstractmethod
class People(object):
	"""docstring for Player"""

	 __metaclass__ = ABCMeta

	def __init__(self, peopleId,name=""):
		self.id = peopleId
		self.name = name
	def setName(self,name):
		self.name = name
	def getName(self):
		return self.name


class player(People):
	def __init__(self,peopleId):
		super(self,peopleId).__init__()
	