from decimal import Decimal, getcontext
from enum import Enum
from functools import partial
from logic.Property import DependentAliasProperty, Property, AliasProperty, CalculatedProperty
import logic.constants as constants
import logic.Enums as enums
class Ship:
	def __init__(self) -> None:
		getcontext().prec = constants.precision

		self.name 		= Property('')
		self.country	= Property('')
		self.type 		= Property('')

		self.buildYear 		= Property(Decimal(1920))
		self.engineBuilt 	= Property(Decimal(1920))

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

		self.fuelType = Property(enums.Fuel.COAL)
		self.fuelType.addProcessor(partial(self.readEnum, enums.Fuel))
		self.engineType = Property(enums.Engine.SIMPLE)
		self.engineType.addProcessor(partial(self.readEnum, enums.Engine))
		self.coalPercent = Property(Decimal(100))

		self.blockCoeff = DependentAliasProperty(self.displacement, self.blockVolume)
		self.blockCoeff.addProcessor(self._validateDecimal,self.blockToDisp)
		self.blockCoeff.addBackProcessor(self.dispToBlock)

#region calcs
	def ftToM(self,newValue : Decimal, *args, **kwds) -> Decimal:
		return self._rem_zeros(newValue * constants.ftTometer)
	def mToFt(self,newValue : Decimal, *args, **kwds) -> Decimal:
		return self._rem_zeros(newValue / constants.ftTometer)
	def calcBlockVolume(self) -> Decimal:

		return self._rem_zeros(self.length()*self.beam()*self.draft())
	def dispToBlock(self, newValue : Decimal, *args, **kwds) -> Decimal:
		return self._rem_zeros(newValue / self.blockVolume())
	def blockToDisp(self, newValue : Decimal, *args, **kwds) -> Decimal:
		return self._rem_zeros(newValue * self.blockVolume())	

#endregion
#region cleaning
	def _validateDecimal(self, newValue, *args, **kwds):
		try:
			result = Decimal(newValue)
			return self._rem_zeros(result) 
		except:
			return None	
		#TODO: write actual validation logic; improper try usage
		
	def _rem_zeros(self, d : Decimal) -> Decimal:
		return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

	def readEnum(self, enum, newValue, *args, **kwds):
		if newValue:
			return enum[newValue]
		else:
			return None 
#endregion