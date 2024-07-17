import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import (Slot, QRect)

from Data_Ship import ship
from GUI_dimension_entry import DimensionEntry

class HullTab(QWidget):

	def __init__(self, parent=None):
		super(HullTab, self).__init__(parent)
 
		layout = QGridLayout()
		self.setLayout(layout)
		# Create widgets		
		dimensions = DimensionEntry()
		layout.addWidget(dimensions)
		
		self.show()


if __name__ == "__main__":
	app = QApplication()
	screen = HullTab()	
	screen.setGeometry(QRect(100, 100, 800, 600))
	sys.exit(app.exec())