from PySide6.QtCore import QObject, Property
from BuildingBlocks import Observable

length = 180
beam = 20
draft = 6
displacement = 10000
shaftCount = 2
speed = 30
def blockCoefficient():
	volume = length*beam*draft
	return displacement/volume





class Event(object):
	pass

class Ship(Observable):
	def __init__(self):

		self._length = 180
		self._beam = 20
		self._draft = 6
		self._displacement = 10000
		self._shaftCount = 2
		self._speed = 30
		self._blockCoeff = self.calcBlock()

		super(Ship, self).__init__()

# methods
	def calcBlock(self):		
		volume = self.length*self.beam*self.draft
		self._blockCoeff = self.displacement/volume
	def calcDisp(self):		
		volume = self.length*self.beam*self.draft
		self._displacement = self.blockCoeff*volume

#getters & setters
	@property
	def length(self):
		return self._length
	@length.setter
	def length(self, value):
		self._length = value
		self.fire()

	@property
	def beam(self):
		return self._beam
	@beam.setter
	def beam(self, value):
		self._beam = value
		self.fire()
		
	@property
	def draft(self):
		return self._draft
	@draft.setter
	def draft(self, value):
		self._draft = value
		self.fire()

	@property
	def displacement(self):
		return self._displacement
	@displacement.setter
	def displacement(self, value):
		self._displacement = value
		calcBlock()
		self.fire()

	@property
	def shaftCount(self):
		return self._shaftCount
	@shaftCount.setter
	def shaftCount(self, value):
		self._shaftCount = value
		self.fire()

	@property
	def speed(self):
		return self._speed
	@speed.setter
	def speed(self, value):
		self._speed = value
		self.fire()

	@property
	def blockCoeff(self):
		return self._blockCoeff
	@blockCoeff.setter
	def blockCoeff(self, value):
		self._blockCoeff = value
		self.calcDisp()
		self.fire()
	

ship = Ship()