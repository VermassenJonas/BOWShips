from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget

class ConfSpinBox(QDoubleSpinBox):
	def __init__(self, parent: QWidget = None) -> None:
		super().__init__(parent)
		self.setMaximum(9999999)
		self.setDecimals(3)

