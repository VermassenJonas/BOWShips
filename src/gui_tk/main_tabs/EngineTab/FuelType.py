from tkinter import ACTIVE, NORMAL, Misc, Widget, StringVar, DISABLED
from gui_tk.tk_main import App
import logic.Enums as enums
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class FuelType(Component):
	def __init__(self, parent : Misc, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.base.grid(column=0, row=1)
		self.fuelLabel = wm.create_label(self.base, self.app.lang('fuel'))
		self.fuelLabel.grid()
		(self.fuelVar, self.fuelButtons) = wm.create_radio_set(self.base, app, enums.Fuel)
		for button in self.fuelButtons:
			button.grid()		
		#self.percVar = StringVar(self.base)
		self.percEntry = wm.create_entry(self.base)
		#self.percEntry.config(textvariable=self.percVar)
		self.percEntry.grid()
		self.doRigging()

	def doRigging(self):
		self.fuelVar.set( str(self.app.ship.engine.fuelType()))
		self.confFuelField()
		wm.bindVarTwoWays(self.fuelVar, self.app.ship.engine.fuelType)
		self.app.ship.engine.fuelType.addCallback(self.confFuelField)

		wm.bindEntryTwoWay(self.percEntry, self.app.ship.engine.coalPercent)
		#self.bindVarRead(self.percVar, self.app.ship.coalPercent)


	def confFuelField(self, value = None):
		if value is None:
			value = self.app.ship.engine.fuelType()
		if value == enums.Fuel.COAL:
			self.app.ship.engine.coalPercent('100')
			self.percEntry.config(state=DISABLED)
		elif value == enums.Fuel.MIXED:
			self.percEntry.config(state=NORMAL)
		elif value == enums.Fuel.OIL:			
			self.app.ship.engine.coalPercent('0')
			self.percEntry.config(state=DISABLED)
		else:
			print(f'panic in {self}')

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =FuelType(root, app)
	screen.base.pack()
	root.mainloop()