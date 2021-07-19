from tkinter import *

class FormatHandler:
	# Initializes a canvas with the default Height and Width 
	def __init__(self):
		self.pixel = PhotoImage(width=1, height=1)
		self.frameHeight= 480
		self.frameWidth = 760
		self.buttonHeight = 210
		self.buttonWidth = 150
		self.itemBuffer = 5
		self.currentRow = 0
		self.currentColumn = 0

	def getHeight(self):
		return(self.height)

	# Clear the canvas to prep for new screen
	def clearCanvas(self, frame):
		self.currentRow = 0
		self.currentColumn = 0
		frame.delete("all")

	# Formats the button in a grid formation with 5 across starting
	# from the top left
	def formatButton(self, frame, buttonNumber, button):
		column = self.itemBuffer + self.currentColumn*self.buttonWidth
		row = self.itemBuffer + self.currentRow*self.buttonHeight
		button.configure(image=self.pixel, compound="c", height=self.buttonHeight-15, width=self.buttonWidth-30, relief=RAISED, font=("Comic Sans MS", 15))
		frame.create_window(column, row, anchor=NW, window=button)
		self.currentColumn += 1
		if(buttonNumber%5 == 0):
			self.currentRow += 1
			self.currentColumn = 0
	
	# Formats the ingrients in a list in descending order
	def formatIngredList(self, frame, drink, list):
		listyBoi = str(drink) + ":\n"
		column = self.itemBuffer + self.currentColumn*self.buttonWidth
		row = self.itemBuffer + self.currentRow*self.buttonHeight
		for ele in list:
			listyBoi += ("-" + ele + "\n")
		listOfIngreds = Label(frame, text=listyBoi, anchor=CENTER, font=("Comic Sans MS", 15))
		frame.create_window(column, row, anchor=NW, window=listOfIngreds)

	# Resizes the Canvas so there is enough scroll 
	# region for large pages and visa versa
	def resizeCanvas(self, frame):
		row = (self.itemBuffer + (self.currentRow+1)*self.buttonHeight)
		frame.config(scrollregion=(0,0,800,row))

	# For long words appends them that way they are on 2 separate lines
	def shortenWords(self, word):
		temp = word.replace(" ","\n")
		return temp
		



		
