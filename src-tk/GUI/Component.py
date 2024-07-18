import tkinter as tk

class Component:
	def __init__(self, parent, app):
		self.parent = parent
		self.app = app
	
	def bindEntry(entry, fn):
		#entry.bind('<Return>', fn)
		#entry.bind('<FocusOut>', fn)
		entry.bind('<Key>', fn)