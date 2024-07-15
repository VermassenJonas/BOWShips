from PySide6.QtCore import QObject, Property


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

class Ship(object):
	def __init__(self):
		self.callbacks = []

		self.length = 180
		self.beam = 20
		self.draft = 6
		self.displacement = 10000
		self.shaftCount = 2
		self.speed = 30

	def subscribe(self, callback):
		self.callbacks.append(callback)
	def fire(self, **attrs):
		e = Event()
		e.source = self
		for k, v in attrs.items():
			setattr(e, k, v)
		for fn in self.callbacks:
			fn(e)
	def blockCoefficient():
		volume = self.length*self.beam*self.draft
		return displacement/volume
	def setBlockCoefficient(block):
		self.displacement = block*self.length*self.beam*self.draft

ship = Ship()