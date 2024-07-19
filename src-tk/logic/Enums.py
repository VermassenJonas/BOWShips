from enum import Enum


class Engine(Enum):
	SIMPLE 	= 'simple'
	COMPLEX = 'complex'
	TURBINE = 'turbine'
class Fuel(Enum):
	OIL 	= 'oil'
	COAL 	= 'coal'
	BOTH 	= 'both'