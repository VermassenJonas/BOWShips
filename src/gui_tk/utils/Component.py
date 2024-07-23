import tkinter as tk
from functools import partial
from BOWS import App
from logic.Property import Property
class Component:
	def __init__(self, parent : tk.Misc, app : App):
		self.parent = parent
		self.app = app

	#def bindReadOnlyEntry(self, entry : tk.Entry, property : Property):		
	#	_var = tk.StringVar()
	#	entry.config(state=tk.DISABLED, textvariable=_var)
	#	self.bindVarTwoWays(_var, property)
	#	return _var
	def restrictEntryNumeric(self, *entries: tk.Entry):
		for entry in entries:
			def is_numeric_input(inp):
				if all(char in '0.123456789' for char in inp):
					return True
				else:
					return False
			reg = entry.master.register(is_numeric_input)
			entry.config(validate='key', validatecommand=(reg, '%P'))

	
	def bindEntryTwoWay(self, entry : tk.Entry, property : Property):
		self.bindEntryRead(entry, property)
		self.bindEntryCallback(entry, property)

	def bindEntryRead(self, entry : tk.Entry, property : Property):
		fn = partial(property, val_fn=entry.get)
		entry.bind('<Return>', fn)
		entry.bind('<FocusOut>', fn)
		entry.bind('KP_Enter', fn)
	
	def _updateEntry( self, entry : tk.Entry, property):
		var = property()
		state = entry.cget('state')		
		entry.config(state=tk.NORMAL)	
		entry.delete(0, tk.END)
		entry.insert(0, var)
		entry.config(state=state)

	def bindEntryCallback(self, entry : tk.Entry , property : Property):		
		property.addCallback(partial(self._updateEntry, entry, property))
		self._updateEntry(entry, property)

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
