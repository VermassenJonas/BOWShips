from tkinter import Widget, StringVar
from GUI.Component import Component
from BOWS import App
import constants
import GUI.WidgetMaker as wm
from logic.Enums import Fuel

class Engines(Component):
	def __init__(self, parent : Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		(fuelVar, fuelButtons) = wm.create_radio_set(self.base, Fuel)
		for button in fuelButtons:
			button.grid()
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