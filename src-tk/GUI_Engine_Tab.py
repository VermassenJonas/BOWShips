from tkinter import Widget
from GUI.Component import Component
from BOWS import App
import constants
from GUI_Engine_SpeedPower import SpeedPower
from GUI_Engine_Engines import Engines
import GUI.WidgetMaker as wm

class EngineTab(Component):
	def __init__(self, parent : Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.speedPower = SpeedPower(self.base, self.app)
		self.engines = Engines(self.base, self.app)
		self.speedPower.base.grid()
		self.engines.base.grid()
		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	
		

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen =EngineTab(root, app)
	screen.base.pack()
	root.mainloop()