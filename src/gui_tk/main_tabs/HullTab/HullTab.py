from tkinter import Misc, Widget
from gui_tk.main_tabs.HullTab.HullGeneral import GeneralData
from gui_tk.main_tabs.HullTab.HullDimension import DimensionData
from gui_tk.main_tabs.HullTab.HullDisplacement import DisplacementData
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm
class HullTab(Component):
	def __init__(self, parent : Misc, app : App) -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		generalData = GeneralData(self.base, self.app)
		generalData.base.grid()
		dimensionData = DimensionData(self.base, self.app)
		dimensionData.base.grid()
		displacementData = DisplacementData(self.base, self.app)
		displacementData.base.grid()

		

if __name__ == "__main__":	
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen =HullTab(root, app)
	screen.base.grid()
	root.mainloop()