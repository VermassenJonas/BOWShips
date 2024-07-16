import tkinter as tk
from tkinter import ttk

from logic.speedCalc import calcHPforSpeed  
from logic.shipData import ship
from BOWS import controlCenter
from decimal import Decimal

class engineGUI(tk.Frame):
	def __init__(self):
			
		pass
	
def draw(root):
	hpVar = tk.StringVar()
	hpVar = calcHPforSpeed()
	hpLabel = ttk.Label(root,  text =hpVar)
	hpLabel.pack()
	length = str(ship.hull.length)
	beam = str(ship.hull.beam)

	textbox = ttk.Entry(root, textvariable=length)
	textbox.insert(0,string=length)
	textbox2 = ttk.Entry(root, textvariable=beam)
	textbox2.insert(0,string=beam)
	textbox2.config(state=tk.DISABLED)

	textbox.pack()
	textbox2.pack()

	def passData():
		ship.hull.length = Decimal(length)
		ship.hull.beam = Decimal(beam)
	controlCenter.sub_read(passData)
	def update():
		print('update here')
		length = str(ship.hull.length)
		beam = str(ship.hull.length/Decimal(9))
	controlCenter.sub_update(update)

