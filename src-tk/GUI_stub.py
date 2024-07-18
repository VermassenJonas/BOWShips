import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from BOWS import App
import GUI.constants as GUIconst


class Stub(Component):
	def __init__(self, parent : tk.Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=GUIconst.framewidth)

		

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =Stub(root, app)
	screen.base.pack()
	root.mainloop()