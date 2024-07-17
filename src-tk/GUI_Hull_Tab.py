import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from GUI_GeneralData import GeneralData
class HullTab(Component):
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent)
		self.base.pack()
		genData = GeneralData(self.base, self.app)
		genData.base.pack()

		

if __name__ == "__main__":	
	from BOWS import App
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	HullTab(root, app)
	root.mainloop()