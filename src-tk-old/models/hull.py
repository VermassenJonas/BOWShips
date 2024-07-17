

class Hull:
	def __init__(self):
		self.beam = 20
		self._length = 180
		self.draft = 6
		self.displacement = 10000
		self.shaftCount = 1	
	@property
	def length(self):
		return self._length
	@length.setter
	def length(self, value):
		self._length = value
		print(value)

