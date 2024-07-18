import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from GUI_Hull_Tab import HullTab
import GUI.constants as GUIconst

class MainTabs(Component):
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)
		#self.base = tk.Frame(parent, width=300, height=200, background='blue')
		self.base =  ttk.Notebook(self.parent, width=GUIconst.framewidth)
		self.hullTab = ttk.Frame(self.base) 
		hullTab = HullTab(self.base, self.app)
		hullTab.base.pack()
		self.base.add(hullTab.base, 	text =self.app.lang.hull) 
		
		#mainTabs.add(FreeboardTab, 	text =strings.freeboard) 
		#mainTabs.add(EngineTab, 	text =strings.engine) 

		

if __name__ == "__main__":	
	from BOWS import App
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen = MainTabs(root, app)
	screen.base.pack()
	root.mainloop()