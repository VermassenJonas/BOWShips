import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from GUI_Hull_Tab import HullTab
from GUI_Engine_Tab import EngineTab
import GUI.constants as GUIconst
from BOWS import App

class MainTabs(Component):
	def __init__(self, parent, app : App) -> None:
		super().__init__(parent, app)
		#self.base = tk.Frame(parent, width=300, height=200, background='blue')
		self.base =  ttk.Notebook(self.parent, width=GUIconst.framewidth, height=550)
		self.hullTab = ttk.Frame(self.base) 
		hullTab = HullTab(self.base, self.app)
		hullTab.base.pack()
		engineTab = EngineTab(self.base, self.app)
		engineTab.base.pack()
		self.base.add(hullTab.base, 	text=f'{app.lang.hull}') 
		self.base.add(engineTab.base,	text=f'{app.lang.engine}')
		
		#mainTabs.add(FreeboardTab, 	text =strings.freeboard) 

		

if __name__ == "__main__":	
	from BOWS import App
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen = MainTabs(root, app)
	screen.base.pack()
	root.mainloop()