

from collections.abc import Callable
from typing import Any
from logic import constants
from logic.Enums import Deck
from logic.Property import CalculatedProperty, PassDown, Property
from logic.Ship import Ship
from logic.utils import ftToM, inToMm, init_num, mToFt, mmToIn, roundOutBound, validateDecimal


class ArmourDeck:
	def __init__(self, deck : Deck, coverageCoeff : Callable[[], Any], ship : Ship) -> None:
		self.ship = ship
		self.name = deck
		self.coverageCoeff = coverageCoeff
		self.thickness = Property(init_num(0),
								processor=validateDecimal,
								outProcessor=roundOutBound)
		self.length = Property(init_num(0),
								processor=validateDecimal,
								outProcessor=roundOutBound)
		self.thicknessIn	= CalculatedProperty(value=init_num(0), 
										dependencies=[self.thickness], calcFun=mmToIn,
										passDown=PassDown(self.thickness, inToMm),
										processor=validateDecimal, outProcessor=roundOutBound)
		self.lengthFt 		= CalculatedProperty(value=init_num(0),
										dependencies=[self.length], calcFun=mToFt,
										passDown=PassDown(self.length, ftToM),
										processor=validateDecimal, outProcessor=roundOutBound)
		
		self.weight = CalculatedProperty(value=init_num(0), 
						dependencies=[self.length, self.thickness],
						calcFun=self.thicknessToWeight, 
						passDown=PassDown(self.thickness, self.weightToThickness),
						processor=validateDecimal, outProcessor=roundOutBound)


	def thicknessToWeight(self, dependencies ):
		surface = self.length()*self.ship.hull.beam() * init_num(self.coverageCoeff())
		return surface * self.thickness() / constants.mmPerM * constants.armourDensity
	def weightToThickness(self, dependencies, weight):
		surface = self.length()*self.ship.hull.beam() * init_num(self.coverageCoeff())
		if surface:
			return weight / (surface * constants.armourDensity / constants.mmPerM)
		else:
			return init_num(0)  