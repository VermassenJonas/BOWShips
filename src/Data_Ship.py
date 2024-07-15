from PySide6.QtCore import QObject, Property

'''
length = 180
beam = 20
draft = 6
displacement = 10000
shaftCount = 2
speed = 30
def blockCoefficient():
	volume = length*beam*draft
	return displacement/volume
'''

class Ship(QObject):
	def __init__(self):
		QObject.__init__(self)
		self.length_ = 180

	def readLength(self):
		return self.length_

	def setLength(self, val):
		self.length_ = val

	length = Property(float, readLength, setLength)
ship = Ship()
