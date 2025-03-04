from enum import Enum
import enum
from functools import partial
from os import stat
from tkinter import DISABLED, Misc, font
import tkinter as tk
import tkinter.ttk as ttk
from typing import Any
from logic.Enums import Unit
from logic.Property import Property
from logic.Singleton import Singleton
from gui_tk.utils.CustomWidgets import CustomEntry, CustomLabel, CustomWidget
class WidgetManager(metaclass=Singleton):
	def __init__(self) -> None:
		self.widgets = {}

	def _addWidget(self, widget : tk.Widget, widgetList = None):
		key = str(type(widget))
		if not key in self.widgets:
			self.widgets[key] = [] 
		self.widgets[key].append(widget)		
		if widgetList is not None:
			widgetList.append(widget)

	#region creators 
	def create_readOnly_entry(self, parent : Misc, dataType: list[Any] = [] , widgetList = None):
		widget = self.create_entry(parent, dataType=dataType, widgetList=widgetList)
		widget.config(state=DISABLED)
		return widget

	def create_entry(self, parent : tk.Misc, dataType: list[Any] = [] , widgetList = None) :
		widget = CustomEntry(parent, dataType, width = 15)
		self._standardizeAlignment(widget)
		self._addWidget(widget, widgetList=widgetList)
		return widget

	def create_numeric_entry(self, parent : tk.Misc, dataType : list[Any]=[], widgetList = None) :
		widget = self.create_entry(parent, dataType=dataType, widgetList=widgetList)
		self.restrictEntryNumeric(widget)
		return widget

	def create_label(self, parent : tk.Misc, text, dataType : list[Any]=[], widgetList = None) :
		widget = CustomLabel(parent, text=text, dataType=dataType)
		self._standardizeAlignment(widget)
		self._addWidget(widget, widgetList)
		return widget

	def create_frame(self, parent : tk.Misc) -> tk.Frame:
		widget = tk.Frame(parent)
		#widget.config(highlightbackground='red', highlightthickness=0.5) # debug line
		widget.grid_configure(ipadx=5, ipady=5)
		self._standardizeAlignment(widget)	
		self._addWidget(widget)
		return widget

	def create_title_label(self, parent : tk.Misc, text='') -> tk.Label:
		widget = self.create_label(parent, text=text)
		widget.config(font=self._boldFont())
		self._addWidget(widget)
		return widget

	def create_paned_window(self, parent) -> tk.PanedWindow:
		widget = tk.PanedWindow(parent)
		self._standardizeAlignment(widget)	
		self._addWidget(widget)
		return widget

	def create_notebook(self, parent) -> ttk.Notebook:
		widget = ttk.Notebook(parent)
		self._standardizeAlignment(widget)	
		self._addWidget(widget)
		return widget

	def create_radiobutton(self, parent, variable : tk.StringVar, text='', 
					value=None) -> tk.Radiobutton:
		widget = tk.Radiobutton(parent, text=text, variable=variable, value=value)
		self._standardizeAlignment(widget)
		self._addWidget(widget)
		return widget

	def create_radio_set(self, parent : tk.Misc,app, enum: type[Enum]):
		buttons = []
		var = tk.StringVar()
		for item in list(enum): 
			button = self.create_radiobutton(parent, text=app.lang(item), variable=var, value=item)
			buttons.append(button)
			self._addWidget(button)
		return (var, buttons)

	def create_ComboBox(self, parent, options):		
		widget = ttk.Combobox(parent, values=options, width=15)
		widget.config(state='readonly')
		self._standardizeAlignment(widget)
		self._addWidget(widget)
		return widget

	def create_root(self) -> tk.Tk:
		return tk.Tk()
	#endregion

	#region bindings	
	
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
		def fn (event):
			value = entry.get()
			property(value = value)
		entry.bind('<Return>', fn)
		entry.bind('<FocusOut>', fn)
		entry.bind('<KP_Enter>', fn)
	


	def bindEntryCallback(self, entry : tk.Entry , property : Property):
		def _updateEntry(value):
			var = property.get()
			state = entry.cget('state')		
			entry.config(state=tk.NORMAL)	
			entry.delete(0, tk.END)
			entry.insert(0, var)
			entry.config(state=state)		
		property.addCallback(_updateEntry)
		_updateEntry(property())

	def bindVarRead(self, var : tk.StringVar, property: Property):
		def _readVar(*args):
			if len(var.get()) and var.get()[-1] == '.':
				pass
			else:
				property(var.get())
		var.trace_add('write', _readVar)

	def bindVarCallback(self, var : tk.StringVar, property : Property):
		def _updateVar(value):
			var.set(str(value))
		property.addCallback(_updateVar)
		_updateVar(property())

	def bindVarTwoWays(self, var: tk.StringVar, property : Property):
		self.bindVarRead(var, property)
		self.bindVarCallback(var, property)
	#endregion
	
	#region interactivity
	def switchUnits(self, widgets : list[CustomWidget],  unit : Unit):
		antiUnit = Unit.IMPERIAL if unit == Unit.METRIC else Unit.METRIC
		for widget in widgets:
			if unit in widget.dataType:
				widget.grid()
			elif antiUnit in widget.dataType:
				widget.grid_remove()
			else:
				pass


	def hideWidgetsGrid(self, *widgets : tk.Widget) :
		for widget in widgets:
			widget.grid_remove()
	def showWidgetsGrid(self, *widgets : tk.Widget) :
		for widget in widgets:
			widget.grid()

	#endregion
	
	#region styling
	def _boldFont(self) -> font.Font:
		return font.Font(weight='bold')

	def _standardizeAlignment(self, widget : tk.Widget):
		widget.grid = partial(widget.grid, sticky=tk.NW)
	#endregion

wm = WidgetManager()