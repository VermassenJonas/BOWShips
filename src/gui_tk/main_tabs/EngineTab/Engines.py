from tkinter import W, Widget, StringVar
from gui_tk.tk_main import App
from gui_tk.main_tabs.EngineTab.EngineType import EngineType
from gui_tk.main_tabs.EngineTab.FuelType import FuelType
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class Engines(Component):
	def __init__(self, parent : Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.titleLabel = wm.create_title_label(self.base, self.app.lang.engines)
		self.titleLabel.grid(column=0, row=0)
		
		self.fuelType = FuelType(self.base, self.app)
		self.fuelType.base.grid(column=0, row=1)
		self.engineType = EngineType(self.base, self.app)
		self.engineType.base.grid(column=1, row=1)
		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	
		

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen =Engines(root, app)
	screen.base.pack()
	root.mainloop()