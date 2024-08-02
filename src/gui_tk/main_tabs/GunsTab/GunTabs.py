from gui_tk.main_tabs.GunsTab.BatteryTab.BatteryTab import BatteryTab
from gui_tk.main_tabs.GunsTab.GunsOverview import GunsOverview
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class GunTabs(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_notebook(self.parent)
		# self.gunsOverview = GunsOverview(self.base, self.app)
		# self.gunsOverview.base.grid()
		# self.base.add(self.gunsOverview.base,	text=app.lang('overview'))
		self.batteries = []
		for battery in list(self.app.enums.Battery):
			batteryTab = BatteryTab(self.base, self.app)
			batteryTab.base.grid()
			self.base.add(batteryTab.base, text=app.lang(battery))


		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =GunTabs(root, app)
	screen.base.pack()
	root.mainloop()