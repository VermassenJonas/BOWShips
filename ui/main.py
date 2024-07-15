import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from HullTab import Ui_HullTab

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.hullTab = Ui_HullTab()
		self.hullTab.setupUi(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()
	app.resolveInterface
	sys.exit(app.exec())