from decimal import Decimal, getcontext
import decimal
from enum import Enum
from functools import partial
from logic import shipSpeedCalc
from logic.Property import DependentAliasProperty, Property, AliasProperty, CalculatedProperty
import logic.constants as constants
import logic.Enums as enums
class Ship:
	def __init__(self) -> None:
		getcontext().prec = constants.precision

		self.name 			= Property('')
		self.country		= Property('')
		self.type 			= Property('')

		self.buildYear 		= Property(Decimal(1920))
		self.engineBuilt 	= Property(Decimal(1920))

		self.length			= Property(Decimal(180))
		self.length			.addProcessor(self._validateDecimal)
		self.length			.addBackProcessor(self.roundOutBound)
		self.lengthft 		= AliasProperty(self.length)
		self.lengthft		.addProcessor(self._validateDecimal, self.ftToM)
		self.lengthft		.addBackProcessor(self.mToFt, self.roundOutBound)

		self.beam			= Property(Decimal(20))
		self.beam			.addProcessor(self._validateDecimal)
		self.beam			.addBackProcessor(self.roundOutBound)
		self.beamft			= AliasProperty(self.beam)
		self.beamft			.addProcessor(self._validateDecimal,self.ftToM)
		self.beamft			.addBackProcessor(self.mToFt, self.roundOutBound)

		self.draft 			= Property(Decimal(6))
		self.draft			.addProcessor(self._validateDecimal)
		self.draft			.addBackProcessor(self.roundOutBound)
		self.draftft 		= AliasProperty(self.draft)
		self.draftft		.addProcessor(self._validateDecimal,self.ftToM)
		self.draftft		.addBackProcessor(self.mToFt, self.roundOutBound)

		self.blockVolume 	= CalculatedProperty(self.calcBlockVolume, self.length, self.beam, self.draft)
		self.blockVolume	.addBackProcessor(self.roundOutBound)

		self.displacement 	= Property(Decimal(10000))
		self.displacement	.addProcessor(self._validateDecimal)
		self.displacement	.addBackProcessor(self.roundOutBound)
		self.blockCoeff 	= DependentAliasProperty(self.displacement, self.blockVolume)
		self.blockCoeff		.addProcessor(self._validateDecimal,self.blockToDisp)
		self.blockCoeff		.addBackProcessor(self.dispToBlock, self.roundOutBound)

		self.fuelType = Property(enums.Fuel.COAL)
		self.fuelType.addProcessor(partial(self.readEnum, enums.Fuel))
		self.engineType = Property(enums.Engine.SIMPLE)
		self.engineType.addProcessor(partial(self.readEnum, enums.Engine))
		self.coalPercent = Property(Decimal('100'))
		self.coalPercent.addProcessor(self._validateDecimal)
		self.coalPercent.addBackProcessor(self.roundOutBound)


		
		self.maxSpeed = Property(Decimal(25))
		self.maxSpeed.addProcessor(self._validateDecimal)
		self.maxSpeed.addBackProcessor(self.roundOutBound)

		self.maxPowerkW = CalculatedProperty(partial(self.calclKWPower, self), self.displacement, self.blockCoeff, self.maxSpeed) 
		self.maxPowerkW.addProcessor(self._validateDecimal)
		self.maxPowerHP = CalculatedProperty(partial(self.kwToHP, self.maxPowerkW) , self.maxPowerkW)

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
	def kwToHP(self, kwPower : Property[Decimal]):
		return kwPower()*constants.kWtoHP

	def calclKWPower(self, *args, **kwds):
		try:
			return shipSpeedCalc.main(self)
		except:
			return 0

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

	def readEnum(self, enum, newValue : str, *args, **kwds):
		if newValue:
			return enum[newValue.upper()]
		else:
			return None 

	def roundOutBound(self, val: Decimal, *args, **kwds):
		return self._rem_zeros(val.quantize(Decimal(constants.roundTo)))
#endregion