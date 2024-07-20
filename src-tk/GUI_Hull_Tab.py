from tkinter import Widget
from GUI.Component import Component
from GUI_Hull_General import GeneralData
from GUI_Hull_Dimension import DimensionData
from GUI_Hull_Displacement import DisplacementData
from BOWS import App
from GUI.WidgetManager import wm
class HullTab(Component):
	def __init__(self, parent : Widget, app : App) -> None:
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