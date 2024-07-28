from enum import Enum
from functools import partial
from tkinter.messagebox import QUESTION
from typing import Dict
from logic import shipSpeedCalc
from logic.components.ArmourBelt import ArmourBelt
from logic.Property import Property, AliasProperty, CalculatedProperty
from logic.calculations.EngineEfficiency import EngineEfficiency
from logic.components.Hull import Hull
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

		self.hull = Hull()

		
		self.armourBelts : Dict[enums.Belt, ArmourBelt]=  {}
		for belt in enums.Belt:
			self.armourBelts[belt] = ArmourBelt(belt)
		

#region Simple Calcs
	
	def kwToHP(self, kwPower : Property):
		return kwPower()*constants.HpPerKW
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