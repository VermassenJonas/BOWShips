import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from BOWS import App
import constants
import GUI.Customization as GuiCust

class SpeedPower(Component):
	def __init__(self, parent : tk.Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=constants.framewidth)

		titleLabel = tk.Label(self.base, text=f'{app.lang.speed_and_power}')
		GuiCust.configHeader(titleLabel)
		
		maxSpeedlabel = tk.Label(self.base, text='0maxSpeed')
		cruiseSpeedLabel = tk.Label(self.base, text='0cruise speed')
		shaftCountLabel = tk.Label(self.base, text='0shafts')
		maxSpeedEntry = tk.Entry(self.base)
		cruiseSpeedEntry = tk.Entry(self.base, state=tk.DISABLED) #TODO: Cruising's for later
		shaftCountEntry = tk.Entry(self.base)
		powReqMaxHPLabel = tk.Label(self.base, text=f'0Power(shp): 0x0000')


		titleLabel.grid			(column=0, row=0, columnspan=2)
		maxSpeedlabel.grid		(column=0, row=1)
		cruiseSpeedLabel.grid	(column=0, row=2)
		shaftCountLabel.grid	(column=0, row=3)
		maxSpeedEntry.grid		(column=1, row=1)
		cruiseSpeedEntry.grid	(column=1, row=2)
		shaftCountEntry.grid	(column=1, row=3)
		

		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =SpeedPower(root, app)
	screen.base.grid()
	root.mainloop()