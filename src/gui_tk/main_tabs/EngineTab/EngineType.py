from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm
import logic.Enums as enums

class EngineType(Component):
	def __init__(self, parent : Misc, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.base.grid(column=1, row=1)
		self.engineLabel = wm.create_label(self.base, app.lang('engine_type'))
		self.engineLabel.grid()
		(self.engineVar, self.engineButtons) = wm.create_radio_set(self.base,app,  enums.Engine)
		for button in self.engineButtons:
			button.grid()	
		self.doRigging()

	def doRigging(self):
		self.engineVar.set( self.app.ship.engineType())
		self.bindVarRead(self.engineVar, self.app.ship.engineType)

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =EngineType(root, app)
	screen.base.pack()
	root.mainloop()