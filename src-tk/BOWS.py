import tkinter as tk
import tkinter.ttk as ttk

import translations.en as en_lang
from GUI.Component import Component
from GUI_MainContent import MainContent
class App(Component):
	def __init__(self, parent, app) -> None:
		super().__init__(parent, app)
		self.app = self
		self.readCBs = []
		self.calcCBs = []
		self.updateCBs = []
		self.process()
		self.lang = en_lang

	def draw(self):		
		self.base = tk.Frame(self.parent)
		mainContent = MainContent(self.base,self)
		self.parent.title(self.lang.main_title)
		self.base.pack()
		mainContent.base.pack()
	def process(self):
		print('update')
		for f in self.readCBs:
			f()
		for f in self.calcCBs:
			f()
		for f in self.updateCBs:
			f()
		self.parent.after(300, self.process)

	

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	app = App(root, None)
	app.draw()
	root.mainloop()