from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class DeckArmour(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.titleLabel = wm.create_title_label(self.base, app.lang('deck_armour'))
		self.titleLabel.grid(row=0, columnspan=5)

		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	
		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen = DeckArmour(root, app)
	screen.base.pack()
	root.mainloop()