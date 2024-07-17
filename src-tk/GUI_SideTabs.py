import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component


class SideTabs(Component):
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)
		#self.base = tk.Frame(parent, width=300, height=200, background='red')
		self.base =  ttk.Notebook(self.parent, width=450)
		shipOverviewTab = ttk.Frame(self.base) 
		reportTab = ttk.Frame(self.base) 
		
		#self.base.add(shipOverviewTab, 	text =self.app.lang.ship_overview) 
		#self.base.add(reportTab, 		text =self.app.lang.report) 
		

		

if __name__ == "__main__":	
	from BOWS import App
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen = SideTabs(root, app)
	screen.base.pack()
	root.mainloop()