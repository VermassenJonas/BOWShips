from enum import StrEnum, auto


class Engine(StrEnum):
	SIMPLE 	= auto()
	COMPLEX 	= auto()
	TURBINE 	= auto()
	
class Fuel(StrEnum):
	COAL 		= auto()
	OIL 		= auto()
	MIXED 		= auto()
class UnitBig(StrEnum):
	METER 		= auto()
	FOOT		= auto()
class UnitSmall(StrEnum):
	MM 			= auto()
	INCH = auto()
class unitTon(StrEnum):
	METRIC = auto()
	LONG = auto()
	SHORT = auto()


