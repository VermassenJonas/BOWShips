import tkinter as tk
import tkinter.ttk as ttk
from GUI.Component import Component
from GUI.Customization import boldFont
from BOWS import App
class DimensionData(Component):
	def __init__(self, parent : tk.Widget, app : App)  -> None:
		super().__init__(parent, app)
		self.base =  ttk.Frame(self.parent, width=450)
		
		labelTitle = tk.Label(self.base, text=app.lang.ship)
		labelTitle.config(font=boldFont())
		nameLabel = tk.Label(self.base, text=f'{app.lang.name}:')
		nameEntry = tk.Entry(self.base)
		countryLabel = tk.Label(self.base, text=f'{app.lang.country}:')
		countryEntry = tk.Entry(self.base)
		typeLabel = tk.Label(self.base, text=f'{app.lang.type}:')
		typeEntry = tk.Entry(self.base)

		yearLabel = tk.Label(self.base, text=f'{app.lang.year}:')
		laidDownLabel = tk.Label(self.base, text='0laid down')
		laidDownEntry = tk.Entry(self.base)
		engineBuiltLabel = tk.Label(self.base, text='0engine built')
		engineBuiltEntry = tk.Entry(self.base)

		labelTitle.grid(column=0, row=0)
		nameLabel.grid(column=0, row=1)
		nameEntry.grid(column=1, row=1)
		countryLabel.grid(column=0, row=2)
		countryEntry.grid(column=1, row=2)
		typeLabel.grid(column=0, row=3)
		typeEntry.grid(column=1, row=3)
		yearLabel.grid(column=3, row=1)
		laidDownLabel.grid(column=2, row=2)
		laidDownEntry.grid(column=3, row=2)
		engineBuiltLabel.grid(column=2, row=3)
		engineBuiltEntry.grid(column=3, row=3)

		

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	screen =DimensionData(root, app)
	screen.base.pack()
	root.mainloop()