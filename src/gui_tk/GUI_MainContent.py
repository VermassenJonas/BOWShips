from tkinter import RAISED, Widget, HORIZONTAL, BOTH

from BOWS import App
from GUI.Component import Component
from GUI_MainTabs import MainTabs
from src.gui_tk.side_tabs.GUI_SideTabs import SideTabs
from GUI.WidgetManager import wm
class MainContent(Component):
	def __init__(self, parent : Widget, app : App) -> None:
		super().__init__(parent, app)

		self.base = wm.create_paned_window(parent)
		self.base.config(orient=HORIZONTAL, sashwidth=5)
		mainTabs = MainTabs(self.base, app)
		self.base.add(mainTabs.base)

		sideTabs = SideTabs(self.base, app)
		self.base.add(sideTabs.base)
		

		

if __name__ == "__main__":	
	from BOWS import App
	root = wm.create_root()
	root.geometry("800x600")
	app = App(root, None)
	screen = MainContent(root, app)	
	screen.base.pack(expand=True, fill=BOTH)
	root.mainloop()