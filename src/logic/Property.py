from collections.abc import Callable
from typing import Any, Generic, TypeVar

T = TypeVar('T')
U = TypeVar('U')


class Property(Generic[T]):
	_id = 0

	def __init__(self, value : T, name : str | None = None,
				processor : Callable[[Any], T] | None = None,
				outProcessor : Callable[[T], Any]| None = None) -> None:
		super().__init__()
		self._value = value
		if not name:
			name = str(self._id)
			self._id += 1 
		self._name = name
		self.callbacks : list[Callable[[T],Any]] = []
		self.processor = processor
		self.outProcessor = outProcessor
		self.isUpdating = True
	@property
	def value(self) -> T:
		return self._value
	@property
	def name(self) -> str:
		return self._name
	def addCallback(self, *callbacks : Callable[[T], Any]) -> None:
		for callback in callbacks:
			self.callbacks.append(callback)
	def get(self) -> Any :
		if self.outProcessor:
			return self.outProcessor(self.value)
		else:
			return self.value
	def _notify(self) -> None:
		if self.isUpdating:
			for callback in self.callbacks:
				callback(self())
	def set(self, value : Any) -> None:
		if self.processor:
			value = self.processor(value)
		if type(value) == type(self.value):
			self._value = value
	def __call__(self, value: Any = None, val_fn :Callable[[], Any] | None = None) -> Any:
		if val_fn:
			value = val_fn()
		if value:
			self.set(value)
		return self.get()



class PassDown(Generic[U, T]):
	def __init__(self, property : Property[T], downTransfo: Callable[[U, dict[str, Property[Any]]], T]) -> None:
		self.property = property
		self.downTransfo = downTransfo


class CalculatedProperty(Property[T]):
	def __init__(self, value: T, 
			dependencies: list[Property[Any]],
			calcFun : Callable[[dict[str, Property[Any]]], T],
			passDown : PassDown [Any, T]| None = None,
			name: str | None = None,
			processor: Callable[[Any], T] | None = None,
			outProcessor: Callable[[T], Any] | None = None) -> None:
		self._dependencies : dict[str, Property[Any]] = {}
		for dependency in dependencies:
			self._dependencies[dependency.name] = dependency
		for property in dependencies:
			property.addCallback(self.calculate)
		self._calcFun = calcFun
		self.passDown = passDown
		self._isDirty = True
		super().__init__(value, name, processor, outProcessor)
	def calculate(self, value : T):
		self._value = self._calcFun(self._dependencies)
	def set(self, value : Any):
		if self.passDown:
			if self.processor:
				value = self.processor(value)
			self.passDown.property(self.passDown.downTransfo(value, self._dependencies))
		else:
			raise ValueError("can't set CalculatedProperty without Passdown")

