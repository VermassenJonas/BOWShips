from enum import StrEnum, auto


class Engine(StrEnum):
	SIMPLE = auto()
	COMPLEX =  auto()
	TURBINE =  auto()
	
class Fuel(StrEnum):
	COAL 	=  auto()
	OIL 	=  auto()
	MIXED 	=  auto()