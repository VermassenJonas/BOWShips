from tkinter import Widget, DISABLED
from GUI.Component import Component
from BOWS import App
import constants
import GUI.WidgetMaker as wm

class SpeedPower(Component):
	def __init__(self, parent : Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent, width=constants.framewidth)

		titleLabel = wm.create_title_label(self.base, text=f'{app.lang.speed_and_power}')
		
		maxSpeedlabel 		= wm.create_label(self.base, text='0maxSpeed')
		cruiseSpeedLabel 	= wm.create_label(self.base, text='0cruise speed')
		shaftCountLabel 	= wm.create_label(self.base, text='0shafts')
		maxSpeedEntry 		= wm.create_entry(self.base)
		cruiseSpeedEntry 	= wm.create_entry(self.base, state=DISABLED) #TODO: Cruising's for later
		shaftCountEntry 	= wm.create_entry(self.base)
		powReqMaxHPLabel 	= wm.create_label(self.base, text=f'0Power(shp): 0x0000')


		titleLabel.grid			(column=0, row=0, columnspan=2)
		maxSpeedlabel.grid		(column=0, row=1)
		cruiseSpeedLabel.grid	(column=0, row=2)
		shaftCountLabel.grid	(column=0, row=3)
		maxSpeedEntry.grid		(column=1, row=1)
		cruiseSpeedEntry.grid	(column=1, row=2)
		shaftCountEntry.grid	(column=1, row=3)
		

		self.doRigging()

	def doRigging(self):
		pass #TODO: implement interactivity	

if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App(root, None)
	screen =SpeedPower(root, app)
	screen.base.grid()
	root.mainloop()