from enum import StrEnum, auto
from tkinter import EXTENDED


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
class Belt(StrEnum):
	MAIN 		= auto()
	UPPER 		= auto()
	EXTENDED 	= auto()
	TORPEDO 	= auto()
	MACHINERY 	= auto()
	MAGAZINES 	= auto()




