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
    def __init__(self):
        self.callbacks = []
    def subscribe(self, callback):
        self.callbacks.append(callback)
    def fire(self, **attrs):
        e = Event()
        e.source = self
        for k, v in attrs.items():
            setattr(e, k, v)
        for fn in self.callbacks:
            fn(e)