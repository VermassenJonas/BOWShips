from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget

class ConfSpinBox(QDoubleSpinBox):
	def __init__(self, parent: QWidget = None) -> None:
		super().__init__(parent)
		self.setMaximum(9999999)
		self.setDecimals(3)

class Event(object):
	pass

class Observable(object):
	def __init__(self, value=None):
		self.callbacks = []
		self._value = value 
	
	def subscribe(self, callback):
		self.callbacks.append(callback)
	def unsubscribe(self, callback):
		self.callbacks.remove(callback)
	def fire(self, **attrs):
		e = Event()
		e.source = self
		for k, v in attrs.items():
			setattr(e, k, v)
		for fn in self.callbacks:
			fn(e)
	#getters & setters
	@property
	def value(self):
		return self._value
	@value.setter
	def value(self, newVal):
		self._value = newVal
		self.fire()