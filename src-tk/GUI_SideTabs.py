from tkinter import Widget
from GUI.Component import Component
from BOWS import App
import constants as constants
import GUI.WidgetMaker as wm
class SideTabs(Component):
	def __init__(self, parent : Widget, app : App) -> None:
		super().__init__(parent, app)
		self.base =  wm.create_notebook(self.parent)
		shipOverviewTab = wm.create_frame(self.base) 
		reportTab = wm.create_frame(self.base) 
		self.base.add(shipOverviewTab, text=f'{app.lang.ship_info}')
		self.base.add(reportTab, text=f'{app.lang.report}')
		
		#self.base.add(shipOverviewTab, 	text =self.app.lang.ship_overview) 
		#self.base.add(reportTab, 		text =self.app.lang.report) 
		

		

if __name__ == "__main__":	
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen = SideTabs(root, app)
	screen.base.pack()
	root.mainloop()