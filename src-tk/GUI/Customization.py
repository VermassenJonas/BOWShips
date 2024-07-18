from tkinter import font
import tkinter as tk
def _boldFont() -> font.Font:
	return font.Font(weight='bold')


def configHeader(label : tk.Label):
	label.config(font=_boldFont())