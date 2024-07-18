import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from GUI_GeneralData import GeneralData
from GUI_DimensionData import DimensionData
from GUI_DisplacementData import DisplacementData
from BOWS import App
class HullTab(Component):
	def __init__(self, parent : tk.Widget, app : App) -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent)
		generalData = GeneralData(self.base, self.app)
		generalData.base.grid()
		dimensionData = DimensionData(self.base, self.app)
		dimensionData.base.grid()
		displacementData = DisplacementData(self.base, self.app)
		displacementData.base.grid()

		

if __name__ == "__main__":	
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =HullTab(root, app)
	screen.base.grid()
	root.mainloop()