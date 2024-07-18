from decimal import Decimal
import constants
class Ship:
	def __init__(self) -> None:
		self.name = ''
		self.country = ''
		self.type = ''
		self._length = Decimal(180)
		self._lengthft = Decimal(0)
		self.beam = Decimal(20)
		self.draft = Decimal(6)
		self.displacement = Decimal(10000)	
		
#region Properties
	#region Hull Dimensions
		#region length
	@property
	def length(self) -> Decimal:
		return self._length
	def setLength(self, value):
		print(f'here: {value}')
		self._length = Decimal(value)
		#endregion
		#region beam
	@property
	def beam(self) -> Decimal:
		'''waterline beam of the ship in m'''
		return self._beam
	@beam.setter
	def beam(self, value : Decimal):
		self._beam = value
		self._beamft = value / constants.ftTometer
	@property
	def beamft(self) -> Decimal:
		'''waterline beam of the ship in ft'''
		return self._beam
	@beamft.setter
	def beamft(self, value : Decimal):
		self._beamft
		self._beam = value * constants.ftTometer
		#endregion
		#region draft
	@property
	def draft(self) -> Decimal:
		'''waterline draft of the ship in m'''
		return self._draft
	@draft.setter
	def draft(self, value : Decimal):
		self._draft = value
		self._draftft = value / constants.ftTometer
	@property
	def draftft(self) -> Decimal:
		'''waterline draft of the ship in ft'''
		return self._draft
	@draftft.setter
	def draftft(self, value : Decimal):
		self._draftft
		self._draft = value * constants.ftTometer
		#endregion
		#region displacement/block
	@property
	def displacement(self) -> Decimal:
		'''normal displacement of the ship'''
		return self._displacement
	@displacement.setter
	def displacement(self, value):
		self._displacement = Decimal(value)
		self._BlockCoefficient = self.calcBlock()
	@property
	def BlockCoefficient(self) -> Decimal:
		'''Block Coefficient of the ship'''
		return self._displacement
	@BlockCoefficient.setter
	def BlockCoefficient(self, value : Decimal):
		self._BlockCoefficient = value
		self._displacement = self.calcDisp()
		#endregion
	#endregion
	#region performance
		#region speed
	@property
	def maxSpeed(self) -> Decimal:
		'''maximum speed of the ship in knots'''
		return self._maxSpeed
	@maxSpeed.setter
	def maxSpeed(self, value : Decimal):
		self._maxSpeed = value
	@property
	def cruiseSpeed(self) -> Decimal:
		'''cruising speed of the ship in knots'''
		return self._cruisespeed
	@cruiseSpeed.setter
	def cruiseSpeed(self, value : Decimal):
		self._cruisespeed = value
		#endregion
		#region power
	@property
	def maxPowerHp(self) -> Decimal:
		'''waterline length of the ship in m'''
		return self._maxPowerHp
	@maxPowerHp.setter
	def maxPowerHp(self, value : Decimal):
		self._maxPowerHp = value
	@property
	def maxPowerKw(self) -> Decimal:
		'''waterline length of the ship in m'''
		return self._maxPowerKw
	@maxPowerKw.setter
	def maxPowerKw(self, value : Decimal):
		self._maxPowerKw = value
	@property
	def cruisePowerHp(self) -> Decimal:
		'''waterline length of the ship in m'''
		return self._cruisePowerHp
	@cruisePowerHp.setter
	def cruisePowerHp(self, value : Decimal):
		self._cruisePowerHp = value
	@property
	def cruisePowerKw(self) -> Decimal:
		'''waterline length of the ship in m'''
		return self._cruisePowerKw
	@cruisePowerKw.setter
	def cruisePowerKw(self, value : Decimal):
		self._cruisePowerKw = value
		#endregion
	#endregion
#endregion
#region calcs
	def calcBlock(self):
		return self.displacement/self.length/self.beam/self.draft
	def calcDisp(self):
		return self.BlockCoefficient*self.length*self.beam*self.draft
#endregion

	