import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from BOWS import App
import GUI.constants as GUIconst

class SideTabs(Component):
	def __init__(self, parent : tk.Widget, app : App) -> None:
		super().__init__(parent, app)
		#self.base = tk.Frame(parent, width=300, height=200, background='red')
		self.base =  ttk.Notebook(self.parent, width=GUIconst.framewidth)
		shipOverviewTab = ttk.Frame(self.base) 
		reportTab = ttk.Frame(self.base) 
		self.base.add(shipOverviewTab, text=f'{app.lang.ship_info}')
		self.base.add(reportTab, text=f'{app.lang.report}')
		
		#self.base.add(shipOverviewTab, 	text =self.app.lang.ship_overview) 
		#self.base.add(reportTab, 		text =self.app.lang.report) 
		

		

if __name__ == "__main__":	
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen = SideTabs(root, app)
	screen.base.pack()
	root.mainloop()