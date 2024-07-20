from typing import Generic, TypeVar, List

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
	def addCallback(self, *callbacks):
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
	def _set(self,new ):
		val = self._value
		for proc in self._processors:
			val = proc(new, val)
		if val:
			self._value = val
	def __call__(self, value: T = None, val_fn = None) -> T:
		if val_fn:
			value = val_fn()
		if not value:
			return self._get()
		else:
			self._set(value)

class AliasProperty(Property[T]):
	def __init__(self, property : Property) -> None:
		self._property = property
		property.addCallback(self._notify)
		super().__init__(None)
	def _get(self) -> T:
		self._value = self.property()
		return super()._get()
	def _set(self, new):
		super()._set(new)
		self._property(self._value)

class CalculatedProperty(Property[T]):
	def __init__(self, calcFun, *properties : List[Property]) -> None:
		super().__init__(None)
		self._properties = properties
		self._dirtyflags = {}
		self._calcFun = calcFun
		self._value = calcFun()
		self._dirty = False
		for property in self._properties:
			property.addCallback(self._notify)
	def _notify(self):
		self._dirty = True
		return super()._notify()
	def _get(self):
		if self._dirty:
			self._value = self._calcFun()
			self._dirty = False
		return super()._get()
	def __call__(self) -> T:
		return self._get()