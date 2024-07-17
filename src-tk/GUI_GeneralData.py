import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from GUI.Customization import boldFont
from BOWS import App 
class GeneralData(Component):
	def __init__(self, parent : tk.Widget, app : App) -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=450)
		label = tk.Label(self.base, text=app.lang.ship)
		label.config(font=boldFont())
		label.pack()
		

if __name__ == "__main__":	
	from BOWS import App
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =GeneralData(root, app)
	screen.base.pack()
	root.mainloop()