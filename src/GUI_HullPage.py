import sys
from PySide6.QtWidgets import *

class HullPage(QWidget):

	def __init__(self, parent=None):
		super(HullPage, self).__init__(parent)
		# Create widgets
		self.edit = QLineEdit("Write my name here..")
		self.button = QPushButton("Show Greetings")
		# Create layout and add widgets
		layout = QVBoxLayout(self)
		layout.addWidget(self.edit)
		layout.addWidget(self.button)
		# Add button signal to greetings slot
		self.button.clicked.connect(self.greetings)
		self.edit.textEdited.connect(self.greetings)
		self.setGeometry(0,0,500,500)
	# Greets the user
	def greetings(self):
		print(f"Hello {self.edit.text()}")

if __name__ == "__main__":
	app = QApplication()
	mainScreen = HullPage()
	mainScreen.show()
	sys.exit(app.exec())