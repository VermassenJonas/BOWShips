from os import TMP_MAX
from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm
from logic import Enums
class SingleBelt:
	def __init__(self, label, thickMM, thickIN, lenM, lenFt, heiM, HeiFt, weight) -> None:
		self.label = label
		self.thickMM = thickMM
		self.thickIN = thickIN
		self.lenM = lenM
		self.lenFt = lenFt
		self.heiM = heiM
		self.HeiFt = HeiFt
		self.weight = weight

class BeltArmour(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.titleLabel = wm.create_title_label(self.base, app.lang('belt_and_bulkheads'))
		self.titleLabel.grid(row=0, columnspan=5)
		self.unitWidgets = []
		self.hiddenBelts = [
			app.enums.Belt.MACHINERY_BELT,
			app.enums.Belt.MAGAZINES_BELT,
		]
		self.belts = {}
		# top labels
		self.drawTopLabels(1)
		row = 2
		# belts themselves
		for belt in list(app.enums.Belt):
			self.drawBelt(row, belt)
			row += 1

		self.selectUnit()
		self.hideUnusedBelts()

	def drawTopLabels(self, row):

		self.unitCombo = wm.create_ComboBox(self.base, list(self.app.enums.Unit))
		self.unitCombo.bind('<<ComboboxSelected>>', func=self.selectUnit)
		self.unitCombo.set(self.app.enums.Unit.METRIC)
		
		self.thicknessLabelMM = wm.create_label(self.base, self.app.lang('thickness_mm'), dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.thicknessLabelIN = wm.create_label(self.base, self.app.lang('thickness_in'), dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		
		self.lengthLabelM = wm.create_label(self.base, self.app.lang('length_m'), dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.lengthLabelFt = wm.create_label(self.base, self.app.lang('length_ft'), dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		
		self.heightLabelM = wm.create_label(self.base, self.app.lang('height_m'), dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.heightLabelFt = wm.create_label(self.base, self.app.lang('height_ft'), dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		
		self.weightLabel = wm.create_label(self.base, self.app.lang('weight_ton'),
					dataType=[self.app.enums.Unit.IMPERIAL, self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)

		self.unitCombo			.grid(column=0, row=row)

		self.thicknessLabelMM	.grid(row=row, column=2)
		self.thicknessLabelIN	.grid(row=row, column=2)

		self.lengthLabelM		.grid(row=row, column=4)
		self.lengthLabelFt		.grid(row=row, column=4)

		self.heightLabelM		.grid(row=row, column=6)
		self.heightLabelFt		.grid(row=row, column=6)

		self.weightLabel		.grid(row=row, column=8)


	def drawBelt(self, row, belt : Enums.Belt):
		beltLabel = wm.create_label(self.base, text=self.app.lang(str(belt)),
				dataType=[belt,self.app.enums.Unit.METRIC, self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)

		beltThickMM = wm.create_numeric_entry(self.base, 	
				dataType=[belt,self.app.enums.Unit.METRIC],  widgetList=self.unitWidgets)
		beltThickIN = wm.create_numeric_entry(self.base, 	
				dataType=[belt,self.app.enums.Unit.IMPERIAL],widgetList=self.unitWidgets)

		beltLenM = 	wm.create_numeric_entry(self.base, 	
				dataType=[belt,self.app.enums.Unit.METRIC],  widgetList=self.unitWidgets)
		beltLenFt =	wm.create_numeric_entry(self.base, 	
				dataType=[belt,self.app.enums.Unit.IMPERIAL],widgetList=self.unitWidgets)

		beltHeightM = 	wm.create_numeric_entry(self.base, 	
				dataType=[belt,self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		beltHeightFt = wm.create_numeric_entry(self.base, 	
				dataType=[belt,self.app.enums.Unit.IMPERIAL],widgetList=self.unitWidgets)
		beltWeight = wm.create_numeric_entry(self.base, widgetList=self.unitWidgets,
				dataType=[belt, self.app.enums.Unit.METRIC, self.app.enums.Unit.IMPERIAL])

		beltLabel		.grid(row=row, column=0)
		beltThickMM		.grid(row=row, column=2)
		beltThickIN		.grid(row=row, column=2)
		beltLenM		.grid(row=row, column=4)
		beltLenFt		.grid(row=row, column=4)
		beltHeightM		.grid(row=row, column=6)
		beltHeightFt	.grid(row=row, column=6)
		beltWeight		.grid(row=row, column=8)

		self.belts[belt] = SingleBelt(label=beltLabel,
									thickMM=beltThickMM,
									thickIN=beltThickIN,
									lenM=beltLenM,
									lenFt=beltLenFt,
									heiM=beltHeightM,
									HeiFt=beltHeightFt,
									weight = beltWeight)
		beltData = self.app.ship.citadel.armourBelts[belt]
		wm.bindEntryTwoWay(beltThickMM, beltData.thickness)
		wm.bindEntryTwoWay(beltThickIN, beltData.thicknessIn)
		wm.bindEntryTwoWay(beltLenM, beltData.length)
		wm.bindEntryTwoWay(beltLenFt, beltData.lengthFt)
		wm.bindEntryTwoWay(beltHeightM, beltData.height)
		wm.bindEntryTwoWay(beltHeightFt, beltData.heightFt)
		wm.bindEntryTwoWay(beltWeight, beltData.weight)

#region interactivity

	def selectUnit(self, event = None):
		unit = self.app.enums.Unit(self.unitCombo.get())
		wm.switchUnits(self.unitWidgets, unit=unit)
		self.hideUnusedBelts()

	def hideUnusedBelts(self):
		for widget in self.unitWidgets:
			if any(belt in self.hiddenBelts for belt in widget.dataType):
				widget.grid_remove()
#endregion 
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =BeltArmour(root, app)
	screen.base.pack()
	root.mainloop()