import sys
from PySide6.QtWidgets import *

import Data_Ship as ship
import Logic_speedCalc as SpeedCalc

class SpeedDemo(QWidget):

	def __init__(self, parent=None):
		super(SpeedDemo, self).__init__(parent)
		layout = QVBoxLayout(self)
		# Create widgets
		self.setWindowTitle('BOWShips pre-alpha demo')
		self.lengthLabel = QLabel(text="Ship Length (m):")
		self.lengthField = QSpinBox()
		self.lengthField.setMaximum(1000)
		self.lengthField.setValue(ship.length)
		layout.addWidget(self.lengthLabel)
		layout.addWidget(self.lengthField)

		self.beamLabel = QLabel(text="Ship Beam (m):")
		self.beamField = QSpinBox()
		self.beamField.setValue(ship.beam)
		layout.addWidget(self.beamLabel)
		layout.addWidget(self.beamField)

		self.draftLabel = QLabel(text="Ship draft (m):")
		self.draftField = QSpinBox()
		self.draftField.setValue(ship.draft)
		layout.addWidget(self.draftLabel)
		layout.addWidget(self.draftField)

		self.displacementLabel = QLabel(text="Ship displacement (t):")
		self.displacementField = QSpinBox()
		self.displacementField.setMaximum(100000)
		self.displacementField.setValue(ship.displacement)
		layout.addWidget(self.displacementLabel)
		layout.addWidget(self.displacementField)

		self.speedLabel = QLabel(text="Ship speed (knt):")
		self.speedField = QSpinBox()
		self.speedField.setValue(ship.speed)
		layout.addWidget(self.speedLabel)
		layout.addWidget(self.speedField)

		self.shaftLabel = QLabel(text="nr of shafts")
		self.shaftField = QSpinBox()
		self.shaftField.setValue(ship.shaftCount)
		layout.addWidget(self.shaftLabel)
		layout.addWidget(self.shaftField)

		self.calcButton = QPushButton("Calculate Power (Bob1-0's code)")
		self.kwLabel = QLabel()
		self.hpLabel = QLabel()

		# Create layout and add widgets
		layout.addWidget(self.calcButton)
		layout.addWidget(self.kwLabel)
		layout.addWidget(self.hpLabel)
		# Add button signal to greetings slot
		self.calcButton.clicked.connect(self.calcSpeed)
		self.calcSpeed()
	# Greets the user
	def calcSpeed(self):
		ship.beam = self.beamField.value()
		ship.length = self.lengthField.value()
		ship.displacement = self.displacementField.value()
		ship.draft = self.draftField.value()
		ship.speed = self.speedField.value()
		ship.shaftCount = self.shaftField.value()
		kWpower = SpeedCalc.calcKWforSpeed()
		hpPower = round(1.341022 * kWpower)
		self.kwLabel.setText(f"Power required (kW): {kWpower}")
		self.hpLabel.setText(f"Power required (shp): {hpPower}")

if __name__ == "__main__":
	app = QApplication()
	mainScreen = SpeedDemo()
	mainScreen.show()
	sys.exit(app.exec())