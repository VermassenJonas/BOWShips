

from logic.Property import Property

from typing import  Generic, TypeVar, List, Self

T = TypeVar('T')
class CalculatedProperty(Property[T]):
	def __init__(self, calcFun, *properties : List[Property]) -> None:
		super().__init__(None)
		self._properties = properties
		self._dirtyflags = {}
		self._calcFun = calcFun
		self._value = calcFun(*self._properties)
		self._dirty = False
		for property in self.properties:
			property.addCallback(self._notify)
	def _notify(self):
		self._dirty = True
		return super()._notify()
	def _get(self):
		if self._dirty:
			self._value = self.calcVal(self._properties)
			self._dirty = False
		return super()._get()
	def __call__(self) -> T:
		return self._get()