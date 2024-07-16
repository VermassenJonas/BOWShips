import tkinter as tk
from tkinter import ttk

import translations.strings as strings
import logic.Constants as constants

import GUI.mainTabs as mainTabs
import GUI.sideTabs as sideTabs

class ControlCenter():
	def __init__(self):
		self.read_callbacks = []
		self.calc_callbacks = []
		self.update_callbacks = []

	def process(self):
		for f in self.read_callbacks:
			f()
		for f in self.calc_callbacks:
			f()
		for f in self.update_callbacks:
			f()


controlCenter = ControlCenter()

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("600x600")
	root.title(strings.main_title)

	paneHolder = tk.PanedWindow(root, orient=tk.HORIZONTAL)
	paneHolder.pack(expand=True, fill=tk.BOTH)


	mainTabs.draw(paneHolder, root)
	sideTabs.draw(paneHolder, root)


	def update():
		controlCenter.process()
		root.after(300, update)
	update() # init logic loop

	root.mainloop()  