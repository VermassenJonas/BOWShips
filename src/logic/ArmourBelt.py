from logic.Property import AliasProperty, Property
from logic.utils import ftToM, init_num, mToFt, roundOutBound, validateDecimal
from logic.Enums import Belt


class ArmourBelt:
	def __init__(self) -> None:
		self.name = Belt
		self.length			= Property		(init_num(0))
		self.height			= Property		(init_num(0))
		self.thickness		= Property		(init_num(0))

		self.lengthFt 		= AliasProperty	(self.length)
		self.heightFt 		= AliasProperty	(self.height)
		self.thicknessIn	= AliasProperty	(self.thickness)

		self.length			.addProcessor(validateDecimal)
		self.height			.addProcessor(validateDecimal)
		self.thickness		.addProcessor(validateDecimal)

		self.lengthFt 		.addProcessor(validateDecimal, ftToM)
		self.heightFt 		.addProcessor(validateDecimal, ftToM)
		self.thicknessIn	.addProcessor(validateDecimal, ftToM)

		self.length			.addBackProcessor(roundOutBound)	
		self.height			.addBackProcessor(roundOutBound)	
		self.thickness		.addBackProcessor(roundOutBound)
			
		self.lengthFt 		.addBackProcessor(mToFt, roundOutBound)	
		self.heightFt 		.addBackProcessor(mToFt, roundOutBound)	
		self.thicknessIn	.addBackProcessor(mToFt, roundOutBound)	
