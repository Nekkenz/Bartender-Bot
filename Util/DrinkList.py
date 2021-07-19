import json

################################################
# Import json files containing drinks in pumps #
################################################

pumpsJSON = "Drinks/Pumps.json"

#################################################

# Loads the JSON file with the Drinks and 
# their respective ingredients and amounts
def loadJSON(File):
	with open(File) as f:
		data = json.load(f)[0]
	return data

class DrinkList:
	# Initialize the Drink list
	def __init__(self, FilePath):
		self.Data = loadJSON(FilePath)
		self.pumps = loadJSON(pumpsJSON)

	# Returns a list of the names of the Drinks given in
	# the json file provided
	def printDrinkList(self):
		DrinkLists = []
		for i in self.Data['Drinks']:
			temp = str(i['Name'])
			DrinkLists.append(temp)
		
		DrinkLists.sort(key = lambda x: x[0])
		return DrinkLists
		# Debuging
		#print(DrinkLists)

	# Returns a Dictionary of the ingredients in the drink
	# requested, Must be located in the JSON file
	def getIngredients(self, drinkName):
		ingreds = ''
		for i in self.Data['Drinks']:
			if str(i['Name']) == drinkName:
				for j in i['Ingredients']:
					ingreds = j
				break
		return ingreds

		# For debugging if you don't know what you are doing
		#for i in ingreds:
		#	print(ingreds[i])
	
	# returns a list of touples containing the ingredients
	# and their respective amount
	def getIngredientAmounts(self, drinkName):
		amountsList = []
		amounts = []
		ingreds = self.getIngredients(drinkName)
		for i in self.Data['Drinks']:
			if str(i['Name']) == drinkName:
				for j in i['Ingredients']:
					amountsList.append(j)
				break
		for i in ingreds:
			amounts.append(amountsList[0][i])
		return amounts

	# Checks to make sure all the ingredients in the drink
	# are in pumps if not return false
	def checkIfIngredientIsAvailable(self, Ingred):
		for i in self.pumps['Pumps']:
			if Ingred == str(i['Name']):
				if i['Pump'] >= 0:
					return True
				else:
					return False
		return False
	
	# Return a list of all Mixers that are available
	def getActiveMixersNameList(self):
		mixers = []
		names = []
		for i in self.pumps['Pumps']:
			if i['Pump'] >= 0:
				temp = (str(i['Name']), int(i['Pump']))
				mixers.append(temp)
				
		
		mixers.sort(key = lambda x: x[1])
		for i in mixers:
			names.append(i[0])

		return names

	# Return the pump numbers for all of the drinks
	def getDrinkPumps(self, drink):
		ingreds = self.getIngredients(drink)

		pumpNums = []
		pumps = self.pumps['Pumps']
		for i in ingreds:
			for j in pumps:
				if j['Name'] == i:
					pumpNums.append(j['Pump'])
			
		return pumpNums

	# Returns the total number of drinks 
	def getNumDrinks(self):
		numDrinks = 0
		for i in self.Data['Drinks']:
			numDrinks += 1
		return numDrinks

		


