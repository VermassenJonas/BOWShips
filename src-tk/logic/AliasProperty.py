from logic.Property import Property
from typing import  Generic, TypeVar, List, Self

T = TypeVar('T')

class AliasProperty(Property[T]):
	def __init__(self, property : Property) -> None:
		super().__init__(None)
		self.property = property
		property.addCallback(self._notify)
	def _get(self) -> T:
		self._value = property()
		return super()._get()
	def _set(self, new):
		self._value = super()._set(new)
		property(self._value)