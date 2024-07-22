from tkinter import E, EW, Misc, Widget
from gui_tk.tk_main import App 
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class GeneralData(Component):
	def __init__(self, parent : Misc, app : App) -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)

		self.titleLabel 	= wm.create_title_label(self.base, text=app.lang.ship)

		self.nameLabel 		= wm.create_label(self.base, text=f'{app.lang.name}:')
		self.countryLabel	= wm.create_label(self.base, text=f'{app.lang.country}:')
		self.typeLabel 		= wm.create_label(self.base, text=f'{app.lang.type}:')

		self.nameEntry 		= wm.create_entry(self.base)
		self.countryEntry 	= wm.create_entry(self.base)
		self.typeEntry		= wm.create_entry(self.base)

		self.yearLabel 			= wm.create_label(self.base, text=f'{app.lang("year")}:')
		self.laidDownLabel 		= wm.create_label(self.base, text=f'{app.lang("laid_down")}:')
		self.engineBuiltLabel	= wm.create_label(self.base, text=f'{app.lang("engine_built")}:')
		self.laidDownEntry 		= wm.create_entry(self.base)
		self.engineBuiltEntry 	= wm.create_entry(self.base)


		self.titleLabel.grid(column=0, row=0)
		self.nameLabel.grid(column=0, row=1)
		self.nameEntry.grid(column=1, row=1)
		self.countryLabel.grid(column=0, row=2)
		self.countryEntry.grid(column=1, row=2)
		self.typeLabel.grid(column=0, row=3)
		self.typeEntry.grid(column=1, row=3)
		self.yearLabel.grid(column=3, row=1, sticky=EW)
		self.laidDownLabel.grid(column=2, row=2)
		self.laidDownEntry.grid(column=3, row=2)
		self.engineBuiltLabel.grid(column=2, row=3)
		self.engineBuiltEntry.grid(column=3, row=3)

		self.doRigging()

	def doRigging(self):
		
		self.bindEntryCallback(self.engineBuiltEntry,		 	self.app.ship.engineBuilt)

		self.bindEntryRead(self.engineBuiltEntry, 				self.app.ship.engineBuilt)
		pass #TODO: implement interactivity	

if __name__ == "__main__":	
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =GeneralData(root, app)
	screen.base.grid()
	root.mainloop()