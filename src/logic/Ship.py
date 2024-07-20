from decimal import Decimal, getcontext
from enum import Enum
from functools import partial
from logic.Property import Property, AliasProperty, CalculatedProperty
import logic.constants as constants
import logic.Enums as enums
class Ship:
	def __init__(self) -> None:
		getcontext().prec = constants.precision

		self.name 		= Property('')
		self.country	= Property('')
		self.type 		= Property('')

		self.length = Property(Decimal(180))
		self.length.addProcessor(self._validateDecimal)
		self.lengthft = AliasProperty(self.length)
		self.lengthft.addProcessor(self._validateDecimal, self.ftToM)
		self.lengthft.addBackProcessor(self.mToFt)

		self.beam = Property(Decimal(20))
		self.beam.addProcessor(self._validateDecimal)
		self.beamft = AliasProperty(self.beam)
		self.beamft.addProcessor(self._validateDecimal,self.ftToM)
		self.beamft.addBackProcessor(self.mToFt)

		self.draft = Property(Decimal(180))
		self.draft.addProcessor(self._validateDecimal)
		self.draftft = AliasProperty(self.draft)
		self.draftft.addProcessor(self._validateDecimal,self.ftToM)
		self.draftft.addBackProcessor(self.mToFt)

		self.blockVolume = CalculatedProperty(self.calcBlockVolume, self.length, self.beam, self.draft)

		self.displacement = Property(Decimal(10000))
		self.displacement.addProcessor(self._validateDecimal)
		self.blockCoeff = AliasProperty(self.displacement)
		self.blockCoeff.addProcessor(self._validateDecimal,self.blockToDisp)
		self.blockCoeff.addBackProcessor(self.dispToBlock)

		self.fuelType = Property(enums.Fuel.COAL)
		self.fuelType.addProcessor(partial(self.readEnum, enums.Fuel))
		self.engineType = Property(enums.Engine.SIMPLE)
		self.engineType.addProcessor(partial(self.readEnum, enums.Engine))
		self.coalPercent = Property(Decimal(100))


#region calcs
	def ftToM(self,value, old=None) -> Decimal:
		return self._rem_zeros(value * constants.ftTometer)
	def mToFt(self,value, old=None) -> Decimal:
		return self._rem_zeros(value / constants.ftTometer)
	def calcBlockVolume(self) -> Decimal:
		return self._rem_zeros(self.length()*self.beam()*self.draft())
	def dispToBlock(self, value, old=None) -> Decimal:
		return self._rem_zeros(value / self.blockVolume())
	def blockToDisp(self, value, old=None) -> Decimal:
		return self._rem_zeros(value * self.blockVolume())	

#endregion
#region cleaning
	def _validateDecimal(self, value, old=None):
		try:
			result = Decimal(value)
			return self._rem_zeros(result) 
		except:
			return False	
		#TODO: write actual validation logic; improper try usage
		
	def _rem_zeros(self, d : Decimal) -> Decimal:
		return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

	def readEnum(self, enum : Enum, name : str | None):
		if name:
			return enum[name]
		else:
			return False 
#endregion