import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Slot

import Data_Ship as ship

class HullTab(QWidget):

	def __init__(self, parent=None):
		super(HullTab, self).__init__(parent)
 
		# Create widgets		

		
		self.show()


if __name__ == "__main__":
	app = QApplication()
	screen = HullTab()
	screen.show()
	sys.exit(app.exec())