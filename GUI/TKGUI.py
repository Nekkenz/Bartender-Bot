from . import Navibar as Nav
from . import MainMenu as MM
from tkinter import *


def createApp():
	window = Tk()
	app=TKgui(window)

class TKgui:
	# Initialize the Window for the Application
	# with default fullscreen
	def __init__(self, master):
		self.window = master
		self.frame=Frame(self.window)
		self.frame.pack(expand=True, fill=BOTH)
		self.canvas=Canvas(self.frame,bg='#34eb67',width=800,height=480,scrollregion=(0,0,800,5000))
		self.vbar=Scrollbar(self.frame,orient=VERTICAL)
		self.vbar.pack(side=RIGHT,fill=Y)
		self.vbar.config(command=self.canvas.yview)
		self.canvas.config(width=800,height=480)
		self.canvas.config(yscrollcommand=self.vbar.set)
		self.canvas.pack(side=LEFT,expand=True,fill=BOTH)
		self.window.attributes("-fullscreen", True)

		## Set up menu bar and main menu
		self.mainFrame = MM.MainMenu(self.canvas, self.window)
		Nav.Navbar(self.window, self.mainFrame)

		## Bind keys to functionality
		self.canvas.bind("<ButtonPress-1>", self.scroll_start)
		self.canvas.bind("<B1-Motion>", self.scroll_move)
		## Window main loop
		self.window.mainloop()

	########################################################
	# Below will be definitions for interupts aka keyboard #
	# inputs that will act as shortcuts					   #
	########################################################

	# Click and drag for scrolling
	def scroll_start(self, event):
		self.canvas.scan_mark(event.x, event.y)

	def scroll_move(self, event):
		self.canvas.scan_dragto(event.x, event.y, gain=1)

	# Toggle Fullscreen 
	def toggleFullScreen(self, event):
		self.fullScreenState = not self.fullScreenState
		self.window.attributes("-fullscreen", self.fullScreenState)

	# Quit Fullscreen
	def quitFullScreen(self, event):
		self.fullScreenState = False
		self.window.attributes("-fullscreen", self.fullScreenState)





