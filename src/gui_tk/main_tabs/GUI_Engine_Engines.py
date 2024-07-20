from tkinter import W, Widget, StringVar
from GUI.Component import Component
from BOWS import App
import src.logic.constants as constants
from GUI.WidgetManager import wm
import logic.Enums as enums
from GUI_Engine_EngineType import EngineType
from GUI_Engines_FuelType import FuelType

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