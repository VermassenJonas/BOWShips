from decimal import Decimal
from logic.Property import Property, AliasProperty, CalculatedProperty

class Ship:
	def __init__(self) -> None:
		self.length = Property(Decimal(180))
		self.length.addProcessor(self._validateDecimal)
		self.lengthft = AliasProperty(self.length)
		self.lengthft.addProcessor(self._validateDecimal, self.ftToM)
		self.lengthft.addBackProcessor(self.mToFt)

		self.beam = Property(Decimal(20))
		self.beam.addProcessor(self._validateDecimal)
		self.beamft = AliasProperty(self.beam)
		self.beamft.addProcessor(self._validateDecimal,self.ftToM)
		self.beamft.addBackProcessor(self.mToFt)

		self.draft = Property(Decimal(180))
		self.draft.addProcessor(self._validateDecimal)
		self.draftft = AliasProperty(self.draft)
		self.draftft.addProcessor(self._validateDecimal,self.ftToM)
		self.draftft.addBackProcessor(self.mToFt)
