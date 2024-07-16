import tkinter as tk
from tkinter import ttk

import translations.strings as strings

import GUI.shipOverviewGUI as shipOverviewGUI

def draw(base, root):
	
	sideTabs = ttk.Notebook(base, width=450) 
	
	shipOverviewTab = ttk.Frame(sideTabs) 
	reportTab = ttk.Frame(sideTabs) 
	
	sideTabs.add(shipOverviewTab, 	text =strings.ship_overview) 
	sideTabs.add(reportTab, 		text =strings.report) 
	base.add(sideTabs)
	
	shipOverviewGUI.draw(shipOverviewTab)