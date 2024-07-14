import sys
from PySide6.QtWidgets import *

class MainContent(QWidget):

	def __init__(self, parent=None):
		super(MainContent, self).__init__(parent)
		# Create widgets

if __name__ == "__main__":
	app = QApplication()
	mainScreen = MainContent()
	mainScreen.show()
	sys.exit(app.exec())