from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class DisplacementData(Component):
	def __init__(self, parent : Misc, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		
		self.titleLabel = wm.create_title_label(self.base, text=f'{app.lang.displacement}')

		self.blockLabel 	= wm.create_label(self.base, text=f'{app.lang.block_coefficient}:')
		self.dispLabel 		= wm.create_label(self.base, text=f'{app.lang.displacement}:')
		self.blockEntry 	= wm.create_entry(self.base)
		self.dispEntry 		= wm.create_entry(self.base)

		self.titleLabel.grid(column=0, row=0, columnspan=2)

		self.blockLabel.grid	(column=0, row=1)
		self.dispLabel.grid		(column=1, row=1)
		self.blockEntry.grid	(column=0, row=2)
		self.dispEntry.grid		(column=1, row=2)

		self.doRigging()
	def doRigging(self):
		self.bindEntryCallback(self.dispEntry,			self.app.ship.displacement)
		self.bindEntryCallback(self.blockEntry,		 	self.app.ship.blockCoeff)

		self.bindEntryRead(self.dispEntry, 			self.app.ship.displacement)
		self.bindEntryRead(self.blockEntry, 		self.app.ship.blockCoeff)

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen =DisplacementData(root, app)
	screen.base.pack()
	root.mainloop()