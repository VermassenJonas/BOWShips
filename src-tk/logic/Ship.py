from decimal import Decimal, getcontext
from logic.Property import Property, CalculatedProperty
import constants
class Ship:
	def __init__(self) -> None:
		getcontext().prec = constants.precision
		self.length = Property(Decimal(180))
		self.length.addProcessor(self._validateDecimal).addProcessor(self._rem_zeros)
		self.lengthft = CalculatedProperty(self.length)
		self.lengthft.addProcessor(self._validateDecimal).addProcessor(self.ftToM)
		self.lengthft.addBackProcessor(self.mToFt).addBackProcessor(self._rem_zeros)

		
		self.name = ''
		self.country = ''
		self.type = ''
		self._beam = Decimal(20)
		self._draft = Decimal(6)
		self._displacement = Decimal(10000)	

		
#region Properties
	#region Hull Dimensions
	def beam(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self._validateDecimal(value):
			self._beam = Decimal(value)
		return self._rem_zeros(self._beam)
	def beamft(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self._validateDecimal(value):
			self._beam = Decimal(value) * constants.ftTometer
		return self._rem_zeros(self._beam / constants.ftTometer)
	def draft(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self._validateDecimal(value):
			self._draft = Decimal(value)
		return self._rem_zeros(self._draft)
	def draftft(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self._validateDecimal(value):
			self._draft = Decimal(value) * constants.ftTometer
		return self._rem_zeros(self._draft / constants.ftTometer)
	def displacement(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self._validateDecimal(value):
			self._displacement = Decimal(value)
		return self._rem_zeros(self._displacement)
	def blockCoeff(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self._validateDecimal(value):
			self._displacement = Decimal(value) * self._volume()
		return self._rem_zeros(self._displacement / self._volume())
	#endregion
	#region speed & power

	#endregion
#endregion
#region calcs
	def _volume(self):
		return self._rem_zeros(self.length.value*self._beam*self._draft)
	def ftToM(self,value):
		return value * constants.ftTometer
	def mToFt(self,value):
		return value / constants.ftTometer
#endregion
#region cleaning
	def _validateDecimal(self, value):
		try:
			result = Decimal(value)
			return result 
		except:
			return False	
		#TODO: improve validation logic; improper try usage
		
	def _rem_zeros(self, d : Decimal) -> Decimal:
		return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
#endregion

