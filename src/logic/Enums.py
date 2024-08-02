from enum import StrEnum, auto
from tkinter import EXTENDED


class Unit(StrEnum):
	METRIC 	= auto()
	IMPERIAL	= auto()
class Engine(StrEnum):
	SIMPLE 	= auto()
	COMPLEX 	= auto()
	TURBINE 	= auto()	
class Fuel(StrEnum):
	COAL 		= auto()
	OIL 		= auto()
	MIXED 		= auto()
class Belt(StrEnum):
	MAIN_BELT 		= auto()
	UPPER_BELT 	= auto()
	EXTENDED_BELT 	= auto()
	TORPEDO_BELT 	= auto()
	MACHINERY_BELT = auto()
	MAGAZINES_BELT = auto()
class DeckLayout(StrEnum):
	ARMOURED = auto()
	PROTECTED = auto()
class Deck(StrEnum):
	MAIN_DECK = auto()
	FORE_DECK = auto()
	AFT_DECK = auto()
class Battery(StrEnum):
	BATTERY_1	= auto()
	BATTERY_2	= auto()
	BATTERY_3	= auto()
	BATTERY_4	= auto()
	BATTERY_5	= auto()
	BATTERY_6	= auto()

 



