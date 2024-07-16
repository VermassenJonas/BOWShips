import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import Property

from Data_Ship import ship
from BuildingBlocks import *

class DisplacementEntry(QWidget):


	def __init__(self, parent=None):
		super(DisplacementEntry, self).__init__(parent)

		self.counter = 0
		# define layout
		layout = QGridLayout()
		self.setLayout(layout) 

		self.blockCoeffField = ConfSpinBox()
		self.blockCoeffField.setDecimals(5)
		self.blockCoeffField.setSingleStep(0.003)

		self.displacementField = ConfSpinBox()
		self.displacementField.setDecimals(0)
		self.displacementField.setSingleStep(100)

		layout.addWidget(self.blockCoeffField,0,0)
		layout.addWidget(self.displacementField, 0,1)

		self.displacementField.textChanged.connect(self.updateDisp)
		self.blockCoeffField.textChanged.connect(self.updateBlock)

		ship.displacement.subscribe(self.refreshDisp)
		ship.blockCoeff.subscribe(self.refreshBlock)

		self.show()

	def updateDisp(self):
		ship.displacement.value = self.displacementField.value()
	def updateBlock(self):
		ship.blockCoeff.value = self.blockCoeffField.value()

	def refreshDisp(self, e):
		self.displacementField.setValue(ship.displacement.value)
	def refreshBlock(self, e):
		self.counter += 1
		print(f'counter: {self.counter}')
		self.blockCoeffField.setValue(ship.blockCoeff.value)

if __name__ == "__main__":
	app = QApplication()
	screen = DisplacementEntry()
	sys.exit(app.exec())