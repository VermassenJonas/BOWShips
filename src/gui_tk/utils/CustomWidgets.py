from abc import ABC
from tkinter import Entry, Label, Widget

class CustomWidget(ABC, Widget):
	def __init__(self, dataType):
		self.dataType = dataType

class CustomEntry(CustomWidget, Entry):
	def __init__(self, parent, dataType , *args, **kwds):
		CustomWidget.__init__(self, dataType=dataType)
		Entry.__init__(self, parent, *args, **kwds)

class CustomLabel(CustomWidget, Label):
	def __init__(self, parent, dataType , *args, **kwds):
		CustomWidget.__init__(self, dataType=dataType)
		Label.__init__(self, parent, *args, **kwds)
