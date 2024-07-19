from tkinter import BOTH, Widget
import tkinter.messagebox as messagebox
import translations.en as en_lang
from GUI.Component import Component
from logic.Ship import Ship
import GUI.WidgetMaker as wm
import constants
class App(Component):
	ship : Ship
	def __init__(self, parent : Widget, app) -> None:
		super().__init__(parent, app)
		self.app = self
		self.readCBs = []
		self.calcCBs = []
		self._updateCBs = []
		self.ship = Ship()
		self.lang = en_lang.lang
		self.process()

	def draw(self):		
		self.base = wm.create_frame(self.parent)
		mainContent = MainContent(self.base,self)
		self.parent.title(self.lang('main_title'))
		self.base.grid()
		mainContent.base.grid()
	def subscribe_update(self, element : Widget, fn):
		self._updateCBs.append((element, fn))
	def process(self):
		for fn in self.readCBs:
			fn()
		for fn in self.calcCBs:
			fn()
		for (element, fn ) in self._updateCBs:
			if element and element.focus_get() != element:
				fn()
		print(f'subscribers: {len(self.readCBs)}, {len(self.calcCBs)}, {len(self._updateCBs)}')
		self.parent.after(constants.clockspeed, self.process)
	

	

if __name__ == "__main__":
	from GUI_MainContent import MainContent #deferred to prevent circular imports
	root = wm.create_root()
	def on_closing():
		if messagebox.askokcancel("Quit", "Do you want to quit?"):
			root.destroy()

	root.protocol("WM_DELETE_WINDOW", on_closing)
	root.geometry("800x600")
	app = App(root, None)
	app.draw()
	root.mainloop()