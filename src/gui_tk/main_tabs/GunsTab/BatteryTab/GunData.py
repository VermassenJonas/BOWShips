from gui_tk.tk_main import App
from gui_tk.utils.Component import Component
from gui_tk.utils.WidgetManager import wm

class GunData(Component):
	def __init__(self, parent, app)  -> None:
		super().__init__(parent, app)
		self.base =  wm.create_frame(self.parent)
		self.title = wm.create_title_label(self.base, app.lang('gun_data'))
		self.title.grid(column=0, row=0)

		self.unitCombo = wm.create_ComboBox(self.base, list(self.app.enums.Unit))
		self.unitCombo.bind('<<ComboboxSelected>>', func=self.selectUnit)
		self.unitCombo.set(self.app.enums.Unit.METRIC)
		self.unitCombo.grid(column=2, row=0)

		

	def selectUnit(self, e):
		pass
		
if __name__ == "__main__":
	root = wm.create_root()
	root.geometry("600x600")
	app = App()
	screen =GunData(root, app)
	screen.base.pack()
	root.mainloop()