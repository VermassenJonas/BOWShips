import tkinter as tk
from tkinter import ttk

from logic.speedCalc import calcHPforSpeed  
from logic.shipData import ship

def draw(root):
	hpVar = tk.StringVar()
	hpVar = calcHPforSpeed()
	hpLabel = ttk.Label(root,  text =hpVar)
	hpLabel.pack()

	textbox = ttk.Entry(root, textvariable=ship.hull.length)
	textbox.insert(0,string=str(ship.hull.length))
	textbox2 = ttk.Entry(root, textvariable=ship.hull.length)

	textbox.pack()
	textbox2.pack()

