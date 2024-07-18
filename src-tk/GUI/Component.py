import tkinter as tk
from functools import partial
class Component:
	def __init__(self, parent, app):
		self.parent = parent
		self.app = app
	
	def bindEntry(self, entry : tk.Entry, fn):
		entry.bind('<Return>', fn)
		entry.bind('<FocusOut>', fn)
		#entry.bind('<Key>', fn)

	def deferRead(self,entry: tk.Entry, var_fn ):
		return (entry, partial(var_fn, val_fn=entry.get))

	
	def updateEntry(self, element : tk.Entry, val_fn):
		element.delete(0, tk.END)
		element.insert(0, str(val_fn()))
	
	def deferEntryUpdate(self,element : tk.Entry, val_fn):
		return (element,partial(self.updateEntry, element, val_fn))