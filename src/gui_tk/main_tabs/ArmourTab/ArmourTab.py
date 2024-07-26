from tkinter import Misc, Widget
from gui_tk.main_tabs.ArmourTab.ArmourBelt import ArmourBelt
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class ArmourTab(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)		
		generalData = ArmourBelt(self.base, self.app)
		generalData.base.grid()
		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =ArmourTab(root, app)
	screen.base.pack()
	root.mainloop()