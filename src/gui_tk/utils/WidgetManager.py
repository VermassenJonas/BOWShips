from enum import Enum, EnumMeta
from functools import partial
from tkinter import font
import tkinter as tk
import tkinter.ttk as ttk
from logic.Singleton import Singleton
class WidgetManager(metaclass=Singleton):
	def __init__(self) -> None:
		self.widgets = {}

	def _addWidget(self, widget : tk.Widget):
		#print(type(widget))
		#if not self.widgets[type(widget)]:
		#	self.widgets[type(widget)] = []
		#self.widgets[type(widget)].append(widget)
		pass


	def _boldFont(self) -> font.Font:
		return font.Font(weight='bold')

	def _standardizeAlignment(self, widget : tk.Widget):
		widget.grid = partial(widget.grid, sticky=tk.NW)

	def create_entry(self, parent : tk.Misc) -> tk.Entry:
		widget = tk.Entry(parent) 
		self._standardizeAlignment(widget)
		self._addWidget(widget)
		return widget

	def create_label(self, parent : tk.Misc, text='') -> tk.Label:
		widget = tk.Label(parent, text=text)
		self._standardizeAlignment(widget)
		self._addWidget(widget)
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

	def create_root(self) -> tk.Tk:
		return tk.Tk()

wm = WidgetManager()