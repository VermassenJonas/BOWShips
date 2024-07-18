import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from GUI.Customization import boldFont
from BOWS import App 
import GUI.constants as GUIconst

class GeneralData(Component):
	def __init__(self, parent : tk.Widget, app : App) -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=GUIconst.framewidth)

		self.labelTitle = tk.Label(self.base, text=app.lang.ship)
		self.labelTitle.config(font=boldFont())
		self.nameLabel = tk.Label(self.base, text=f'{app.lang.name}:')
		self.nameEntry = tk.Entry(self.base)
		self.countryLabel = tk.Label(self.base, text=f'{app.lang.country}:')
		self.countryEntry = tk.Entry(self.base)
		self.typeLabel = tk.Label(self.base, text=f'{app.lang.type}:')
		self.typeEntry = tk.Entry(self.base)

		self.yearLabel = tk.Label(self.base, text=f'{app.lang.year}:')
		self.laidDownLabel = tk.Label(self.base, text=f'{app.lang.laid_down}:')
		self.laidDownEntry = tk.Entry(self.base)
		self.engineBuiltLabel = tk.Label(self.base, text=f'{app.lang.engine_built}:')
		self.engineBuiltEntry = tk.Entry(self.base)


		self.labelTitle.grid(column=0, row=0)
		self.nameLabel.grid(column=0, row=1)
		self.nameEntry.grid(column=1, row=1)
		self.countryLabel.grid(column=0, row=2)
		self.countryEntry.grid(column=1, row=2)
		self.typeLabel.grid(column=0, row=3)
		self.typeEntry.grid(column=1, row=3)
		self.yearLabel.grid(column=3, row=1)
		self.laidDownLabel.grid(column=2, row=2)
		self.laidDownEntry.grid(column=3, row=2)
		self.engineBuiltLabel.grid(column=2, row=3)
		self.engineBuiltEntry.grid(column=3, row=3)
		

if __name__ == "__main__":	
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =GeneralData(root, app)
	screen.base.grid()
	root.mainloop()