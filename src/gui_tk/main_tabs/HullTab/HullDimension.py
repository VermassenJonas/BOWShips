from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class DimensionData(Component):
	app : App

#region init
	def __init__(self, parent : Misc, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		
		self.titleLabel = wm.create_title_label(self.base, text=app.lang('dimensions'))

		self.lengthLabel		= wm.create_label(self.base, text=app.lang('length'))
		self.beamLabel 			= wm.create_label(self.base, text=app.lang('beam'))
		self.draftLabel 		= wm.create_label(self.base, text=app.lang('draft'))
		self.unitWidgets = []

		self.meterLabel 		= wm.create_label(self.base, dataType=[app.enums.Unit.METRIC], widgetList=self.unitWidgets, text=app.lang('meter'))
		self.lengthMeterEntry 	= wm.create_entry(self.base, dataType=[app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.beamMeterEntry 	= wm.create_entry(self.base, dataType=[app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.draftMeterEntry 	= wm.create_entry(self.base, dataType=[app.enums.Unit.METRIC], widgetList=self.unitWidgets)

		self.feetLabel 			= wm.create_label(self.base, dataType=[app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets, text=app.lang('feet'))
		self.lengthFeetEntry 	= wm.create_entry(self.base, dataType=[app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.beamFeetEntry 		= wm.create_entry(self.base, dataType=[app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.draftFeetEntry 	= wm.create_entry(self.base, dataType=[app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		
		self.titleLabel.grid		(column=0, row=0, columnspan=2)
		self.lengthLabel.grid		(column=1, row=1)
		self.beamLabel.grid			(column=2, row=1)
		self.draftLabel.grid		(column=3, row=1)

		self.meterLabel.grid		(column=0, row=2)
		self.lengthMeterEntry.grid	(column=1, row=2)
		self.beamMeterEntry.grid	(column=2, row=2)
		self.draftMeterEntry.grid	(column=3, row=2)

		self.feetLabel.grid			(column=0, row=2)
		self.lengthFeetEntry.grid	(column=1, row=2)
		self.beamFeetEntry.grid		(column=2, row=2)
		self.draftFeetEntry.grid	(column=3, row=2)

		self.unitCombo = wm.create_ComboBox(self.base, list(self.app.enums.Unit))
		
		self.unitCombo.grid(row=1, column=0)

		self.doRigging()
#endregion
#region rigging
	def doRigging(self):
		wm.bindEntryTwoWay(self.lengthMeterEntry, 	self.app.ship.hull.length)
		wm.bindEntryTwoWay(self.lengthFeetEntry, 	self.app.ship.hull.lengthft)
		wm.bindEntryTwoWay(self.beamMeterEntry, 	self.app.ship.hull.beam)
		wm.bindEntryTwoWay(self.beamFeetEntry,	 	self.app.ship.hull.beamft)
		wm.bindEntryTwoWay(self.draftMeterEntry,	self.app.ship.hull.draft)
		wm.bindEntryTwoWay(self.draftFeetEntry, 	self.app.ship.hull.draftft)

		wm.restrictEntryNumeric(self.lengthMeterEntry)
		wm.restrictEntryNumeric(self.lengthFeetEntry)
		wm.restrictEntryNumeric(self.beamMeterEntry)
		wm.restrictEntryNumeric(self.beamFeetEntry)
		wm.restrictEntryNumeric(self.draftMeterEntry)
		wm.restrictEntryNumeric(self.draftFeetEntry)

		self.unitCombo.bind('<<ComboboxSelected>>', func=self.selectUnit)
		self.unitCombo.set(self.app.enums.Unit.METRIC)
		self.selectUnit()
#endregion
#region interactivity

	def selectUnit(self, event = None):
		unit = self.app.enums.Unit(self.unitCombo.get())
		wm.switchUnits(self.unitWidgets, unit=unit)

#endregion


if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =DimensionData(root, app)
	screen.base.grid()
	root.mainloop()