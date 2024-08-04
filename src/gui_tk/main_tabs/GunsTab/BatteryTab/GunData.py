from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class GunData(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.title = wm.create_title_label(self.base, app.lang('gun_data'))
		self.title.grid(column=0, row=0, columnspan=2)

		self.unitCombo = wm.create_ComboBox(self.base, list(self.app.enums.Unit))
		self.unitCombo.bind('<<ComboboxSelected>>', func=self.selectUnit)
		self.unitCombo.set(self.app.enums.Unit.METRIC)
		self.unitCombo.grid(column=2, row=0)

		self.unitWidgets = []
		self.calibreMmLabel = wm.create_label(self.base, text=app.lang('calibre_mm'),
									dataType=[app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.calibreInLabel = wm.create_label(self.base, text=app.lang('calibre_in'),
									dataType=[app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.calibreMmEntry = wm.create_numeric_entry(self.base, dataType=[app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.calibreInEntry = wm.create_numeric_entry(self.base, dataType=[app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.barrelLenCal = wm.create_numeric_entry(self.base)
		self.calibreMmLabel.grid(column=0, row=1)
		self.calibreInLabel.grid(column=1, row=1)
		self.calibreMmEntry.grid(column=0, row=2)
		self.calibreInEntry.grid(column=1, row=2)


		self.selectUnit()
		

	def selectUnit(self, event = None):
		unit = self.app.enums.Unit(self.unitCombo.get())
		wm.switchUnits(self.unitWidgets, unit=unit)
		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =GunData(root, app)
	screen.base.pack()
	root.mainloop()