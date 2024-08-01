from logic import constants
from logic.Property import CalculatedProperty, PassDown, Property
from logic.utils import ftToM, inToMm, init_num, mToFt, mmToIn, roundOutBound, validateDecimal
from logic.Enums import Belt


class ArmourBelt:
	def __init__(self, belt : Belt) -> None:
		self.name = belt
		self.length			= Property	(init_num(0),
										processor=validateDecimal,
										outProcessor=roundOutBound)
		self.height			= Property	(init_num(0), 
										processor=validateDecimal,
										outProcessor=roundOutBound)
		self.thickness		= Property	(init_num(0),
										processor=validateDecimal,
										outProcessor=roundOutBound)

		self.lengthFt 		= CalculatedProperty(value=init_num(0),
										dependencies=[self.length], calcFun=mToFt,
										passDown=PassDown(self.length, ftToM),
										processor=validateDecimal, outProcessor=roundOutBound)
		self.heightFt 		= CalculatedProperty(value=init_num(0), 
										dependencies=[self.height], calcFun=mToFt,
										passDown=PassDown(self.height, ftToM),
										processor=validateDecimal, outProcessor=roundOutBound)
		self.thicknessIn	= CalculatedProperty(value=init_num(0), 
										dependencies=[self.thickness], calcFun=mmToIn,
										passDown=PassDown(self.thickness, inToMm),
										processor=validateDecimal, outProcessor=roundOutBound)
		
		self.weight = CalculatedProperty(value=init_num(0), 
						dependencies=[self.length, self.height, self.thickness],
						calcFun=self.thicknessToWeight, 
						passDown=PassDown(self.thickness, self.weightToThickness),
						processor=validateDecimal, outProcessor=roundOutBound)


	def thicknessToWeight(self, dependencies ):
		surface = self.length()*self.height()*init_num('2') #two sides to a ship
		return surface * self.thickness() / constants.mmPerM * constants.armourDensity
	def weightToThickness(self, dependencies, weight):
		surface = self.length()*self.height()*init_num('2') #two sides to a ship
		return weight / (surface * constants.armourDensity / constants.mmPerM)
 