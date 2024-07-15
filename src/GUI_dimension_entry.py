import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Property

from Data_Ship import ship
from BuildingBlocks import *

class HullTab(QWidget):

	lengthField = None
	def updateLPP(self, e):
		self.LengthPPField.setValue(ship.length/2)

	def updateShip(self):
		ship.length = self.lengthField.value()

	def __init__(self, parent=None):
		super(HullTab, self).__init__(parent)

		# define layout
		layout = QGridLayout()
		self.setLayout(layout) 
		# Create widgets		

		self.lengthLabel = QLabel(text="Ship length (m):")
		self.beamLabel = QLabel(text="Ship beam (m):")
		self.draftLabel = QLabel(text="Ship draft (m):")

		self.lengthField = ConfSpinBox()
		self.lengthField.setPrefix('waterline: ')
		self.lengthField.setSuffix(' m')
		self.lengthField.setValue(ship.length)

		self.beamField = ConfSpinBox()
		self.beamField.setValue(ship.beam)

		self.draftField = ConfSpinBox()
		self.draftField.setValue(ship.draft)
		

		self.LengthPPField = ConfSpinBox()
		self.LengthPPField.setValue(ship.length/2)
		self.LengthPPField.setDisabled(True)

		layout.addWidget(self.lengthLabel	,1,0)
		layout.addWidget(self.beamLabel		,1,1)
		layout.addWidget(self.draftLabel	,1,2)
		layout.addWidget(self.lengthField	,2,0)
		layout.addWidget(self.beamField		,2,1)
		layout.addWidget(self.draftField	,2,2)
		layout.addWidget(self.LengthPPField	,3,0)

		self.lengthField.textChanged.connect(self.updateShip)

		ship.subscribe(self.updateLPP)		
		self.show()





if __name__ == "__main__":
	app = QApplication()
	screen = HullTab()
	screen.show()
	sys.exit(app.exec())