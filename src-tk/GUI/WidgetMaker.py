from enum import Enum
from functools import partial
from tkinter import font
import tkinter as tk
import tkinter.ttk as ttk

def _boldFont() -> font.Font:
	return font.Font(weight='bold')

def _standardizeAlignment(widget : tk.Widget):
	widget.grid = partial(widget.grid, sticky=tk.W)

def create_entry(parent : tk.Misc) -> tk.Entry:
	widget = tk.Entry(parent) 
	_standardizeAlignment(widget)
	return widget

def create_label(parent : tk.Misc, text='') -> tk.Label:
	widget = tk.Label(parent, text=text)
	_standardizeAlignment(widget)
	return widget

def create_frame(parent : tk.Misc) -> tk.Frame:
	widget = tk.Frame(parent)
	widget.config(highlightbackground='red', highlightthickness=0.5) # debug line
	widget.grid_configure(ipadx=5, ipady=5)
	_standardizeAlignment(widget)	
	return widget

def create_title_label(parent : tk.Misc, text='') -> tk.Label:
	widget = create_label(parent, text=text)
	widget.config(font=_boldFont())
	return widget

def create_paned_window(parent) -> tk.PanedWindow:
	widget = tk.PanedWindow(parent)
	_standardizeAlignment(widget)	
	return widget

def create_notebook(parent) -> ttk.Notebook:
	widget = ttk.Notebook(parent)
	_standardizeAlignment(widget)	
	return widget

def create_radiobutton(parent, text='', variable=None, 
                value=None) -> tk.Radiobutton:
	widget = ttk.Radiobutton(parent, text=text, variable=variable, value=value)
	_standardizeAlignment(widget)
	return widget

def create_radio_set(parent : tk.Misc,app, enum: Enum):
	buttons = []
	var = tk.StringVar()
	for item in list(enum):
		button = create_radiobutton(parent, text=app.lang(item.value), variable=var, value=item.name)
		buttons.append(button)
	return (var, buttons)

def create_root() -> tk.Tk:
	return tk.Tk()

if __name__ == '__main__':
	class Fuel(Enum):
		OIL 	= 'oil'
		COAL 	= 'coal'
		BOTH 	= 'both'
	root = tk.Tk()
	create_radio_set(root, Fuel)