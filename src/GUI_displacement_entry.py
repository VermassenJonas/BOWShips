import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Property

from Data_Ship import ship
from BuildingBlocks import *

class DisplacementEntry(QWidget):


	def __init__(self, parent=None):
		super(DisplacementEntry, self).__init__(parent)

		self.show()




if __name__ == "__main__":
	app = QApplication()
	screen = DisplacementEntry()
	sys.exit(app.exec())