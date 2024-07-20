from tkinter import Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class Stub(Component):
	def __init__(self, parent : Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)

		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	
		
if __name__ == '__main__':
	from gui_tk.tk_main import App	
	root = wm.create_root()
	root.geometry("800x600")
	app = App(root, None)
	screen = Stub(root, app)	
	screen.base.pack(expand=True)
	root.mainloop()