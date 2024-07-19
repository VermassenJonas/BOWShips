import tkinter as tk
from functools import partial
from logic.Property import Property
class Component:
	def __init__(self, parent, app):
		self.parent = parent
		self.app = app
	
	def bindEntryRead(self, entry : tk.Entry, var_fn):
		fn = partial(var_fn, val_fn=entry.get)
		entry.bind('<Return>', fn)
		entry.bind('<FocusOut>', fn)	
	def _updateEntry(self, element : tk.Entry, value):
		element.delete(0, tk.END)
		element.insert(0, str(value))
	def bindEntryCallback(self, entry : tk.Entry , property : Property):
		property.addCallback(partial(self._updateEntry, entry))