from typing import Any, Generic, TypeVar

T = TypeVar('T')
class Property(Generic[T]):
	def __init__(self, value: T) -> None:
		super().__init__()
		self.value = value
		self._callbacks = []
		self._processors = []
	def addCallback(self, callback):
		self._callbacks.append(callback)
		return self
	def addProcessor(self, processor=None, processors=None):
		if processor:
			self._processors.append(processor)
		if processors:
			self._processors.extend(processors)
		return self
	def _notify(self):
		for callback in self._callbacks:
			callback(self.value)
	def __call__(self, value=None, val_fn=None,*args: Any, **kwds: Any) -> T:
		if val_fn:
			value = val_fn()
		for processor in self._processors:
			var = processor(value)
			if var:
				value = var
			else:
				value = None
				break
		if value:
			self.value = value
			self._notify()
		return self.value
class AliasProperty(Property[T]):
	def __init__(self, property : Property[T]) -> None:
		super().__init__(None)
		self._backProcessors = []
		self.property = property
		self.property.addCallback(self._notify)
	def _notify(self, *args):
		for callback in self._callbacks:
			callback(self())
	def addBackProcessor(self, processor=None, processors=None):
		if processor:
			self._backProcessors.append(processor)
		if processors:
			self._backProcessors.extend(processors)
		return self
	def calcValue(self) -> T:
		value = self.property()
		for processor in self._backProcessors:
			value = processor(value)
		return value
	def __call__(self,value=None, val_fn=None, *args: Any, **kwds: Any) -> T:
		if val_fn:
			value = val_fn()
		if value:
			for processor in self._processors:
				var = processor(value)
				if var:
					value = var
				else:
					value = None
					break
			if value:
				self.property(value)				
				self._notify()
		return self.calcValue()