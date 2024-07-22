from functools import partial
from typing import Any, Callable, Generic, TypeVar

T = TypeVar('T')

class Property(Generic[T]):
	_value : T
	def __init__(self, value : T) -> None:
		super().__init__()
		self._callbacks = []
		self._processors = []
		self._backProcessors = []
		self._value = value
		self._set(value)
	def addCallback(self, *callbacks : Callable[[], Any]):
		for callback in callbacks:
			self._callbacks.append(callback)
	def _notify(self):
		for callback in self._callbacks:
			callback()
	def addProcessor(self, *processors):
		for processor in processors:
			self._processors.append(processor)
	def addBackProcessor(self, *backProcessors):
		for backProcessor in backProcessors:
			self._backProcessors.append(backProcessor)
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
		if value:
			self._value = value
			self._notify()
	def __call__(self, value: T | None = None, val_fn : Callable[[], T] | None = None) -> T:
		if val_fn:
			value = val_fn()
		if value:
			self._set(value)
		return self._get()

class AliasProperty(Property[T]):
	def __init__(self, property : Property) -> None:
		self._property = property
		property.addCallback(self._notify)
		super().__init__(property())
	def _get(self) -> T:
		self._value = self._property()
		return super()._get()
	def _set(self, value):
		self._callbacks, temp  = [], self._callbacks #switcharoo to prevent callbacks from being called early/twice
		super()._set(value)
		self._callbacks = temp
		self._property(self._value)

class CalculatedProperty(Property[T]):
	def __init__(self, calcFun, *properties : Property[Any]) -> None:
		super().__init__(calcFun())
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
class DependentAliasProperty(AliasProperty[T]):
	def __init__(self, property: Property, dependency : CalculatedProperty) -> None:
		super().__init__(property)
		dependency.addCallback(self._notify)
		self._dependency = dependency
	def addProcessor(self, *processors):
		processors = [partial(proc, dependency=self._dependency) for proc in processors]
		return super().addProcessor(*processors)
	def addBackProcessor(self, *backProcessors):
		backProcessors = [partial(proc, dependency=self._dependency) for proc in backProcessors]
		return super().addBackProcessor(*backProcessors)

class DependentProperty(Property[T]):
	def __init__(self, value : T, dependency : CalculatedProperty) -> None:
		super().__init__(value)
		dependency.addCallback(self._notify)
		self._dependency = dependency
	def addProcessor(self, *processors):
		processors = [partial(proc, dependency=self._dependency()) for proc in processors]
		return super().addProcessor(*processors)
	def addBackProcessor(self, *backProcessors):
		backProcessors = [partial(proc, dependency=self._dependency()) for proc in backProcessors]
		return super().addBackProcessor(*backProcessors)
