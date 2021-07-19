from tkinter import *
from Util import DrinkList as DL
from Util import FormatHandler as FH
from Util import PumpsHandler as PH
import time
import os

# Handler to create a Drink List object
def createDrinks(File):
	Drinks = DL.DrinkList(File)
	return Drinks

class MainMenu:
	# Define settings upon initialization. Here you can specify
	def __init__(self, Frame, Window, File):
		self.master = Window
		self.canvas = Frame
		self.file = File
		self.format = FH.FormatHandler()
		self.drinkList = DL.DrinkList(self.file)
		self.pixel = PhotoImage(width=1, height=1)
		self.drinkPumps = PH.PumpsHandler()
		self.startUp()

	# This will be the menu for config settings
	def configMenu(self):
		self.format.clearCanvas(self.canvas)
		configPumpsButton = Button(self.canvas, text="Config Pumps", command=self.configPumps)
		self.format.formatButton(self.canvas, 1, configPumpsButton)
		self.format.resizeCanvas(self.canvas)

	# Menu showing all pumps and their active Mixer
	# Here you will be able to hold down the pump button
	# to pour, when you release pouring will stop
	def configPumps(self):
		self.format.clearCanvas(self.canvas)
		listOfMixers = self.drinkList.getActiveMixersNameList()
		mixerMenuButton = []
		# Iterate through all drinks and create a 
		# button linking it to the ingredients for 
		# said drink
		iter = 1
		for i in range(12):
			mixerName = "Pump " + str(iter) + ":\n" + self.format.shortenWords(str(listOfMixers[i]))
			button = Button(self.canvas, text=mixerName)
			button.bind('<ButtonPress-1>',lambda event, num=iter: self.start_test(num))
			button.bind('<ButtonRelease-1>',lambda event, num=iter: self.stop_test(num))
			mixerMenuButton.append(button)
			self.format.formatButton(self.canvas, iter, mixerMenuButton[i])
			iter += 1
		self.format.resizeCanvas(self.canvas)


	# This is the menu for all of the drink options
	def drinksMenu(self):
		self.format.clearCanvas(self.canvas)
		#Drinks = DL.DrinkList(self.file)
		listOfDrinks = self.drinkList.printDrinkList()
		drinkMenuButton = []
		# Iterate through all drinks and create a 
		# button linking it to the ingredients for 
		# said drink
		iter = 1
		for i in range(self.drinkList.getNumDrinks()):
			
			canMakeDrink = False
			drinkName = listOfDrinks[i]
			# Iterate through ingredients and print each one
			for j in self.drinkList.getIngredients(drinkName):
				if self.drinkList.checkIfIngredientIsAvailable(j) == False:
					canMakeDrink = False
					iter -= 1
					break
				else:
					canMakeDrink = True
			if canMakeDrink and iter >= 1:
				drinkMenuButton.append(Button(self.canvas, text=self.format.shortenWords(drinkName), command=lambda name=drinkName:self.drinksIngred(name, self.drinkList)))
				self.format.formatButton(self.canvas, iter, drinkMenuButton[iter-1])
			iter += 1
		self.format.resizeCanvas(self.canvas)

	# This will print out the ingredients adn button for the drink selected
	def drinksIngred(self, drink, Drinks):
		self.format.clearCanvas(self.canvas)
		numIngred = len(Drinks.getIngredients(drink))
		# Add the Mix Drink button 
		makeDrinkButton = Button(self.canvas, text="Mix Drink", command=lambda name=drink:self.iceMenu(drink), relief=RAISED, font=("Comic Sans MS", 20))	
		self.format.formatButton(self.canvas, 1, makeDrinkButton)
		iter = 0
		Ingredients = []
		# Iterate through ingredients and print each one
		for i in Drinks.getIngredients(drink):
			Ingredients.append(str(i))
		self.format.formatIngredList(self.canvas, drink, Ingredients)
		iter += 1
		self.format.resizeCanvas(self.canvas)

	def iceMenu(self, drink):
		self.format.clearCanvas(self.canvas)
		ice = Button(self.canvas, text="Ice", command=lambda name=drink:self.mixDrink(drink, True), relief=RAISED, font=("Comic Sans MS", 20))	
		self.format.formatButton(self.canvas, 1, ice)
		noIce = Button(self.canvas, text="No Ice", command=lambda name=drink:self.mixDrink(drink, False), relief=RAISED, font=("Comic Sans MS", 20))	
		self.format.formatButton(self.canvas, 2, noIce)
	# Menu that will show while your drink is being made
	# Emergency Stop button and some facts will be on this page
	def mixDrink(self, drink, ice):
		self.format.clearCanvas(self.canvas)
		STOP = 'STOP FOR THE LOVE OF GOD'
		emergencyStop = Button(self.canvas, bg='red', text="Emergency\n Stop", command=lambda name=STOP:self.emergencyStop(), relief=RAISED, font=("Comic Sans MS", 20))	
		self.format.formatButton(self.canvas, 1, emergencyStop)
		dir = os.path.dirname(__file__)
		filename = os.path.join(dir, '../Images/MoneyForMe.gif')
		img = PhotoImage(file=filename)      
		self.format.formatIngredList(self.canvas, 'Please Tip Me.\nI Worked Hard\nOn This', '')
		self.canvas.create_image(560,5, anchor=NE, image=img) 

		pumps = []
		amounts = []
		for i in self.drinkList.getDrinkPumps(drink):
			pumps.append(i)
			# Test pumps
			# self.drinkPumps.checkIfPumpIsConnected(pumps[i])
		pumpNum = 0
		for i  in self.drinkList.getIngredientAmounts(drink):
			self.drinkPumps.pour(pumps[pumpNum], i, ice)
			# Create a new thread for each pump
			# In thread turn on the pump and then sleep for desired time
			# Turn off pump and then rejoin
			# root.after(POLLING_DELAY, check_status)
			# def check_status():
			#	with lock:
			#		if not finished:
			#			root.after(POLLING_DELAY, check_status)  # Keep polling.
			#		else:
			#			print('end')

			amounts.append(i)
			pumpNum += 1
			print(i)

	
		# Turn on both pumps
		temp = self.drinkList.getIngredientAmounts(drink)
		print(temp)
		self.format.resizeCanvas(self.canvas)
		# TODO: Time will be dictated if pumps are on or off
		var = IntVar()
		self.master.after(45000, var.set, 1)
		self.master.wait_variable(var)
		self.initMainMenu()

	# Shit hit the fan and if you are here everything went south
	# Nicholas Tolentino is not responsible for the reason why you
	# have unfortunatly ended up in this situation
	def emergencyStop(self):
		print("Stopping all pumps")
		# End all threads

	# Default Main Menu
	def initMainMenu(self):
		self.format.clearCanvas(self.canvas)
		configButton = Button(self.canvas, text="MANUAL", command=self.configMenu)
		self.format.formatButton(self.canvas, 1, configButton)
		drinkMenuButton = Button(self.canvas, text="DRINKS", command=self.drinksMenu)
		self.format.formatButton(self.canvas, 2, drinkMenuButton)
		self.format.resizeCanvas(self.canvas)

	# Copyright and Menu page
	def startUp(self):
		self.format.clearCanvas(self.canvas)
		data = []
		dirname = os.path.dirname(__file__)
		filename = os.path.join(dir, '../README.txt')
		with open (filename, 'r') as myfile:
			data=myfile.readlines()

		longListy = ""
		for ele in data:
			longListy += (ele)
		introMsg = Label(self.canvas, text=longListy, anchor=CENTER, font=("Comic Sans MS", 11))
		self.canvas.create_window(10, 10, anchor=NW, window=introMsg)
		self.canvas.config(scrollregion=(0,0,800,1500))
		var = IntVar()
		
		# For Debug Use
		self.master.after(1000, var.set, 1)
		
		#self.master.after(15500, var.set, 1)
		self.master.wait_variable(var)
		self.initMainMenu()
	
	def start_test(self, pump):
		self.drinkPumps.startPour(pump)
		
	def stop_test(self, pump):
		self.drinkPumps.stopPour(pump)
		
	def destroyAll(self):
		self.drinkPumps.killAll()
		quit()
		

