from tkinter import Widget, DISABLED
from GUI.Component import Component
from BOWS import App
import constants
import GUI.WidgetMaker as wm

class SpeedPower(Component):
	def __init__(self, parent : Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base 				= wm.create_frame(self.parent)

		self.titleLabel				= wm.create_title_label(self.base, text=f'{app.lang.speed_and_power}')

		self.maxSpeedlabel 			= wm.create_label(self.base, text=self.app.lang('maxSpeed'))
		self.cruiseSpeedLabel 		= wm.create_label(self.base, text=self.app.lang('cruise_speed'))
		self.shaftCountLabel 		= wm.create_label(self.base, text=self.app.lang('shafts'))
		self.maxSpeedEntry 			= wm.create_entry(self.base)
		self.cruiseSpeedEntry 		= wm.create_entry(self.base)
		self.shaftCountEntry 		= wm.create_entry(self.base)
		self.powReqMaxHPLabel 		= wm.create_label(self.base, text=f'0Power(shp): 0x0000')


		self.titleLabel.grid		(column=0, row=0, columnspan=2)
		self.maxSpeedlabel.grid		(column=0, row=1)
		self.cruiseSpeedLabel.grid	(column=0, row=2)
		self.shaftCountLabel.grid	(column=0, row=3)
		self.maxSpeedEntry.grid		(column=1, row=1)
		self.cruiseSpeedEntry.grid	(column=1, row=2)
		self.shaftCountEntry.grid	(column=1, row=3)
		

		self.doRigging()

	def doRigging(self):
		self.cruiseSpeedEntry.config(state=DISABLED) #TODO: Cruising's for later
		pass #TODO: implement interactivity	

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen =SpeedPower(root, app)
	screen.base.grid()
	root.mainloop()