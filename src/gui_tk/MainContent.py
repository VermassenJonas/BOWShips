from tkinter import RAISED, Widget, HORIZONTAL, BOTH

from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.main_tabs.MainTabs import MainTabs
from gui_tk.side_tabs.SideTabs import SideTabs
from gui_tk.utils.WidgetManager import wm
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