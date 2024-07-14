import sys
from PySide6.QtWidgets import *

import Data_Ship as ship

class HullTab(QWidget):

	def __init__(self, parent=None):
		super(HullTab, self).__init__(parent)

		# define layout
		layout = QGridLayout()
		self.setLayout(layout) 
		# Create widgets		

		self.lengthLabel = QLabel(text="Ship length (m):")
		self.beamLabel = QLabel(text="Ship beam (m):")
		self.draftLabel = QLabel(text="Ship draft (m):")

		self.lengthField = QDoubleSpinBox()
		self.lengthField.setMaximum(99999999)
		self.lengthField.setValue(ship.length)

		self.beamField = QDoubleSpinBox()
		self.beamField.setValue(ship.beam)

		self.draftField = QDoubleSpinBox()
		self.draftField.setMaximum(99999999)
		self.draftField.setValue(ship.draft)
		
		layout.addWidget(self.lengthLabel,0,0)
		layout.addWidget(self.beamLabel,0,1)
		layout.addWidget(self.draftLabel,0,2)

		layout.addWidget(self.lengthField,1,0)
		layout.addWidget(self.beamField,1,1)
		layout.addWidget(self.draftField,1,2)

		self.LengthPPField = QDoubleSpinBox()
		self.LengthPPField.setMaximum(99999999)
		self.LengthPPField.setValue(ship.length)
		layout.addWidget(self.LengthPPField, 2,0)


		
		self.show()


if __name__ == "__main__":
	app = QApplication()
	screen = HullTab()
	screen.show()
	sys.exit(app.exec())