from decimal import Decimal, getcontext
import constants
class Ship:
	def __init__(self) -> None:
		getcontext().prec = 8
		self.name = ''
		self.country = ''
		self.type = ''
		self._length = Decimal(180)
		self.beam = Decimal(20)
		self.draft = Decimal(6)
		self.displacement = Decimal(10000)	
		
#region Properties
	#region Hull Dimensions
	def length(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if value and self.validateDecimal(value):
			self._length = Decimal(value)
		return self._length
	def lengthft(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if value and self.validateDecimal(value):
			self._length = Decimal(value) / constants.ftTometer
		return self._length * constants.ftTometer
	#endregion
#endregion
#region calcs
	def calcBlock(self):
		return self.displacement/self.length/self.beam/self.draft
	def calcDisp(self):
		return self.BlockCoefficient*self.length*self.beam*self.draft
#endregion
	def validateDecimal(self, value):
		try:
			Decimal(value)
			return True
		except:
			return False
		#TODO: improve validation logic; improper try usage
	