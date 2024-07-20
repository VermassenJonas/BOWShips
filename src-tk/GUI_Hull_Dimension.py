from tkinter import Widget
from GUI.Component import Component
from BOWS import App
import constants as constants
from GUI.WidgetManager import wm

class DimensionData(Component):
	app : App
	def __init__(self, parent : Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		
		self.titleLabel = wm.create_title_label(self.base, text=f'{app.lang.dimensions}')

		self.lengthLabel	= wm.create_label(self.base, text=f'{app.lang.length}:')
		self.beamLabel 		= wm.create_label(self.base, text=f'{app.lang.beam}:')
		self.draftLabel 	= wm.create_label(self.base, text=f'{app.lang.draft}:')
		self.meterLabel 	= wm.create_label(self.base, text=f'{app.lang.meter} (m):' )
		self.feetLabel 		= wm.create_label(self.base, text=f'{app.lang.feet} (ft):' )

		self.lengthMeterEntry 	= wm.create_entry(self.base)
		self.beamMeterEntry 	= wm.create_entry(self.base)
		self.draftMeterEntry 	= wm.create_entry(self.base)
		self.lengthFeetEntry 	= wm.create_entry(self.base)
		self.beamFeetEntry 		= wm.create_entry(self.base)
		self.draftFeetEntry 	= wm.create_entry(self.base)

		self.titleLabel.grid		(column=0, row=0, columnspan=2)
		self.lengthLabel.grid		(column=1, row=1)
		self.beamLabel.grid			(column=2, row=1)
		self.draftLabel.grid		(column=3, row=1)
		self.meterLabel.grid		(column=0, row=2)
		self.feetLabel.grid			(column=0, row=3)

		self.lengthMeterEntry.grid	(column=1, row=2)
		self.beamMeterEntry.grid	(column=2, row=2)
		self.draftMeterEntry.grid	(column=3, row=2)
		self.lengthFeetEntry.grid	(column=1, row=3)
		self.beamFeetEntry.grid		(column=2, row=3)
		self.draftFeetEntry.grid	(column=3, row=3)

		self.doRigging()

	def doRigging(self):

		self.bindEntryCallback(self.lengthMeterEntry, 	self.app.ship.length)
		self.bindEntryCallback(self.lengthFeetEntry, 	self.app.ship.lengthft)
		self.bindEntryCallback(self.beamMeterEntry, 	self.app.ship.beam)
		self.bindEntryCallback(self.beamFeetEntry,	 	self.app.ship.beamft)
		self.bindEntryCallback(self.draftMeterEntry,	self.app.ship.draft)
		self.bindEntryCallback(self.draftFeetEntry, 	self.app.ship.draftft)

		self.bindEntryRead(self.lengthMeterEntry, 		self.app.ship.length)
		self.bindEntryRead(self.lengthFeetEntry, 		self.app.ship.lengthft)
		self.bindEntryRead(self.beamMeterEntry, 		self.app.ship.beam)
		self.bindEntryRead(self.beamFeetEntry, 			self.app.ship.beamft)
		self.bindEntryRead(self.draftMeterEntry, 		self.app.ship.draft)
		self.bindEntryRead(self.draftFeetEntry, 		self.app.ship.draftft)

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen =DimensionData(root, app)
	screen.base.grid()
	root.mainloop()