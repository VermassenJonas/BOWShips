import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from BOWS import App
import constants
from GUI_Engine_SpeedPower import SpeedPower

class EngineTab(Component):
	def __init__(self, parent : tk.Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=constants.framewidth)
		self.speedPower = SpeedPower(self.base, self.app)
		self.speedPower.base.grid()
		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	
		

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =EngineTab(root, app)
	screen.base.pack()
	root.mainloop()