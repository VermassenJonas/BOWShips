from decimal import Decimal, getcontext
import constants
class Ship:
	def __init__(self) -> None:
		getcontext().prec = constants.precision
		self.name = ''
		self.country = ''
		self.type = ''
		self._length = Decimal(180)
		self._beam = Decimal(20)
		self._draft = Decimal(6)
		self._displacement = Decimal(10000)	
		
#region Properties
	#region Hull Dimensions
	def length(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self.validateDecimal(value):
			self._length = Decimal(value)
		return self.rem_zeros(self._length)
	def lengthft(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self.validateDecimal(value):
			self._length = Decimal(value) * constants.ftTometer
		return self.rem_zeros(self._length / constants.ftTometer)
	def beam(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self.validateDecimal(value):
			self._beam = Decimal(value)
		return self.rem_zeros(self._beam)
	def beamft(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self.validateDecimal(value):
			self._beam = Decimal(value) * constants.ftTometer
		return self.rem_zeros(self._beam / constants.ftTometer)
	def draft(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self.validateDecimal(value):
			self._draft = Decimal(value)
		return self.rem_zeros(self._draft)
	def draftft(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self.validateDecimal(value):
			self._draft = Decimal(value) * constants.ftTometer
		return self.rem_zeros(self._draft / constants.ftTometer)
	def displacement(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self.validateDecimal(value):
			self._displacement = Decimal(value)
		return self.rem_zeros(self._displacement)
	def blockCoeff(self, value=None, val_fn = None, *args) -> Decimal:
		if val_fn:
			value = val_fn()
		if self.validateDecimal(value):
			self._displacement = Decimal(value) * self.volume()
		return self.rem_zeros(self._displacement / self.volume())
	#endregion
	#region speed & power

	#endregion
#endregion
#region calcs
	def volume(self):
		return self.rem_zeros(self._length*self._beam*self._draft)
#endregion
#region cleaning
	def validateDecimal(self, value):
		try:
			Decimal(value)
			return True
		except:
			return False	
		#TODO: improve validation logic; improper try usage
		
	def rem_zeros(self, d : Decimal) -> Decimal:
		return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
#endregion