import tkinter as tk
from functools import partial
from BOWS import App
from logic.Property import Property
class Component:
	def __init__(self, parent : tk.Misc, app : App):
		self.parent = parent
		self.app = app
	
	def bindEntryRead(self, entry : tk.Entry, property : Property):
		fn = partial(property, val_fn=entry.get)
		entry.bind('<Return>', fn)
		entry.bind('<FocusOut>', fn)
		
	def bindEntryCallback(self, entry : tk.Entry , property : Property):			
		def _updateEntry( element : tk.Entry, _property):
			element.delete(0, tk.END)
			element.insert(0, str(_property()))
		property.addCallback(partial(_updateEntry, entry, property))
		_updateEntry(entry, property)

	def bindVarRead(self, var : tk.StringVar, property: Property):
		def _readVar(*args):
			if len(var.get()) and var.get()[-1] == '.':
				pass
			else:
				property(var.get())
		var.trace_add('write', _readVar)

	def bindVarCallback(self, var : tk.StringVar, property : Property):
		def _updateVar(_var : tk.StringVar, prop : Property):
			_var.set(str(prop()))
		property.addCallback(partial(_updateVar, var, property))
		_updateVar(var, property)

	def bindVarTwoWays(self, var: tk.StringVar, property : Property):
		self.bindVarRead(var, property)
		self.bindVarCallback(var, property)
