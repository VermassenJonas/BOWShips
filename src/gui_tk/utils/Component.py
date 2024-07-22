import tkinter as tk
from functools import partial
from BOWS import App
from logic.Property import Property
class Component:
	def __init__(self, parent : tk.Misc, app : App):
		self.parent = parent
		self.app = app
	
	def bindEntryRead(self, entry : tk.Entry, var_fn):
		fn = partial(var_fn, val_fn=entry.get)
		entry.bind('<Return>', fn)
		entry.bind('<FocusOut>', fn)
	def bindEntryCallback(self, entry : tk.Entry , property : Property):			
		def _updateEntry( element : tk.Entry, _property):
			element.delete(0, tk.END)
			element.insert(0, str(_property()))
		property.addCallback(partial(_updateEntry, entry, property))
	def bindVarRead(self, var : tk.StringVar, _property: Property):
		def _readVar(*args):
			_property(var.get())
		var.trace_add('write', _readVar)