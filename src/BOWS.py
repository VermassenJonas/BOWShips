
from decimal import getcontext
from logic import constants
import logic.Enums as enums
from logic.Ship import Ship
import translations.en as en_lang

class App:
	def __init__(self) -> None:	
		self.enums = enums	
		self.ship = Ship()
		self.lang = en_lang.lang


if __name__ == "__main__":
	
	getcontext().prec = constants.precision
	app = App()
	from gui_tk.tk_main import main
	main(app)
