from tkinter import Misc, Widget
from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class ArmourBelt(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.titleLabel = wm.create_title_label(self.base, app.lang('belt_and_bulkheads'))
		self.titleLabel.grid(row=0, columnspan=5)
		self.unitWidgets = []
		# top labels
		self.drawTopLabels(1)
		#first row
		self.drawMainBelt(2)

	def drawTopLabels(self, row):
		self.thicknessLabelMM = wm.create_label(self.base, self.app.lang('thickness_mm'), dataType=self.app.enums.Unit.METRIC, widgetList=self.unitWidgets)
		self.thicknessLabelIN = wm.create_label(self.base, self.app.lang('thickness_in'), dataType=self.app.enums.Unit.IMPERIAL, widgetList=self.unitWidgets)
		
		self.lengthLabelM = wm.create_label(self.base, self.app.lang('length_m'), dataType=self.app.enums.Unit.METRIC, widgetList=self.unitWidgets)
		self.lengthLabelFt = wm.create_label(self.base, self.app.lang('length_ft'), dataType=self.app.enums.Unit.IMPERIAL, widgetList=self.unitWidgets)
		
		self.heightLabelM = wm.create_label(self.base, self.app.lang('height_m'), dataType=self.app.enums.Unit.METRIC, widgetList=self.unitWidgets)
		self.heightLabelFt = wm.create_label(self.base, self.app.lang('height_ft'), dataType=self.app.enums.Unit.IMPERIAL, widgetList=self.unitWidgets)
		

		self.thicknessLabelMM	.grid(row=row, column=1)
		self.thicknessLabelIN	.grid(row=row, column=2)

		self.lengthLabelM		.grid(row=row, column=3)
		self.lengthLabelFt		.grid(row=row, column=4)

		self.heightLabelM		.grid(row=row, column=5)
		self.heightLabelFt		.grid(row=row, column=6)


	def drawMainBelt(self, row):
		self.mainBeltLabel = wm.create_label(self.base, self.app.lang('main_belt'))

		self.mainBeltThickMM = wm.create_numeric_entry(self.base, dataType=self.app.enums.Unit.METRIC, widgetList=self.unitWidgets)
		self.mainBeltThickIN = wm.create_numeric_entry(self.base, dataType=self.app.enums.Unit.IMPERIAL, widgetList=self.unitWidgets)
		
		self.mainBeltLenM = wm.create_numeric_entry(self.base, dataType=self.app.enums.Unit.METRIC, widgetList=self.unitWidgets)
		self.mainBeltLenFt = wm.create_numeric_entry(self.base, dataType=self.app.enums.Unit.IMPERIAL, widgetList=self.unitWidgets)
		
		self.mainBeltHeightM = wm.create_numeric_entry(self.base, dataType=self.app.enums.Unit.METRIC, widgetList=self.unitWidgets)
		self.mainBeltHeightFt = wm.create_numeric_entry(self.base, dataType=self.app.enums.Unit.IMPERIAL, widgetList=self.unitWidgets)
		
		self.mainBeltLabel		.grid(row=row, column=0)

		self.mainBeltThickMM	.grid(row=row, column=1)
		self.mainBeltThickIN	.grid(row=row, column=2)

		self.mainBeltLenM		.grid(row=row, column=3)
		self.mainBeltLenFt		.grid(row=row, column=4)

		self.mainBeltHeightM	.grid(row=row, column=5)
		self.mainBeltHeightFt	.grid(row=row, column=6)
		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =ArmourBelt(root, app)
	screen.base.pack()
	root.mainloop()