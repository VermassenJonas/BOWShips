from decimal import Decimal

from logic import  constants
from logic.Property import Property

def init_num(value):
	return Decimal(str(value))


def ftToM(dependencies: dict[str, Property[Decimal]], value) -> Decimal:
	return rem_zeros(value * constants.ftTometer)

def mToFt(dependencies: dict[str, Property[Decimal]]) -> Decimal:
	value : Decimal = list(dependencies.values())[0]()
	return rem_zeros(value / constants.ftTometer)

def inToMm(dependencies: dict[str, Property[Decimal]], value)  -> Decimal:
	return rem_zeros(value * constants.mmPerInch)
def mmToIn(dependencies: dict[str, Property[Decimal]])  -> Decimal:
	value = list(dependencies.values())[0]()
	return rem_zeros(value / constants.mmPerInch)

def rem_zeros( d : Decimal) -> Decimal:
	return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

def validateDecimal(value, *args, **kwds):
	try:
		result = Decimal(value)
		return rem_zeros(result) 
	except:
		return Decimal(0)	

def readEnum(enum, value : str, *args, **kwds):
	if value:
		return enum[value.upper()]
	else:
		return None 

def roundOutBound(value, *args, **kwds):
	if value:
		return rem_zeros(value.quantize(constants.roundTo))
	else:
		return Decimal(0)
def verifyUpdate(value, *args, **kwds):
	print(f'update: {value}')
	return value