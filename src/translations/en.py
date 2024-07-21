from enum import Enum
from importlib import simple
from typing import Any

_trans_dict = {
		'main_title' 		: "BOWShips: Build your Own Warships",
		'hull' 				: "Hull",
		'freeboard' 		: "Freeboard",
		'ship_info' 		: "Ship Info",
		'report' 			: "Report",
		'ship_overview' 	: 'Ship Overview',
		'engine' 			: 'Engine',
		'engines' 			: 'Engines',
		'ship' 				: 'Ship',
		'name' 				: 'Name',
		'country' 			: 'Country',
		'type' 				: 'Type',
		'year' 				: 'Year',
		'dimensions' 		: 'Dimensions',
		'laid_down' 		: 'Laid Down',
		'engine_built' 		: 'Engine Built',
		'length' 			: 'length',
		'beam' 				: 'beam',
		'draft' 			: 'draft',
		'meter' 			: 'meter',
		'feet' 				: 'feet',
		'displacement' 		: 'Displacement',
		'block_coefficient' : 'Block Coefficient',
		'speed_and_power' 	: 'Speed & Power',
		'fuel' 				: 'Fuel',
		'maxSpeed' 			: 'Max Speed',
		'cruise_speed' 		: 'Cruise Speed',
		'shafts' 			: 'Shafts',
		'engine_type' 		: 'Engine Type',
		'Coal' : 'Coal',
		'Mixed' : 'Mixed',
		'Oil':'Oil',
		'simple' : 'Simple',
		'complex' : 'Complex',
		'turbine' : 'Turbine',
	} 

class Lang(object):
	def __call__(self, name : str,*args: Any, **kwds: Any) -> Any:
		try: 
			return _trans_dict[name]
		except:
			print(f'untranslated string: {name}')
			return f'00_{name}'
	def __getattribute__(self, name: str) -> Any:
		try: 
			#print(f'outdated access of translation string: {name}')
			return _trans_dict[name]
		except:
			print(f'untranslated string: {name}')
			return f'00_{name}'
lang = Lang()
