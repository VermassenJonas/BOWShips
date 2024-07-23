import tkinter as tk
from functools import partial
from BOWS import App
from logic.Property import Property
class Component:
	def __init__(self, parent : tk.Misc, app : App):
		self.parent = parent
		self.app = app


	