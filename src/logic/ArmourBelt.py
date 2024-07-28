from decimal import Decimal
from logic import constants
from logic.Property import AliasProperty, CalculatedProperty, Property
from logic.utils import ftToM, inToMm, init_num, mToFt, mmToIn, roundOutBound, validateDecimal
from logic.Enums import Belt


class ArmourBelt:
	def __init__(self, belt : Belt) -> None:
		self.name = belt
		self.length			= Property		(init_num(0),
											processor=validateDecimal,
											backProcessor=roundOutBound)
		self.height			= Property		(init_num(0),
											processor=validateDecimal,
											backProcessor=roundOutBound)
		self.thickness		= Property		(init_num(0),
											processor=validateDecimal,
											backProcessor=roundOutBound)

		self.lengthFt 		= AliasProperty	(self.length, downTransfo=ftToM, upTransfo=mToFt,
											processor=validateDecimal, backProcessor=roundOutBound)
		self.heightFt 		= AliasProperty	(self.height, downTransfo=ftToM, upTransfo=mToFt,
											processor=validateDecimal, backProcessor=roundOutBound)
		self.thicknessIn	= AliasProperty	(self.thickness, downTransfo=inToMm, upTransfo=mmToIn,
											processor=validateDecimal, backProcessor=roundOutBound)
		self.surface 		= CalculatedProperty(self.calcArmourSurface, self.length, self.height, backProcessor=roundOutBound)

		self.weight			= AliasProperty(property=self.thickness, downTransfo=self.weightToThickness, upTransfo=self.thicknessToWeight,
											processor=validateDecimal, backProcessor=roundOutBound, dependency=self.surface)

	def calcArmourSurface(self):
		return self.length()*self.height()*Decimal('2') #two sides to a ship

	def thicknessToWeight(self, thickness):
		surface = self.surface()
		return surface * thickness / constants.mmPerM * constants.armourDensity
	def weightToThickness(self, weight):
		surface = self.surface()
		return weight / (surface * constants.armourDensity / constants.mmPerM)
 