import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component

from GUI_MainTabs import MainTabs
class MainContent(Component):
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)
		self.base =  tk.PanedWindow(parent, orient=tk.HORIZONTAL)
		self.base.pack(expand=True, fill=tk.BOTH)
		MainTabs(self.base, app)
		#SideTabs(self.base, app)
		

		

if __name__ == "__main__":	
	from BOWS import App
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	MainContent(root, app)
	root.mainloop()