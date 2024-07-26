from enum import Enum
from functools import partial
from tkinter.messagebox import QUESTION
from logic import shipSpeedCalc
from logic.Property import Property, AliasProperty, CalculatedProperty
from logic.calculations.EngineEfficiency import EngineEfficiency
import logic.constants as constants
import logic.Enums as enums
from logic.utils import ftToM, init_num, mToFt, readEnum, rem_zeros, roundOutBound, validateDecimal

class Ship:
	def __init__(self) -> None:

		self.name 			= Property('')
		self.country		= Property('')
		self.type 			= Property('')

		self.buildYear 		= Property(init_num(1920),
								processor=validateDecimal, backProcessor=roundOutBound)
		self.engineBuilt 	= Property(init_num(1920),
								processor=validateDecimal,backProcessor=roundOutBound)

		self.length			= Property(init_num(180),
								processor=validateDecimal,backProcessor=roundOutBound)
		self.lengthft 		= AliasProperty(self.length, downTransfo=ftToM, upTransfo=mToFt,
								processor=validateDecimal, backProcessor=roundOutBound)

		self.beam			= Property(init_num(20),
								processor=validateDecimal, backProcessor=roundOutBound)
		self.beamft			= AliasProperty(self.beam, downTransfo=ftToM, upTransfo=mToFt,
								processor=validateDecimal, backProcessor=roundOutBound)

		self.draft 			= Property(init_num(6),
								processor=validateDecimal,backProcessor=roundOutBound)

		self.draftft 		= AliasProperty(self.draft, downTransfo=ftToM, upTransfo=mToFt,
								processor=validateDecimal,backProcessor=roundOutBound)

		self.blockVolume 	= CalculatedProperty(self.calcBlockVolume, self.length, self.beam, self.draft,
								backProcessor=roundOutBound)

		self.displacement 	= Property(init_num(10000),
								processor=validateDecimal,backProcessor=roundOutBound)

		self.blockCoeff 	= AliasProperty(self.displacement, downTransfo=self.blockToDisp, upTransfo=self.dispToBlock,
								processor=validateDecimal,backProcessor=roundOutBound, dependency=self.blockVolume)

		self.fuelType = Property(enums.Fuel.COAL,
							processor=partial(readEnum, enums.Fuel))
		self.engineType = Property(enums.Engine.SIMPLE,
							processor=partial(readEnum, enums.Engine))
		self.coalPercent = Property(init_num(100),
								processor=validateDecimal,backProcessor=roundOutBound)
		
		self.maxSpeed = Property(init_num(25),
								processor=validateDecimal,backProcessor=roundOutBound)

		self.maxPowerkW = CalculatedProperty(partial(self.calclKWPower, self), self.displacement,
								self.blockCoeff, self.maxSpeed,backProcessor=roundOutBound)
		self.maxPowerHP = CalculatedProperty(partial(self.kwToHP, self.maxPowerkW), 
								self.maxPowerkW,backProcessor=roundOutBound)

		self.engineEfficiency= CalculatedProperty(self.calcEngineEfficiency, self.engineBuilt, 
								self.fuelType, self.engineType, self.coalPercent, backProcessor=roundOutBound)
								
		self.engineWeight = CalculatedProperty(self.calcEngineWeight, self.engineEfficiency, 
								self.maxPowerHP, backProcessor=roundOutBound)

#region Simple Calcs
	def calcBlockVolume(self):
		length, beam, draft = self.length(), self.beam(), self.draft()	 
		if not None in (length, beam, draft):
			return rem_zeros(length*beam*draft)#ignore
	def dispToBlock(self, newValue , *args, **kwds):
		return rem_zeros(newValue / self.blockVolume())
	def blockToDisp(self, newValue, *args, **kwds):
		return rem_zeros(newValue * self.blockVolume())	
	def kwToHP(self, kwPower : Property):
		return kwPower()*constants.kWtoHP
	def calcEngineWeight(self, *args, **kwds):
		return self.maxPowerHP() / self.engineEfficiency()
#endregion
#region Outer Calls
	def calclKWPower(self, *args, **kwds):
		try:
			return shipSpeedCalc.main(self)
		except:
			return init_num(0)
	def calcEngineEfficiency(self, *args, **kwds):
		ee = EngineEfficiency(self)
		result = ee.calcEngineEfficiency()
		if result:
			return result
		else:
			return init_num(5)
#endregion
#region cleaning
	
#endregion