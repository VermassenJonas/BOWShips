import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
class HullTab(Component):
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=450)
		self.base.pack()
		ttk.Label(self.base,  text ="0placeholder").pack()
		#mainTabs.add(FreeboardTab, 	text =strings.freeboard) 
		#mainTabs.add(EngineTab, 	text =strings.engine) 

		

if __name__ == "__main__":	
	from BOWS import App
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	HullTab(root, app)
	root.mainloop()