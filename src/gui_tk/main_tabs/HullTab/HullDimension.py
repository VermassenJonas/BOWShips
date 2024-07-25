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

		self.lengthMeterEntry 	= wm.create_entry(self.base)
		self.beamMeterEntry 	= wm.create_entry(self.base)
		self.draftMeterEntry 	= wm.create_entry(self.base)
		self.meterWidgets = [
			self.lengthMeterEntry,
			self.beamMeterEntry,
			self.draftMeterEntry
		]


		self.lengthFeetEntry 	= wm.create_entry(self.base)
		self.beamFeetEntry 		= wm.create_entry(self.base)
		self.draftFeetEntry 	= wm.create_entry(self.base)
		self.feetWidgets = [
			self.lengthFeetEntry,
			self.beamFeetEntry,
			self.draftFeetEntry
		]


		self.titleLabel.grid		(column=0, row=0, columnspan=2)
		self.lengthLabel.grid		(column=1, row=1)
		self.beamLabel.grid			(column=2, row=1)
		self.draftLabel.grid		(column=3, row=1)

		self.lengthMeterEntry.grid	(column=1, row=2)
		self.beamMeterEntry.grid	(column=2, row=2)
		self.draftMeterEntry.grid	(column=3, row=2)

		self.lengthFeetEntry.grid	(column=1, row=2)
		self.beamFeetEntry.grid		(column=2, row=2)
		self.draftFeetEntry.grid	(column=3, row=2)

		self.unitCombo = wm.create_ComboBox(self.base, list(self.app.enums.Unit))
		
		self.unitCombo.grid(row=2, column=0)

		self.doRigging()
#endregion
#region rigging
	def doRigging(self):
		wm.bindEntryTwoWay(self.lengthMeterEntry, 	self.app.ship.length)
		wm.bindEntryTwoWay(self.lengthFeetEntry, 	self.app.ship.lengthft)
		wm.bindEntryTwoWay(self.beamMeterEntry, 	self.app.ship.beam)
		wm.bindEntryTwoWay(self.beamFeetEntry,	 	self.app.ship.beamft)
		wm.bindEntryTwoWay(self.draftMeterEntry,	self.app.ship.draft)
		wm.bindEntryTwoWay(self.draftFeetEntry, 	self.app.ship.draftft)

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
	def hideFeet(self):
		wm.hideWidgetsGrid(*self.feetWidgets)
	def showFeet(self):
		wm.showWidgetsGrid(*self.feetWidgets)
	def hideMeter(self):
		wm.hideWidgetsGrid(*self.meterWidgets)
	def showMeter(self):
		wm.showWidgetsGrid(*self.meterWidgets)

	def selectUnit(self, event = None):
		unit = self.unitCombo.get()
		if unit == self.app.enums.Unit.IMPERIAL:
			self.hideMeter()
			self.showFeet()
		else:
			self.hideFeet()
			self.showMeter()

#endregion


if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =DimensionData(root, app)
	screen.base.grid()
	root.mainloop()