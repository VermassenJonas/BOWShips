from decimal import Decimal

from logic import constants

def init_num(value):
	return Decimal(str(value))


def ftToM(newValue : Decimal, *args, **kwds) -> Decimal:
	return rem_zeros(newValue * constants.ftTometer)
def mToFt(newValue : Decimal, *args, **kwds) -> Decimal:
	return rem_zeros(newValue / constants.ftTometer)

def rem_zeros( d : Decimal) -> Decimal:
	return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

def validateDecimal(newValue, *args, **kwds):
	try:
		result = Decimal(newValue)
		return rem_zeros(result) 
	except:
		return None	

def readEnum(enum, newValue : str, *args, **kwds):
	if newValue:
		return enum[newValue.upper()]
	else:
		return None 

def roundOutBound(val: Decimal, *args, **kwds):
	if val:
		return rem_zeros(val.quantize(Decimal(constants.roundTo)))
	else:
		return Decimal(0)
def verifyUpdate(newvalue, *args, **kwds):
	print(f'update: {newvalue}')
	return newvalue