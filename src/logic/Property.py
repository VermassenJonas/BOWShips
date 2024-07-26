from functools import partial
from tkinter import NO
from typing import Any, Callable, Generic, TypeVar

T = TypeVar('T')

class Property(Generic[T]):
	def __init__(self, value : T, processor : Callable[[Any], T] | None = None, backProcessor : Callable[[T], Any] | None= None) -> None:
		super().__init__()
		self._callbacks = []
		self._processors = []
		if processor:
			self._processors.append(processor)
		self._backProcessors = []
		if backProcessor:
			self._backProcessors.insert(0, backProcessor)
		self._value : T = value
		self._isUpdating = True
	def isUpdating(self, bool : bool | None = None):
		old = self._isUpdating
		if bool is not None:
			self._isUpdating = bool
		return old
	def addCallback(self, *callbacks : Callable[[], Any]):
		for callback in callbacks:
			self._callbacks.append(callback)
	def _notify(self):
		if self._isUpdating:
			for callback in self._callbacks:
				callback()
	def addProcessor(self, *processors : Callable [[T], T]):
		for processor in processors:
			self._processors.append(processor)
	def addBackProcessor(self, *backProcessors : Callable [[T], T]):
		for backProcessor in backProcessors:
			self._backProcessors.insert(0,backProcessor)
	@property
	def value(self):
		return self._value
	def _get(self) -> T:
		value = self._value
		for backProc in self._backProcessors:
			value = backProc(value)
		return value
	def _set(self,value) -> None:
		for proc in self._processors:
			old = self._value
			new = proc(newValue=value, oldValue=old)
			value, old = new, value
		if type(value) == type(self._value):
			self._value = value
			self._notify()
	def __call__(self, value: Any | None = None, val_fn : Callable[[], T] | None = None) -> T:
		if val_fn:
			value = val_fn()
		if value:
			self._set(value)
		return self._get()

class CalculatedProperty(Property[T]):
	def __init__(self, calcFun : Callable[[], T], *properties : Property[Any], backProcessor=None) -> None:
		super().__init__(calcFun(), backProcessor=backProcessor)
		self._calcFun = calcFun
		self._dirty = False
		for property in properties:
			property.addCallback(self._notify)
	def _notify(self):
		self._dirty = True
		return super()._notify()
	def _get(self) -> T:
		if self._dirty:
			self._value = self._calcFun()
			self._dirty = False
		return super()._get()
	def _set(self, value) -> None:
		pass


class AliasProperty(Property[T]):
	def __init__(self, property : Property, 
				downTransfo : Callable, upTransfo : Callable, dependency : CalculatedProperty | None = None,
				processor : Callable | None= None, backProcessor : Callable | None = None) -> None:
		self._property = property
		self._downTransfo = downTransfo
		self._upTransfo = upTransfo
		self._dependency = dependency
		if self._dependency is not None:
			self._downTransfo = partial(downTransfo, dependency=dependency)
			self._upTransfo = partial(upTransfo, dependency=dependency)
			self._dependency.addCallback(self._notify)
		property.addCallback(self._notify)
		super().__init__(upTransfo(property()), processor=processor, backProcessor=backProcessor)
	def _get(self) -> T:
		self._value = self._upTransfo(self._property())
		return super()._get()
	def _set(self, value):
		temp = self.isUpdating(False) # to prevent callbacks from being called early and twice
		super()._set(value)
		self.isUpdating(temp)
		self._property(self._downTransfo(self._value))

