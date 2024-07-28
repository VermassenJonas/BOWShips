from functools import partial
from logic.Property import AliasProperty, CalculatedProperty, Property
from logic.Ship import Ship
from logic.utils import ftToM, init_num, mToFt, readEnum, rem_zeros, roundOutBound, validateDecimal
import logic.Enums as enums

class Engine:
	def __init__(self, ship : Ship) -> None:
		self.fuelType = Property(enums.Fuel.COAL,
							processor=partial(readEnum, enums.Fuel))
		self.engineType = Property(enums.Engine.SIMPLE,
							processor=partial(readEnum, enums.Engine))
		self.coalPercent = Property(init_num(100),
								processor=validateDecimal,backProcessor=roundOutBound)
		
		self.maxSpeed = Property(init_num(25),
								processor=validateDecimal,backProcessor=roundOutBound)

		self.maxPowerkW = CalculatedProperty(partial(self.calclKWPower, self), self.hull.displacement,
								self.hull.blockCoeff, self.maxSpeed,backProcessor=roundOutBound)
		self.maxPowerHP = CalculatedProperty(partial(self.kwToHP, self.maxPowerkW), 
								self.maxPowerkW,backProcessor=roundOutBound)

		self.engineEfficiency= CalculatedProperty(self.calcEngineEfficiency, self.engineBuilt, 
								self.fuelType, self.engineType, self.coalPercent, backProcessor=roundOutBound)
								
		self.engineWeight = CalculatedProperty(self.calcEngineWeight, self.engineEfficiency, 
								self.maxPowerHP, backProcessor=roundOutBound)
		