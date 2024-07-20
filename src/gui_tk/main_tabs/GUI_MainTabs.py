from tkinter import Widget, BOTH
from GUI.Component import Component
from GUI_Hull_Tab import HullTab
from GUI_Engine_Tab import EngineTab
import src.logic.constants as constants
from BOWS import App
from GUI.WidgetManager import wm

class MainTabs(Component):
	def __init__(self, parent : Widget, app : App) -> None:
		super().__init__(parent, app)
		self.base =  wm.create_notebook(self.parent)
		self.hullTab = HullTab(self.base, self.app)
		self.hullTab.base.grid()
		self.engineTab = EngineTab(self.base, self.app)
		self.engineTab.base.grid()
		self.base.add(self.hullTab.base, 	text=f'{app.lang.hull}') 
		self.base.add(self.engineTab.base,	text=f'{app.lang.engine}')
		
		#mainTabs.add(FreeboardTab, 	text =strings.freeboard) 

		

if __name__ == "__main__":	
	from BOWS import App
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen = MainTabs(root, app)
	screen.base.pack()
	root.mainloop()