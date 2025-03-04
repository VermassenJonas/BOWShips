from tkinter import BOTH, Misc, Widget
import tkinter.messagebox as messagebox
from BOWS import App
import translations.en as en_lang
from gui_tk.utils.Component import Component
from logic.Ship import Ship
from gui_tk.utils.WidgetManager import wm
class ScreenRoot(Component):
	ship : Ship
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)
		self.app = app
		self.readCBs = []
		self.calcCBs = []
		self._updateCBs = []
		self.ship = Ship()
		self.lang = en_lang.lang
		#self.process()

	def draw(self):	
		from gui_tk.MainContent import MainContent	
		self.base = wm.create_frame(self.parent)
		mainContent = MainContent(self.base,self.app)
		self.parent.title(self.lang('main_title')) # type: ignore
		self.base.pack(expand=True, fill=BOTH)
		mainContent.base.pack(expand=True, fill=BOTH)
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
		self.parent.after(5000, self.process)
	

	

def main(app : App ) -> None:
	root = wm.create_root()
	def on_closing():
		if messagebox.askokcancel("Quit", "Do you want to quit?"):
			root.destroy()

	root.protocol("WM_DELETE_WINDOW", on_closing)
	root.geometry("800x600")
	screen = ScreenRoot(root, app)
	screen.draw()
	root.mainloop()


if __name__ == "__main__":
	app = App()
	main(app)