import tkinter as tk
import tkinter.ttk as ttk


from GUI.Component import Component
from GUI_MainTabs import MainTabs
from GUI_SideTabs import SideTabs

class MainContent(Component):
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)

		self.base = tk.PanedWindow(parent, orient=tk.HORIZONTAL, sashwidth=10)

		mainTabs = MainTabs(self.base, app)
		self.base.add(mainTabs.base)

		sideTabs = SideTabs(self.base, app)
		self.base.add(sideTabs.base)
		

		

if __name__ == "__main__":	
	from BOWS import App
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =MainContent(root, app)	
	screen.base.pack(expand=True, fill=tk.BOTH)
	root.mainloop()