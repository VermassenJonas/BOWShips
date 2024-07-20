from enum import Enum
from typing import Any


class Lang(object):
	main_title = "BOWShips: Build your Own Warships"
	hull = "Hull"
	freeboard = "Freeboard"
	ship_info = "Ship Info"
	report = "Report"
	ship_overview = 'Ship Overview'
	engine = 'Engine'
	engines = 'Engines'
	ship = 'Ship'
	name = 'Name'
	country = 'Country'
	type = 'Type'
	year = 'Year'
	dimensions = 'Dimensions'
	laid_down = 'Laid Down'
	engine_built = 'Engine Built'
	length = 'length'
	beam = 'beam'
	draft = 'draft'
	meter = 'meter'
	feet = 'feet'
	displacement = 'Displacement'
	block_coefficient = 'Block Coefficient'
	speed_and_power = 'Speed & Power'
	fuel = 'Fuel'
	maxSpeed = 'Max Speed'
	cruise_speed = 'Cruise Speed'
	shafts = 'Shafts'
	def __getattribute__(self, name: str) -> Any:
		try:
			return object.__getattribute__(self, name)
		except:
			return f'00{name}' #if you see this prefix, add translation.		
	def __call__(self, codeString : str, *args: Any, **kwds: Any) -> str:
		return self.__getattribute__(codeString)
lang = Lang()