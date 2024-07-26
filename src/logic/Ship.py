from enum import Enum
from functools import partial
from tkinter.messagebox import QUESTION
from logic import shipSpeedCalc
from logic.Property import DependentAliasProperty, Property, AliasProperty, CalculatedProperty
from logic.calculations.EngineEfficiency import EngineEfficiency
import logic.constants as constants
import logic.Enums as enums
from logic.utils import ftToM, init_num, mToFt, readEnum, rem_zeros, roundOutBound, validateDecimal

class Ship:
	def __init__(self) -> None:

		self.name 			= Property('')
		self.country		= Property('')
		self.type 			= Property('')

		self.buildYear 		= Property(init_num(1920))
		self.buildYear 		.addProcessor(validateDecimal)
		self.buildYear 		.addBackProcessor(roundOutBound)
		self.engineBuilt 	= Property(init_num(1920))
		self.engineBuilt	.addProcessor(validateDecimal)
		self.engineBuilt	.addBackProcessor(roundOutBound)

		self.length			= Property(init_num(180))
		self.length			.addProcessor(validateDecimal)
		self.length			.addBackProcessor(roundOutBound)
		self.lengthft 		= AliasProperty(self.length)
		self.lengthft		.addProcessor(validateDecimal, ftToM)
		self.lengthft		.addBackProcessor(mToFt, roundOutBound)

		self.beam			= Property(init_num(20))
		self.beam			.addProcessor(validateDecimal)
		self.beam			.addBackProcessor(roundOutBound)
		self.beamft			= AliasProperty(self.beam)
		self.beamft			.addProcessor(validateDecimal,ftToM)
		self.beamft			.addBackProcessor(mToFt, roundOutBound)

		self.draft 			= Property(init_num(6))
		self.draft			.addProcessor(validateDecimal)
		self.draft			.addBackProcessor(roundOutBound)
		self.draftft 		= AliasProperty(self.draft)
		self.draftft		.addProcessor(validateDecimal,ftToM)
		self.draftft		.addBackProcessor(mToFt, roundOutBound)

		self.blockVolume 	= CalculatedProperty(self.calcBlockVolume, self.length, self.beam, self.draft)
		self.blockVolume	.addBackProcessor(roundOutBound)

		self.displacement 	= Property(init_num(10000))
		self.displacement	.addProcessor(validateDecimal)
		self.displacement	.addBackProcessor(roundOutBound)

		self.blockCoeff 	= DependentAliasProperty(self.displacement, self.blockVolume)
		self.blockCoeff		.addProcessor(validateDecimal,self.blockToDisp)
		self.blockCoeff		.addBackProcessor(self.dispToBlock,roundOutBound)

		self.fuelType = Property(enums.Fuel.COAL)
		self.fuelType.addProcessor(partial(readEnum, enums.Fuel))
		self.engineType = Property(enums.Engine.SIMPLE)
		self.engineType.addProcessor(partial(readEnum, enums.Engine))
		self.coalPercent = Property(init_num(100))
		self.coalPercent.addProcessor(validateDecimal)
		self.coalPercent.addBackProcessor(roundOutBound)
		
		self.maxSpeed = Property(init_num(25))
		self.maxSpeed.addProcessor(validateDecimal)
		self.maxSpeed.addBackProcessor(roundOutBound)

		self.maxPowerkW = CalculatedProperty(partial(self.calclKWPower, self), self.displacement, self.blockCoeff, self.maxSpeed) 
		self.maxPowerkW.addProcessor(validateDecimal)
		self.maxPowerkW.addBackProcessor(roundOutBound)
		self.maxPowerHP = CalculatedProperty(partial(self.kwToHP, self.maxPowerkW) , self.maxPowerkW)
		self.maxPowerHP.addBackProcessor(roundOutBound)

		self.engineEfficiency= CalculatedProperty(self.calcEngineEfficiency, self.engineBuilt, self.fuelType, self.engineType, self.coalPercent)
		self.engineEfficiency.addBackProcessor(roundOutBound) 
		self.engineWeight 		= CalculatedProperty(self.calcEngineWeight, self.engineEfficiency, self.maxPowerHP)
		self.engineWeight.addBackProcessor(roundOutBound)

#region Simple Calcs
	def calcBlockVolume(self):

		return rem_zeros(self.length()*self.beam()*self.draft())
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