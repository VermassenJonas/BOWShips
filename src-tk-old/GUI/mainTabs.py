import tkinter as tk
from tkinter import ttk

import translations.strings as strings

import GUI.HullGUI as hullGUI
import GUI.engineGUI as engineGUI


def draw(base, root):
	
	mainTabs = ttk.Notebook(base, width=450) 
	
	hullTab = ttk.Frame(mainTabs) 
	FreeboardTab = ttk.Frame(mainTabs)
	EngineTab = ttk.Frame(mainTabs)
	
	mainTabs.add(hullTab, 		text =strings.hull) 
	mainTabs.add(FreeboardTab, 	text =strings.freeboard) 
	mainTabs.add(EngineTab, 	text =strings.engine) 

	base.add(mainTabs)
	
	hullGUI.draw(hullTab)
	engineGUI.draw(EngineTab)

	