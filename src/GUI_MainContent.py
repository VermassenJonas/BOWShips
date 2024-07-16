import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import (Slot, QRect)

from Data_Ship import ship
from GUI_HullTab import HullTab

class MainContent(QWidget):

	def __init__(self, parent=None):
		super(MainContent, self).__init__(parent)
		layout = QHBoxLayout()
		self.setLayout(layout)


		# Create widgets		
		tabHolder = QTabWidget()
		tabHolder.addTab(HullTab(), 'hull')

		layout.addChildWidget(tabHolder)


		self.show()


if __name__ == "__main__":
	app = QApplication()
	screen = MainContent()	
	screen.setGeometry(QRect(0, 0, 800, 600))
	sys.exit(app.exec())