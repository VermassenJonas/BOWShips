from os import stat
from tkinter import DISABLED, Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm
from logic.Enums import Deck

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
		self.drawLabels(4)
		self.mainDeck = self.drawDeck(5, self.app.enums.Deck.MAIN_DECK)
		self.mainDeck.lenM.config(state=DISABLED)
		self.mainDeck.lenFt.config(state=DISABLED)
		self.foreDeck = self.drawDeck(6, self.app.enums.Deck.FORE_DECK)
		self.aftDeck = self.drawDeck(7, self.app.enums.Deck.AFT_DECK)


	def drawConfig(self):
		pass
	def drawLabels(self, row):

		self.thicknessMMlabel = wm.create_label(self.base, self.app.lang('thickness_mm'),dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.thicknessInlabel = wm.create_label(self.base, self.app.lang('thickness_in'),dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.lengthMLabel = 	wm.create_label(self.base, self.app.lang('length_m'),dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.lengthFtLabel = 	wm.create_label(self.base, self.app.lang('length_ft'),dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		self.weightLabel = 		wm.create_label(self.base, self.app.lang('weight_ton'))

		
		self.thicknessMMlabel		.grid(column=1, row=row)
		self.thicknessInlabel		.grid(column=1, row=row)
		self.lengthMLabel			.grid(column=3, row=row)
		self.lengthFtLabel			.grid(column=3, row=row)
		self.weightLabel			.grid(column=5, row=row)
		
	def drawDeck(self, row: int, deck : Deck):
		label = 			wm.create_label(self.base, self.app.lang(deck))		
		thickEntry = 		wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		thickInEntry = 	wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		lengthEntry =		wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		lengthFtEntry = 	wm.create_numeric_entry(self.base, dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		weight = 			wm.create_numeric_entry(self.base)

		label			.grid(column=0, row=row)
		thickEntry		.grid(column=1, row=row)
		thickInEntry	.grid(column=1, row=row)
		lengthEntry 	.grid(column=3, row=row)
		lengthFtEntry	.grid(column=3, row=row)
		weight			.grid(column=5, row=row)

		return SingleDeck(label=label,
						thickMM=thickEntry,
						thickIN=thickInEntry,
						lenM=lengthEntry,
						lenFt=lengthFtEntry,
						weight=weight)

		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen = DeckArmour(root, app)
	screen.base.pack()
	root.mainloop()