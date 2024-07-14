# File: main.py
import sys

from PySide6.QtWidgets import *
from GUI.MainContent import MainContent

class MainScreen(QMainWindow):
	def __init__(self):
		super(MainScreen, self).__init__()
		self.setCentralWidget = MainContent(self)
		self.setWindowTitle("BOWShips")
		self.setGeometry(100,100,800,800)

if __name__ == "__main__":
	app = QApplication()
	mainScreen = MainScreen()
	mainScreen.show()
	sys.exit(app.exec())