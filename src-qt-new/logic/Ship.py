from decimal import Decimal, getcontext
from logic.Property import Property, CalculatedProperty
import constants
class Ship:
	def __init__(self) -> None:
		getcontext().prec = constants.precision

		self.name = Property('')
		self.country = Property('')
		self.type = Property('')
		self.length = Property(Decimal(180))
		self.length.addProcessor(self._validateDecimal)
		self.lengthft = CalculatedProperty(self.length)
		self.lengthft.addProcessor(self._validateDecimal).addProcessor(self.ftToM)
		self.lengthft.addBackProcessor(self.mToFt)

		self.beam = Property(Decimal(20))
		self.beam.addProcessor(self._validateDecimal)
		self.beamft = CalculatedProperty(self.beam)
		self.beamft.addProcessor(self._validateDecimal).addProcessor(self.ftToM)
		self.beamft.addBackProcessor(self.mToFt)

		self.draft = Property(Decimal(180))
		self.draft.addProcessor(self._validateDecimal)
		self.draftft = CalculatedProperty(self.draft)
		self.draftft.addProcessor(self._validateDecimal).addProcessor(self.ftToM)
		self.draftft.addBackProcessor(self.mToFt)

		self.displacement = Property(Decimal(10000))
		self.displacement.addProcessor(self._validateDecimal)
		self.blockCoeff = CalculatedProperty(self.displacement)
		self.blockCoeff.addProcessor(self._validateDecimal).addProcessor(self.blockToDisp)
		self.blockCoeff.addBackProcessor(self.dispToBlock)


#region calcs
	def ftToM(self,value) -> Decimal:
		return self._rem_zeros(value * constants.ftTometer)
	def mToFt(self,value) -> Decimal:
		return self._rem_zeros(value / constants.ftTometer)
	def _volume(self) -> Decimal:
		return self._rem_zeros(self.length()*self.beam()*self.draft())
	def dispToBlock(self, value) -> Decimal:
		return self._rem_zeros(value / self._volume())
	def blockToDisp(self, value) -> Decimal:
		return self._rem_zeros(value * self._volume())	

#endregion
#region cleaning
	def _validateDecimal(self, value):
		try:
			result = Decimal(value)
			return self._rem_zeros(result) 
		except:
			return False	
		#TODO: write actual validation logic; improper try usage
		
	def _rem_zeros(self, d : Decimal) -> Decimal:
		return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
#endregion

