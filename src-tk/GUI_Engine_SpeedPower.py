import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from BOWS import App
import GUI.constants as GUIconst
import GUI.Customization as GuiCust

class SpeedPower(Component):
	def __init__(self, parent : tk.Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=GUIconst.framewidth)

		titleLabel = tk.Label(self.base, text=f'{app.lang.speed_and_power}')
		GuiCust.configHeader(titleLabel)

		titleLabel.grid()

		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	
		

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =SpeedPower(root, app)
	screen.base.pack()
	root.mainloop()