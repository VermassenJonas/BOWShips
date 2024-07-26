from tkinter import Misc, Widget, BOTH
from gui_tk.main_tabs.ArmourTab.ArmourTab import ArmourTab
from gui_tk.utils.Component import Component
from gui_tk.main_tabs.HullTab.HullTab import HullTab
from gui_tk.main_tabs.EngineTab.EngineTab import EngineTab
import logic.constants as constants
from gui_tk.tk_main import App
from gui_tk.utils.WidgetManager import wm

class MainTabs(Component):
	def __init__(self, parent : Misc, app : App) -> None:
		super().__init__(parent, app)
		self.base =  wm.create_notebook(self.parent)
		self.hullTab = HullTab(self.base, self.app)
		self.hullTab.base.grid()
		self.armourTab = ArmourTab(self.base, self.app)
		self.armourTab.base.grid()
		self.engineTab = EngineTab(self.base, self.app)
		self.engineTab.base.grid()
		self.base.add(self.hullTab.base, 	text=app.lang('hull')) 
		self.base.add(self.armourTab.base,	text=app.lang('armour'))
		self.base.add(self.engineTab.base,	text=app.lang('engine'))
		
		#mainTabs.add(FreeboardTab, 	text =strings.freeboard) 

		

if __name__ == "__main__":	
	from gui_tk.tk_main import App
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen = MainTabs(root, app)
	screen.base.pack()
	root.mainloop()