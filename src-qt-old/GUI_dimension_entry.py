import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Property

from Data_Ship import ship
from BuildingBlocks import *

class DimensionEntry(QWidget):


	def __init__(self, parent=None):
		super(DimensionEntry, self).__init__(parent)

		# define layout
		layout = QGridLayout()
		self.setLayout(layout) 
		# Create widgets		

		self.lengthLabel = QLabel(text="Ship length (waterline):")
		self.beamLabel = QLabel(text="Ship beam:")
		self.draftLabel = QLabel(text="Ship draft (normal):")

		self.lengthField = ConfSpinBox()
		self.lengthField.setSuffix(' m')
		self.lengthField.setValue(ship.value)

		self.beamField = ConfSpinBox()
		#self.beamField.setPrefix('hull: ')
		self.beamField.setSuffix(' m')
		self.beamField.setValue(ship.beam)

		self.draftField = ConfSpinBox()
		#self.draftField.setPrefix('normal: ')
		self.draftField.setSuffix(' m')
		self.draftField.setValue(ship.draft)


		

		self.LengthOAField = ConfSpinBox()
		self.LengthOAField.setValue(ship.value+2.5)
		self.LengthOAField.setDisabled(True)

		layout.addWidget(self.lengthLabel	,1,0)
		layout.addWidget(self.beamLabel		,1,1)
		layout.addWidget(self.draftLabel	,1,2)
		layout.addWidget(self.lengthField	,2,0)
		layout.addWidget(self.beamField		,2,1)
		layout.addWidget(self.draftField	,2,2)

		layout.addWidget(self.LengthOAField	,4,0)

		self.lengthField.textChanged.connect(self.updateShip)
		self.beamField.textChanged.connect(self.updateShip)
		self.draftField.textChanged.connect(self.updateShip)

		ship.subscribe(self.updateLOA)		
		self.show()

	def updateLOA(self, e):
		self.LengthOAField.setValue(ship.value*ship.beam*ship.draft)

	def updateShip(self):
		ship.value = self.lengthField.value()
		ship.beam = self.beamField.value()




if __name__ == "__main__":
	app = QApplication()
	screen = DimensionEntry()
	sys.exit(app.exec())