
from observable_properties import observable, Observable
from decimal import *






class Ship(Observable):
	def __init__(self):

		self._length = Decimal('180')
		self._beam = Decimal('20')
		self._draft = Decimal('6')
		self._displacement =Decimal('10000')
		self._shaftCount = Decimal(2)
		self._speed = Decimal('30')
		self.calcBlock()

		super(Ship, self).__init__()

	# methods
	def calcBlock(self):		
		volume = self.length*self.beam*self.draft
		self._blockCoeff = self.displacement/volume
	def calcDisp(self):		
		volume = self.length*self.beam*self.draft
		self._displacement = Decimal(self.blockCoeff*volume)

	#getters & setters
	@observable
	def length(self):
		return self._length
	@length.setter
	def length(self, value):
		self._length = Decimal(value)

	@observable
	def beam(self):
		return self._beam
	@beam.setter
	def beam(self, value):
		self._beam = Decimal(value)
		
	@observable
	def draft(self):
		return self._draft
	@draft.setter
	def draft(self, value):
		self._draft = Decimal(value)

	@observable
	def displacement(self):
		return self._displacement
	@displacement.setter
	def displacement(self, value):
		self._displacement = Decimal(value)
		self.calcBlock()

	@observable
	def shaftCount(self):
		return self._shaftCount
	@shaftCount.setter
	def shaftCount(self, value):
		self._shaftCount = Decimal(value)

	@observable
	def speed(self):
		return self._speed
	@speed.setter
	def speed(self, value):
		self._speed = Decimal(value)

	@observable
	def blockCoeff(self):
		return self._blockCoeff
	@blockCoeff.setter
	def blockCoeff(self, value):
		self._blockCoeff = Decimal(value)
		self.calcDisp()

ship = Ship()