from enum import Enum
from functools import partial
from tkinter.messagebox import QUESTION
from typing import Dict
from logic import shipSpeedCalc
from logic.components.ArmourBelt import ArmourBelt
from logic.Property import Property
import logic.Enums as enums
from logic.utils import ftToM, init_num, mToFt, readEnum, rem_zeros, roundOutBound, validateDecimal

class Ship:
	def __init__(self) -> None:

		from logic.components.Engine import Engine
		from logic.components.Hull import Hull

		self.name 			= Property('')
		self.country		= Property('')
		self.type 			= Property('')

		self.buildYear 		= Property(init_num(1920),
								processor=validateDecimal, outProcessor=roundOutBound)
		self.engineBuilt 	= Property(init_num(1920),
								processor=validateDecimal, outProcessor=roundOutBound)

		self.hull = Hull(self)
		self.engine = Engine(self)
		self.engine.init_props()


		self.armourBelts : Dict[enums.Belt, ArmourBelt]=  {}
		for belt in enums.Belt:
			self.armourBelts[belt] = ArmourBelt(belt)
		

#region Simple Calcs
#endregion
#region Outer Calls
#endregion
#region cleaning
	
#endregion