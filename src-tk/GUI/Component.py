import tkinter as tk
from functools import partial
class Component:
	def __init__(self, parent, app):
		self.parent = parent
		self.app = app
	
	def bindEntry(self, entry : tk.Entry, fn):
		#entry.bind('<Return>', fn)
		#entry.bind('<FocusOut>', fn)
		entry.bind('<Key>', fn)

	def readEntry(self, entry : tk.Entry, var, e):
		print(e)
		print(f'{var}, {entry.get()}')
		var = entry.get()
		print(var)
	
	def updateEntry(self, element : tk.Entry, value):
		element.delete(0, tk.END)
		element.insert(0, str(value))
	
	def deferEntryUpdate(self,element : tk.Entry, value):
		return (element,partial(self.updateEntry, element, value))