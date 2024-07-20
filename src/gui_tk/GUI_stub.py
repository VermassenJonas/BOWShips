from tkinter import Widget
from GUI.Component import Component
from BOWS import App
import src.logic.constants as constants
from GUI.WidgetManager import wm

class Stub(Component):
	def __init__(self, parent : Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)

		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	
		

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen =Stub(root, app)
	screen.base.pack()
	root.mainloop()