

from logic.Ship import Ship
import translations.en as en_lang

class App:
	def __init__(self) -> None:		
		self.ship = Ship()
		self.lang = en_lang.lang


if __name__ == "__main__":
	app = App()
	from gui_tk.tk_main import main
	main(app)
