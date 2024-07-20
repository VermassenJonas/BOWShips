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
	def bindEntryCallback(self, entry : tk.Entry , property : Property):			
		def _updateEntry( element : tk.Entry, value):
			element.delete(0, tk.END)
			element.insert(0, str(value))
		property.addCallback(partial(_updateEntry, entry))
	def bindVarRead(self, var : tk.StringVar, property: Property):
		def _readVar(*args):
			property(var.get())
		var.trace_add('write', _readVar)