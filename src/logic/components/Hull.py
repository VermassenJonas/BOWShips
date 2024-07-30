from logic.Property import CalculatedProperty, PassDown, Property
from logic.Ship import Ship
from logic.utils import ftToM, init_num, mToFt, rem_zeros, roundOutBound, validateDecimal


class Hull:
	def __init__(self, ship : Ship) -> None:
		self.length			= Property(init_num(180),
								processor=validateDecimal,outProcessor=roundOutBound)
	
		self.lengthft 		= CalculatedProperty(value=init_num(0),
										dependencies=[self.length], calcFun=mToFt,
										passDown=PassDown(self.length, ftToM),
										processor=validateDecimal, outProcessor=roundOutBound)

		self.beam			= Property(init_num(20),
								processor=validateDecimal, outProcessor=roundOutBound)
		self.beamft			= CalculatedProperty(value=init_num(0),
										dependencies=[self.beam], calcFun=mToFt,
										passDown=PassDown(self.beam, ftToM),
										processor=validateDecimal, outProcessor=roundOutBound)

		self.draft 			= Property(init_num(6),
								processor=validateDecimal,outProcessor=roundOutBound)

		self.draftft 		= CalculatedProperty(value=init_num(0),
										dependencies=[self.draft], calcFun=mToFt,
										passDown=PassDown(self.draft, ftToM),
										processor=validateDecimal, outProcessor=roundOutBound)

		self.blockVolume 	= CalculatedProperty(init_num(0), calcFun= self.calcBlockVolume, 
								dependencies =[self.length,	self.beam,self.draft],
								outProcessor=roundOutBound)

		self.displacement 	= Property(init_num(10000),
								processor=validateDecimal,outProcessor=roundOutBound)

		self.blockCoeff 	= CalculatedProperty(value=init_num(0.5), calcFun=self.dispToBlock,
							dependencies=[self.blockVolume, self.displacement], 
							passDown=PassDown(self.displacement, self.blockToDisp),
							processor=validateDecimal, outProcessor=roundOutBound)
	
	
	
	
	def calcBlockVolume(self, *args):
		length, beam, draft = self.length(), self.beam(), self.draft()	 
		return rem_zeros(length*beam*draft)
	
	def dispToBlock(self, value , *args, **kwds):
		return rem_zeros(value / self.blockVolume())
	def blockToDisp(self, value, *args, **kwds):
		return rem_zeros(value * self.blockVolume())	