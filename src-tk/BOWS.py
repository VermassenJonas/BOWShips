from decimal import Decimal
import tkinter as tk
import tkinter.ttk as ttk
import constants
import translations.en as en_lang
from GUI.Component import Component
from logic.Ship import Ship
class App(Component):
	ship : Ship
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)
		self.app = self
		self.readCBs = []
		self.calcCBs = []
		self._updateCBs = []
		self.ship = Ship()
		self.lang = en_lang
		self.process()

	def draw(self):		
		self.base = tk.Frame(self.parent)
		mainContent = MainContent(self.base,self)
		self.parent.title(self.lang.main_title)
		self.base.pack()
		mainContent.base.pack()
	def subscribe_update(self, element : tk.Widget, fn):
		self._updateCBs.append((element, fn))
	
	def process(self):
		for fn in self.readCBs:
			fn()
		for fn in self.calcCBs:
			fn()
		for (element, fn ) in self._updateCBs:
			if element and element.focus_get() != element:
				fn()
		self.parent.after(300, self.process)
	

	

if __name__ == "__main__":
	from GUI_MainContent import MainContent #deferred to prevent circular imports
	root = tk.Tk()
	root.geometry("800x600")
	app = App(root, None)
	app.draw()
	root.mainloop()