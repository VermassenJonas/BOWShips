from typing import Any



class Lang:
	_trans_dict = {
		'main_title' 			: "BOWShips: Build your Own Warships",
		'hull' 					: "Hull",
		'freeboard' 			: "Freeboard",
		'ship_info' 			: "Ship Info",
		'report' 				: "Report",
		'ship_overview' 		: 'Ship Overview',
		'engine' 				: 'Engine',
		'engines' 				: 'Engines',
		'ship' 					: 'Ship',
		'name' 					: 'Name',
		'country' 				: 'Country',
		'type' 					: 'Type',
		'year' 					: 'Year',
		'dimensions' 			: 'Dimensions',
		'laid_down' 			: 'Laid Down',
		'engine_built' 			: 'Engine Built',
		'length' 				: 'length',
		'beam' 					: 'beam',
		'draft' 				: 'draft',
		'meter' 				: 'meter',
		'feet' 					: 'feet',
		'displacement' 			: 'Displacement',
		'block_coefficient' 	: 'Block Coefficient',
		'speed_and_power' 		: 'Speed & Power',
		'fuel' 					: 'Fuel',
		'maxSpeed' 				: 'Max Speed',
		'cruise_speed' 			: 'Cruise Speed',
		'shafts' 				: 'Shafts',
		'engine_type' 			: 'Engine Type',
		'coal' 					: 'Coal',
		'mixed' 				: 'Mixed',
		'oil'					:'Oil',
		'simple' 				: 'Simple',
		'complex' 				: 'Complex',
		'turbine' 				: 'Turbine',
		'power' 				: 'Power',
		'engine_weight' 		: 'Engine Weight',
		'engine_efficiency' 	: 'Engine Efficiency',
		'weight_of_main_engine' : 'Weight of Engine',
		'armour' 				: 'Armour',
		'magazines_belt' 		: 'Belt over Magazines',
		'machinery_belt' 		: 'Belt over Machinery',
		'torpedo_belt'	 		: 'Torpedo Bulkheads',
		'extended_belt'	 		: 'Armour over ends',
		'upper_belt'	 		: 'Upper Belt',
		'main_belt'	 			: 'Main Belt',
		'thickness_mm'	 		: 'Thickness (mm)',
		'thickness_in'	 		: 'Thickness (inch)',
		'length_m'	 			: 'Length (m)',
		'length_ft'	 			: 'Length (ft)',
		'height_m'	 			: 'Height (m)',
		'height_ft'	 			: 'Height (ft)',
		'belt_and_bulkheads'	: 'Belts & Bulkheads',
		'weight_ton'			: 'Weight (ton)',

	} 
	def __call__(self, name : str,*args: Any, **kwds: Any) -> Any:
		try: 
			return self._trans_dict[name]
		except:
			print(f'untranslated string: {name}')
			return f'00_{name}'
	
lang = Lang()
