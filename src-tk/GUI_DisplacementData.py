import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from BOWS import App
from GUI.Customization import boldFont
import GUI.constants as GUIconst

class DisplacementData(Component):
	def __init__(self, parent : tk.Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=GUIconst.framewidth)
		
		self.labelTitle = tk.Label(self.base, text=f'{app.lang.displacement}')
		self.labelTitle.config(font=boldFont())

		self.labelTitle.grid()

		



if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =DisplacementData(root, app)
	screen.base.pack()
	root.mainloop()