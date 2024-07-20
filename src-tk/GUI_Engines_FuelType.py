from tkinter import ACTIVE, NORMAL, Widget, StringVar, DISABLED
from GUI.Component import Component
from BOWS import App
import constants
from GUI.WidgetManager import wm
import logic.Enums as enums

class FuelType(Component):
	def __init__(self, parent : Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.base.grid(column=0, row=1)
		self.fuelLabel = wm.create_label(self.base, self.app.lang.fuel)
		self.fuelLabel.grid()
		(self.fuelVar, self.fuelButtons) = wm.create_radio_set(self.base, app, enums.Fuel)
		for button in self.fuelButtons:
			button.grid()		
		self.percVar = StringVar(self.base)
		self.percEntry = wm.create_entry(self.base)
		self.percEntry.config(textvariable=self.percVar)
		self.percEntry.grid()
		self.doRigging()

	def doRigging(self):
		self.fuelVar.set( self.app.ship.fuelType().name)
		self.confFuelField(self.app.ship.fuelType())
		self.bindVarRead(self.fuelVar, self.app.ship.fuelType)
		self.app.ship.fuelType.addCallback(self.confFuelField)

		self.bindVarRead(self.percVar, self.app.ship.coalPercent)


	def confFuelField(self, value : enums.Fuel | None):
		if value == enums.Fuel.COAL:
			self.percEntry.config(state=DISABLED)
			self.percVar.set('100')
		elif value == enums.Fuel.MIXED:
			self.percEntry.config(state=NORMAL)
		elif value == enums.Fuel.OIL:			
			self.percEntry.config(state=DISABLED)
			self.percVar.set('0')
		else:
			print(f'panic in {self}')

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen =FuelType(root, app)
	screen.base.pack()
	root.mainloop()