from functools import partial
from logic import constants, shipSpeedCalc
from logic.Property import AliasProperty, CalculatedProperty, Property
from logic.Ship import Ship
from logic.calculations.EngineEfficiency import EngineEfficiency
from logic.utils import ftToM, init_num, mToFt, readEnum, rem_zeros, roundOutBound, validateDecimal
import logic.Enums as enums

class Engine:
	def __init__(self, ship : Ship) -> None:
		self._ship = ship
	


	def init_props(self):
		
		self.fuelType = Property(enums.Fuel.COAL,
							processor=partial(readEnum, enums.Fuel))
		self.engineType = Property(enums.Engine.SIMPLE,
							processor=partial(readEnum, enums.Engine))
		self.coalPercent = Property(init_num(100),
								processor=validateDecimal,backProcessor=roundOutBound)
		
		self.maxSpeed = Property(init_num(25),
								processor=validateDecimal,backProcessor=roundOutBound)

		self.maxPowerkW = CalculatedProperty(partial(self.calclKWPower, self._ship), self._ship.hull.displacement,
								self._ship.hull.blockCoeff, self.maxSpeed,backProcessor=roundOutBound)
		self.maxPowerHP = CalculatedProperty(partial(self.kwToHP, self.maxPowerkW), 
								self.maxPowerkW,backProcessor=roundOutBound)

		self.engineEfficiency= CalculatedProperty(self.calcEngineEfficiency, self._ship.engineBuilt, 
								self.fuelType, self.engineType, self.coalPercent, backProcessor=roundOutBound)
								
		self.engineWeight = CalculatedProperty(self.calcEngineWeight, self.engineEfficiency, 
								self.maxPowerHP, backProcessor=roundOutBound)
	
	
	def kwToHP(self, kwPower : Property):
		return kwPower()*constants.HpPerKW
	def calcEngineWeight(self, *args, **kwds):
		return self.maxPowerHP() / self.engineEfficiency()

	
	def calclKWPower(self, *args, **kwds):
		try:
			return shipSpeedCalc.main(ship=self._ship)
		except:
			return init_num(0)
	def calcEngineEfficiency(self, *args, **kwds):
		ee = EngineEfficiency(self._ship)
		result = ee.calcEngineEfficiency()
		if result:
			return result
		else:
			return init_num(5)