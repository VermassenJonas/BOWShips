from enum import Enum


class Engine(Enum):
	SIMPLE 	= 'simple'
	COMPLEX = 'complex'
	TURBINE = 'turbine'
class Fuel(Enum):
	COAL 	= 'Coal'
	OIL 	= 'Oil'
	MIXED 	= 'Mixed'