from enum import StrEnum, auto


class Engine(StrEnum):
	SIMPLE 	= auto()
	COMPLEX 	= auto()
	TURBINE 	= auto()
	
class Fuel(StrEnum):
	COAL 		= auto()
	OIL 		= auto()
	MIXED 		= auto()
class Unit(StrEnum):
	METRIC 	= auto()
	IMPERIAL	= auto()
#class Magnitude(StrEnum):
#	METER		= auto()
#	MM 		= auto()



