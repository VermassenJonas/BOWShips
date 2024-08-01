from PySide6.QtWidgets import QApplication, QWidget

def main():
	app = QApplication([])
	window = QWidget()
	window.show()
	app.exec()

if __name__ == '__main__':
	main()