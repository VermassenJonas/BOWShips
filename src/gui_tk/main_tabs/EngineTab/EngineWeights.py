from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class EngineWeights(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)

		self.title = wm.create_title_label(self.base, app.lang('engine_weight'))
		self.title.grid()

		self.engineEfficiencyLabel	= wm.create_label(self.base, app.lang('engine_efficiency:') )
		self.engineWeightLabel	= wm.create_label(self.base, app.lang('weight_of_main_engine:') )

		self.engineEfficiencyEntry = wm.create_readOnly_entry(self.base)		
		self.engineWeightEntry = wm.create_readOnly_entry(self.base)

		self.engineEfficiencyLabel.grid(column=0, row=1)
		self.engineWeightLabel.grid(column=0, row=2)
		
		self.engineEfficiencyEntry.grid(column=1, row=1)
		self.engineWeightEntry.grid(column=1, row=2)

		self.doRigging()

	def doRigging(self):
		
		wm.bindEntryTwoWay(self.engineEfficiencyEntry, self.app.ship.engineEfficiency)
		wm.bindEntryTwoWay(self.engineWeightEntry, self.app.ship.engineWeight)
		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =EngineWeights(root, app)
	screen.base.pack()
	root.mainloop()