from enum import Enum
from tkinter import font
import tkinter as tk
import tkinter.ttk as ttk
#import constants

def _boldFont() -> font.Font:
	return font.Font(weight='bold')

def create_entry(parent : tk.Misc, state=tk.NORMAL) -> tk.Entry:
	entry = tk.Entry(parent, state=state) 
	return entry

def create_label(parent : tk.Misc, text='') -> tk.Label:
	label = tk.Label(parent, text=text)
	return label

def create_title_label(parent : tk.Misc, text='') -> tk.Label:
	label = create_label(parent, text=text)
	label.config(font=_boldFont())
	return label

def create_frame(parent : tk.Misc, width=0) -> tk.Frame:
	frame = tk.Frame(parent,width=width) 
	return frame

def create_root() -> tk.Tk:
	return tk.Tk()

def create_paned_window(parent) -> tk.PanedWindow:
	return tk.PanedWindow(parent)

def create_notebook(parent) -> ttk.Notebook:
	return ttk.Notebook(parent)

def create_radiobutton(parent, text='', variable=None, 
                value=None) -> tk.Radiobutton:
	radButton = ttk.Radiobutton(parent, text=text, variable=variable, value=value)
	return radButton
def create_radio_set(parent : tk.Misc, enum: Enum):
	buttons = []
	var = tk.StringVar()
	for item in list(enum):
		button = create_radiobutton(parent, text=item.value, variable=var, value=item.value)
		buttons.append(button)
	return (var, buttons)

if __name__ == '__main__':
	class Fuel(Enum):
		OIL 	= 'oil'
		COAL 	= 'coal'
		BOTH 	= 'both'
	root = tk.Tk()
	create_radio_set(root, Fuel)