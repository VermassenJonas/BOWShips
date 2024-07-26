from os import TMP_MAX
from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm
from logic import Enums
class SingleBelt:
	def __init__(self, label, thickMM, thickIN, lenM, lenFt, heiM, HeiFt) -> None:
		self.label = label
		self.thickMM = thickMM
		self.thickIN = thickIN
		self.lenM = lenM
		self.lenFt = lenFt
		self.heiM = heiM
		self.HeiFt = HeiFt
class ArmourBelt(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.titleLabel = wm.create_title_label(self.base, app.lang('belt_and_bulkheads'))
		self.titleLabel.grid(row=0, columnspan=5)
		self.unitWidgets = []
		self.drawnBelts = [
			app.enums.Belt.MAIN_BELT,
			app.enums.Belt.UPPER_BELT,
			app.enums.Belt.EXTENDED_BELT,
			app.enums.Belt.TORPEDO_BELT,
		]
		self.belts = {}
		# top labels
		self.drawTopLabels(1)
		row = 2
		# belts themselves
		for belt in self.drawnBelts:
			self.drawBelt(row, belt)
			row += 1

	def drawTopLabels(self, row):
		self.thicknessLabelMM = wm.create_label(self.base, self.app.lang('thickness_mm'), dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.thicknessLabelIN = wm.create_label(self.base, self.app.lang('thickness_in'), dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		
		self.lengthLabelM = wm.create_label(self.base, self.app.lang('length_m'), dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.lengthLabelFt = wm.create_label(self.base, self.app.lang('length_ft'), dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		
		self.heightLabelM = wm.create_label(self.base, self.app.lang('height_m'), dataType=[self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		self.heightLabelFt = wm.create_label(self.base, self.app.lang('height_ft'), dataType=[self.app.enums.Unit.IMPERIAL], widgetList=self.unitWidgets)
		

		self.thicknessLabelMM	.grid(row=row, column=1)
		self.thicknessLabelIN	.grid(row=row, column=2)

		self.lengthLabelM		.grid(row=row, column=3)
		self.lengthLabelFt		.grid(row=row, column=4)

		self.heightLabelM		.grid(row=row, column=5)
		self.heightLabelFt		.grid(row=row, column=6)


	def drawBelt(self, row, belt : Enums.Belt):
		beltLabel = wm.create_label(self.base, self.app.lang(str(belt)))

		beltThickMM = wm.create_numeric_entry(self.base, 	dataType=[belt,self.app.enums.Unit.METRIC],  widgetList=self.unitWidgets)
		beltThickIN = wm.create_numeric_entry(self.base, 	dataType=[belt,self.app.enums.Unit.IMPERIAL],widgetList=self.unitWidgets)

		beltLenM = 	wm.create_numeric_entry(self.base, 	dataType=[belt,self.app.enums.Unit.METRIC],  widgetList=self.unitWidgets)
		beltLenFt =	wm.create_numeric_entry(self.base, 	dataType=[belt,self.app.enums.Unit.IMPERIAL],widgetList=self.unitWidgets)

		beltHeightM = 	wm.create_numeric_entry(self.base, 	dataType=[belt,self.app.enums.Unit.METRIC], widgetList=self.unitWidgets)
		beltHeightFt = wm.create_numeric_entry(self.base, 	dataType=[belt,self.app.enums.Unit.IMPERIAL],widgetList=self.unitWidgets)
	
		beltLabel		.grid(row=row, column=0)
		beltThickMM		.grid(row=row, column=1)
		beltThickIN		.grid(row=row, column=2)
		beltLenM		.grid(row=row, column=3)
		beltLenFt		.grid(row=row, column=4)
		beltHeightM		.grid(row=row, column=5)
		beltHeightFt	.grid(row=row, column=6)

		self.belts[belt] = SingleBelt(label=beltLabel,
									thickMM=beltThickMM,
									thickIN=beltThickIN,
									lenM=beltLenM,
									lenFt=beltLenFt,
									heiM=beltHeightM,
									HeiFt=beltHeightFt)
		#TODO: rigging
		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =ArmourBelt(root, app)
	screen.base.pack()
	root.mainloop()