from functools import partial
from logic import constants, shipSpeedCalc
from logic.Property import CalculatedProperty, Property
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
								processor=validateDecimal,outProcessor=roundOutBound)
		
		self.maxSpeed = Property(init_num(25),
								processor=validateDecimal,outProcessor=roundOutBound)

		self.maxPowerkW = CalculatedProperty(calcFun=self.calclKWPower, value=init_num(0), 
											dependencies=[self._ship.hull.displacement, self._ship.hull.blockCoeff, self.maxSpeed],
											outProcessor=roundOutBound)
		self.maxPowerHP = CalculatedProperty(value=init_num(0), calcFun=self.kwToHP, dependencies=[self.maxPowerkW],
											outProcessor=roundOutBound)

		self.engineEfficiency= CalculatedProperty(value=init_num(0), calcFun=self.calcEngineEfficiency,
									dependencies=[self._ship.engineBuilt, self.fuelType, self.engineType, self.coalPercent],
									outProcessor=roundOutBound)
								
		self.engineWeight = CalculatedProperty(value=init_num(0), calcFun=self.calcEngineWeight,
							dependencies=[self.engineEfficiency, self.maxPowerHP], outProcessor=roundOutBound)
		#CalculatedProperty(self.calcEngineWeight, self.engineEfficiency, 
		#						self.maxPowerHP, outProcessor=roundOutBound)
	
	
	def kwToHP(self, *args):
		return self.maxPowerkW()*constants.HpPerKW
	def calcEngineWeight(self, *args):
		return self.maxPowerHP() / self.engineEfficiency()

	
	def calclKWPower(self, *args):
		try:
			return shipSpeedCalc.main(ship=self._ship)
		except:
			return init_num(0)
	def calcEngineEfficiency(self, *args):
		ee = EngineEfficiency(self._ship)
		result = ee.calcEngineEfficiency()
		if result:
			return result
		else:
			return init_num(5)