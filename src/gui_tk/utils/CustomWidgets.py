from tkinter import Entry


class CustomEntry(Entry):
	def __init__(self, parent, dataType , *args, **kwds):
		self.dataType = dataType
		super().__init__(parent, *args, **kwds)