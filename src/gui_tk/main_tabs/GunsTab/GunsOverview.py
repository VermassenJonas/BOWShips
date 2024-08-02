from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class GunsOverview(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)

		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	
		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =GunsOverview(root, app)
	screen.base.pack()
	root.mainloop()