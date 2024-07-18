import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from BOWS import App
import GUI.Customization as GuiCust
import constants as constants

class DisplacementData(Component):
	def __init__(self, parent : tk.Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=constants.framewidth)
		
		self.titleLabel = tk.Label(self.base, text=f'{app.lang.displacement}')
		GuiCust.configHeader(self.titleLabel)

		self.blockLabel = tk.Label(self.base, text=f'{app.lang.block_coefficient}:')
		self.dispLabel = tk.Label(self.base, text=f'{app.lang.displacement}:')
		self.blockEntry = tk.Entry(self.base)
		self.dispEntry = tk.Entry(self.base)

		self.titleLabel.grid(column=0, row=0, columnspan=2)

		self.blockLabel.grid	(column=0, row=1)
		self.dispLabel.grid		(column=1, row=1)
		self.blockEntry.grid	(column=0, row=2)
		self.dispEntry.grid		(column=1, row=2)

		self.doRigging()
	def doRigging(self):
		pass #TODO: implement interactivity



if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =DisplacementData(root, app)
	screen.base.pack()
	root.mainloop()