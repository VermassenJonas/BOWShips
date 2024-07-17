import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
class MainTabs(Component):
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)
		self.base =  ttk.Notebook(self.parent, width=450)
		self.base.pack()
		self.hullTab = ttk.Frame(self.base) 
		self.base.add(self.hullTab, 		text ='strings.hull') 
		

		

if __name__ == "__main__":	
	from BOWS import App
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	MainTabs(root, app)
	root.mainloop()