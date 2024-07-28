from logic.Property import AliasProperty, CalculatedProperty, Property
from logic.utils import ftToM, init_num, mToFt, rem_zeros, roundOutBound, validateDecimal


class Hull:
	def __init__(self) -> None:
		self.length			= Property(init_num(180),
								processor=validateDecimal,backProcessor=roundOutBound)
		self.lengthft 		= AliasProperty(self.length, downTransfo=ftToM, upTransfo=mToFt,
								processor=validateDecimal, backProcessor=roundOutBound)

		self.beam			= Property(init_num(20),
								processor=validateDecimal, backProcessor=roundOutBound)
		self.beamft			= AliasProperty(self.beam, downTransfo=ftToM, upTransfo=mToFt,
								processor=validateDecimal, backProcessor=roundOutBound)

		self.draft 			= Property(init_num(6),
								processor=validateDecimal,backProcessor=roundOutBound)

		self.draftft 		= AliasProperty(self.draft, downTransfo=ftToM, upTransfo=mToFt,
								processor=validateDecimal,backProcessor=roundOutBound)

		self.blockVolume 	= CalculatedProperty(self.calcBlockVolume, self.length, self.beam, self.draft,
								backProcessor=roundOutBound)

		self.displacement 	= Property(init_num(10000),
								processor=validateDecimal,backProcessor=roundOutBound)

		self.blockCoeff 	= AliasProperty(self.displacement, downTransfo=self.blockToDisp, upTransfo=self.dispToBlock,
								processor=validateDecimal,backProcessor=roundOutBound, dependency=self.blockVolume)
	
	
	
	
	def calcBlockVolume(self):
		length, beam, draft = self.length(), self.beam(), self.draft()	 
		if not None in (length, beam, draft):
			return rem_zeros(length*beam*draft)
	
	def dispToBlock(self, value , *args, **kwds):
		return rem_zeros(value / self.blockVolume())
	def blockToDisp(self, value, *args, **kwds):
		return rem_zeros(value * self.blockVolume())	