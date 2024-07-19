import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
from GUI.Component import Component
from BOWS import App
import constants as constants
import GUI.Customization as GuiCust
class DimensionData(Component):
	app : App
	def __init__(self, parent : tk.Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=constants.framewidth)
		
		self.titleLabel = tk.Label(self.base, text=f'{app.lang.dimensions}')
		GuiCust.configHeader(self.titleLabel)

		self.lengthLabel	= tk.Label(self.base, text=f'{app.lang.length}:')
		self.beamLabel 		= tk.Label(self.base, text=f'{app.lang.beam}:')
		self.draftLabel 	= tk.Label(self.base, text=f'{app.lang.draft}:')
		self.meterLabel 	= tk.Label(self.base, text=f'{app.lang.meter} (m):' )
		self.feetLabel 		= tk.Label(self.base, text=f'{app.lang.feet} (ft):' )

		self.lengthMeterEntry 	= tk.Entry(self.base)
		self.lengthFeetEntry 	= tk.Entry(self.base)
		self.beamMeterEntry 	= tk.Entry(self.base)
		self.beamFeetEntry 		= tk.Entry(self.base)
		self.draftMeterEntry 	= tk.Entry(self.base)
		self.draftFeetEntry 	= tk.Entry(self.base)

		self.titleLabel.grid	(column=0, row=0, columnspan=2)
		self.lengthLabel.grid	(column=1, row=1)
		self.beamLabel.grid		(column=2, row=1)
		self.draftLabel.grid	(column=3, row=1)
		self.meterLabel.grid	(column=0, row=2)
		self.feetLabel.grid		(column=0, row=3)

		self.lengthMeterEntry.grid	(column=1, row=2)
		self.lengthFeetEntry.grid	(column=1, row=3)
		self.beamMeterEntry.grid	(column=2, row=2)
		self.beamFeetEntry.grid		(column=2, row=3)
		self.draftMeterEntry.grid	(column=3, row=2)
		self.draftFeetEntry.grid	(column=3, row=3)

		self.doRigging()

	def doRigging(self):
		#self.app.subscribe_update(*self.deferEntryUpdate(self.beamMeterEntry, 	self.app.ship.beam))
		#self.app.subscribe_update(*self.deferEntryUpdate(self.beamFeetEntry, 	self.app.ship.beamft))
		#self.app.subscribe_update(*self.deferEntryUpdate(self.draftMeterEntry, 	self.app.ship.draft))
		#self.app.subscribe_update(*self.deferEntryUpdate(self.draftFeetEntry, 	self.app.ship.draftft))

		self.app.ship.length.addCallback(partial(self._updateEntry, self.lengthMeterEntry))
		self.app.ship.lengthft.addCallback(partial(self._updateEntry, self.lengthFeetEntry))

		self.bindEntryRead(self.lengthMeterEntry, self.app.ship.length)
		self.bindEntryRead(self.lengthFeetEntry, self.app.ship.lengthft)
		#self.bindEntry(*self.deferRead(self.beamMeterEntry, 	self.app.ship.beam))
		#self.bindEntry(*self.deferRead(self.beamFeetEntry, 		self.app.ship.beamft))
		#self.bindEntry(*self.deferRead(self.draftMeterEntry, 	self.app.ship.draft))
		#self.bindEntry(*self.deferRead(self.draftFeetEntry, 	self.app.ship.draftft))

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =DimensionData(root, app)
	screen.base.grid()
	root.mainloop()