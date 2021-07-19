from tkinter import *
class Navbar:
	# Define settings upon initialization. Here you can specify
	def __init__(self, Window, MainFrame):
		self.master = Window
		self.mainFrame = MainFrame
		self.initNavBar()

	def donothing(self):
		button = Button(self.master, text="Do nothing button")
		button.pack()

	# Menu Bar settings
	# TODO: Add funtionality or remove extra settings
	def initNavBar(self):
		menubar = Menu(self.master)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Home", command=self.mainFrame.initMainMenu)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=lambda name='quitAll':self.mainFrame.destroyAll())
		menubar.add_cascade(label="Menu", menu=filemenu)
		self.master.config(menu=menubar)