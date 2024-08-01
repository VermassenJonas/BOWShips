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
	MAIN_BELT 		= auto()
	UPPER_BELT 	= auto()
	EXTENDED_BELT 	= auto()
	TORPEDO_BELT 	= auto()
	MACHINERY_BELT 	= auto()
	MAGAZINES_BELT 	= auto()
class DeckLayout(StrEnum):
	ARMOURED = auto()
	PROTECTED = auto()
class Deck(StrEnum):
	MAIN = auto()
	FORE = auto()
	AFT = auto()





