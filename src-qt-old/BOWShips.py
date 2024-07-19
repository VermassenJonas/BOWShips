import sys

from PySide6.QtWidgets import *
from GUI_MainContent import MainContent
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

class MainScreen(QMainWindow):
	def __init__(self):
		super(MainScreen, self).__init__()
		self.setCentralWidget = MainContent(self)
		self.setWindowTitle("BOWShips")
		self.setGeometry(100,100,800,800)

if __name__ == "__main__":
	ui_file = QFile("./mainform.ui")
	ui_file.open(QFile.ReadOnly)

	loader = QUiLoader()
	window = loader.load(ui_file)
	window.show()