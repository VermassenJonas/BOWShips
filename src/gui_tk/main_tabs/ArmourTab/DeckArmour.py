from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class SingleDeck:
	def __init__(self, label, thickMM, thickIN, lenM, lenFt, weight) -> None:
		self.label = label
		self.thickMM = thickMM
		self.thickIN = thickIN
		self.lenM = lenM
		self.lenFt = lenFt
		self.weight = weight

class DeckArmour(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.titleLabel = wm.create_title_label(self.base, app.lang('deck_armour'))
		self.titleLabel.grid(row=0, columnspan=5)
		self.unitWidgets = []

		self.drawConfig()
		self.drawDecks(4)


	def drawConfig(self):
		pass
	def drawDecks(self, startrow):

		self.thicknessMMlabel = wm.create_label(self.base, self.app.lang('thickness_mm'),dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.thicknessInlabel = wm.create_label(self.base, self.app.lang('thickness_in'),dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.lengthMLabel = 	wm.create_label(self.base, self.app.lang('length_m'),dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.lengthFtLabel = 	wm.create_label(self.base, self.app.lang('length_ft'),dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.weightLabel = 		wm.create_label(self.base, self.app.lang('weight_ton'))

		self.mainDeckLabel = 			wm.create_label(self.base, self.app.lang('main_deck'))		
		self.mainDeckThickEntry = 		wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.mainDeckThickInEntry = 	wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.mainDeckLengthEntry =		wm.create_readOnly_entry(self.base, dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.mainDeckLengthFtEntry = 	wm.create_readOnly_entry(self.base, dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.mainDeckWeight = 			wm.create_numeric_entry(self.base)

		self.foreDeckLabel =			wm.create_label(self.base, self.app.lang('fore_deck'))		
		self.foreDeckThickEntry = 		wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.foreDeckThickInEntry = 	wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.foreDeckLengthEntry = 		wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.foreDeckLengthFtEntry = 	wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.foreDeckWeight = 			wm.create_numeric_entry(self.base)

		self.aftDeckLabel = 		wm.create_label(self.base, self.app.lang('aft_deft'))		
		self.aftDeckThickEntry = 	wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.aftDeckThickInEntry = 	wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.aftDeckLengthEntry = 	wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.aftDeckLengthFtEntry = wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.aftDeckWeight = 		wm.create_numeric_entry(self.base)

		self.thicknessMMlabel		.grid(column=1, row=startrow)
		self.thicknessInlabel		.grid(column=1, row=startrow)
		self.lengthMLabel			.grid(column=3, row=startrow)
		self.lengthFtLabel			.grid(column=3, row=startrow)
		self.weightLabel			.grid(column=5, row=startrow)

		self.mainDeckLabel			.grid(column=0, row=startrow+1)
		self.mainDeckThickEntry		.grid(column=1, row=startrow+1)
		self.mainDeckThickInEntry	.grid(column=1, row=startrow+1)
		self.mainDeckLengthEntry 	.grid(column=3, row=startrow+1)
		self.mainDeckLengthFtEntry	.grid(column=3, row=startrow+1)
		self.mainDeckWeight			.grid(column=5, row=startrow+1)

		self.foreDeckLabel			.grid(column=0, row=startrow+2)
		self.foreDeckThickEntry		.grid(column=1, row=startrow+2)
		self.foreDeckThickInEntry	.grid(column=1, row=startrow+2)
		self.foreDeckLengthEntry 	.grid(column=3, row=startrow+2)
		self.foreDeckLengthFtEntry	.grid(column=3, row=startrow+2)
		self.foreDeckWeight			.grid(column=5, row=startrow+2) 

		self.aftDeckLabel			.grid(column=0, row=startrow+3)
		self.aftDeckThickEntry		.grid(column=1, row=startrow+3)
		self.aftDeckThickInEntry	.grid(column=1, row=startrow+3)
		self.aftDeckLengthEntry 	.grid(column=3, row=startrow+3)
		self.aftDeckLengthFtEntry	.grid(column=3, row=startrow+3)
		self.aftDeckWeight			.grid(column=5, row=startrow+3)

	def drawDeck(self, row, belt):
		pass


		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen = DeckArmour(root, app)
	screen.base.pack()
	root.mainloop()