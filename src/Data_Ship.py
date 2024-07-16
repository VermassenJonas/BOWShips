from BuildingBlocks import Observable


from decimal import *




class Event(object):
	pass
class Ship():
	def __init__(self) -> None:
		self.length = Observable(Decimal(180))
		self.beam = Observable(Decimal(20))
		self.draft = Observable(Decimal(6))
		self.displacement = Observable(Decimal(10000))
		self.shaftCount = Observable(Decimal(2))
		self.speed = Observable(Decimal('30'))
		self.blockCoeff = Observable(self.calcBlock())

	def calcBlock(self):		
		volume = self.length.value*self.beam.value*self.draft.value
		return self.displacement.value/volume
	

#class Ship(Observable):
#	def __init__(self):
#
#		self._length = Decimal('180')
#		self._beam = Decimal('20')
#		self._draft = Decimal('6')
#		self._displacement =Decimal('10000')
#		self._shaftCount = Decimal(2)
#		self._speed = Decimal('30')
#		self.calcBlock()
#
#		super(Ship, self).__init__()
#
#	# methods
#	def calcBlock(self):		
#		volume = self.length*self.beam*self.draft
#		self._blockCoeff = self.displacement/volume
#	def calcDisp(self):		
#		volume = self.length*self.beam*self.draft
#		self._displacement = Decimal(self.blockCoeff*volume)
#
#	#getters & setters
#	@property
#	def length(self):
#		return self._length
#	@length.setter
#	def length(self, value):
#		self._length = Decimal(value)
#		self.fire()
#
#	@property
#	def beam(self):
#		return self._beam
#	@beam.setter
#	def beam(self, value):
#		self._beam = Decimal(value)
#		self.fire()
#		
#	@property
#	def draft(self):
#		return self._draft
#	@draft.setter
#	def draft(self, value):
#		self._draft = Decimal(value)
#		self.fire()
#
#	@property
#	def displacement(self):
#		return self._displacement
#	@displacement.setter
#	def displacement(self, value):
#		self._displacement = Decimal(value)
#		self.calcBlock()
#		self.fire()
#
#	@property
#	def shaftCount(self):
#		return self._shaftCount
#	@shaftCount.setter
#	def shaftCount(self, value):
#		self._shaftCount = Decimal(value)
#		self.fire()
#
#	@property
#	def speed(self):
#		return self._speed
#	@speed.setter
#	def speed(self, value):
#		self._speed = Decimal(value)
#		self.fire()
#
#	@property
#	def blockCoeff(self):
#		return self._blockCoeff
#	@blockCoeff.setter
#	def blockCoeff(self, value):
#		self._blockCoeff = Decimal(value)
#		self.calcDisp()
#		self.fire()

ship = Ship()