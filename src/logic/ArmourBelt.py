from logic.Property import AliasProperty, Property
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
