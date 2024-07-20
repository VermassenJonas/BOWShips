from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.main_tabs.EngineTab.SpeedNPower import SpeedPower
from gui_tk.main_tabs.EngineTab.Engines import Engines
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class EngineTab(Component):
	def __init__(self, parent : Misc, app : App)  -> None:
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