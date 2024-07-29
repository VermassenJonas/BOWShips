from decimal import Decimal
from data import DataReader
from logic.Enums import Engine, Fuel 
from logic.Interpolator import Interpolator
from logic.Ship import Ship
class EngineEfficiency:
	def __init__(self, ship : Ship) -> None:
		from logic.Ship import Ship 
		self._ship : Ship = ship
	def calcEngineEfficiency(self) -> Decimal | None:
		# part 1: read CSV values
		## 1.1: determine what to read
		ship = self._ship
		csv_file = 'engineWeight'
		columns = self._determineColumns()	
		[colCoal, colOil] =  columns
		dataCoal = DataReader.readSingleDataColumn(colCoal,  index=ship.engineBuilt(), csv_file=csv_file)
		coalVal = Interpolator.linear_interpolation(ship.engineBuilt(), *dataCoal)
		dataOil = DataReader.readSingleDataColumn(colOil, index=ship.engineBuilt(), csv_file=csv_file)
		oilVal = Interpolator.linear_interpolation(ship.engineBuilt(), *dataOil)
		return Interpolator.linear_interpolation(ship.engine.coalPercent(), (100, coalVal), (0, oilVal) )



			
	def _determineColumns(self):
		ship = self._ship
		_engine = ship.engine.engineType()
		columns: list[int] = []
		match  _engine:
			case Engine.SIMPLE:
				columns.extend([1,4])
			case Engine.COMPLEX:
				columns.extend([2,5])
			case Engine.TURBINE:
				columns.extend([3,6])
		return columns