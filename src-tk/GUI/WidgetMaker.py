from tkinter import font
import tkinter as tk
import tkinter.ttk as ttk
import constants

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

def create_frame(parent : tk.Misc, width=constants.framewidth) -> tk.Frame:
	frame = tk.Frame(parent,width=width) 
	return frame

def create_root() -> tk.Tk:
	return tk.Tk()

def create_paned_window(parent) -> tk.PanedWindow:
	return tk.PanedWindow(parent)

def create_notebook(parent) -> ttk.Notebook:
	return ttk.Notebook(parent)