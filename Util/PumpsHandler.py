from . import ThreadHandler as TH
import time



class PumpsHandler:
	# Initializes 12 threads that will handle all 12 pumps
	def __init__(self):
		self.pump1 = self.createPumpThread(1, "Pump: 1", 23)
		self.pump2 = self.createPumpThread(2, "Pump: 2", 24)
		self.pump3 = self.createPumpThread(3, "Pump: 3", 13)
		self.pump4 = self.createPumpThread(4, "Pump: 4", 5)
		self.pump5 = self.createPumpThread(5, "Pump: 5", 25)
		self.pump6 = self.createPumpThread(6, "Pump: 6", 6)
		self.pump7 = self.createPumpThread(7, "Pump: 7", 10)
		self.pump8 = self.createPumpThread(8, "Pump: 8", 19)
		self.pump9 = self.createPumpThread(9, "Pump: 9", 11)
		self.pump10 = self.createPumpThread(10, "Pump: 10",17)
		self.pump11 = self.createPumpThread(11, "Pump: 11", 27)
		self.pump12 = self.createPumpThread(12, "Pump: 12", 9)
		self.startThread(1)
		self.startThread(2)
		self.startThread(3)
		self.startThread(4)
		self.startThread(5)
		self.startThread(6)
		self.startThread(7)
		self.startThread(8)
		self.startThread(9)
		self.startThread(10)
		self.startThread(11)
		self.startThread(12)
		
		

	def createPumpThread(self, pumpNum, pumpName, pinNum):
		return TH.myThread(pumpNum, pumpName, pinNum)

	# Starts thread requested
	def startThread(self, thread):
		if thread == 1:
			self.pump1.start()
		elif thread == 2:
			self.pump2.start()
		elif thread == 3:
			self.pump3.start()
		elif thread == 4:
			self.pump4.start()
		elif thread == 5:
			self.pump5.start()
		elif thread == 6:
			self.pump6.start()
		elif thread == 7:
			self.pump7.start()
		elif thread == 8:
			self.pump8.start()
		elif thread == 9:
			self.pump9.start()
		elif thread == 10:
			self.pump10.start()
		elif thread == 11:
			self.pump11.start()
		elif thread == 12:
			self.pump12.start()
		else:
			print("No Pump with that number found")

	# Joins the requested thread. May not need
	def stopThread(self, thread):
		if thread == 1:
			self.pump1.join()
		elif thread == 2:
			self.pump2.join()
		elif thread == 3:
			self.pump3.join()
		elif thread == 4:
			self.pump4.join()
		elif thread == 5:
			self.pump5.join()
		elif thread == 6:
			self.pump6.join()
		elif thread == 7:
			self.pump7.join()
		elif thread == 8:
			self.pump8.join()
		elif thread == 9:
			self.pump9.join()
		elif thread == 10:
			self.pump10.join()
		elif thread == 11:
			self.pump11.join()
		elif thread == 12:
			self.pump12.join()
		else:
			print("No Pump with that number found")

	# Sets the time for the pump to pour and executes
	# pour with coresponding thread
	def pour(self, pump, timer, ice):
		if ice == True:
			timer = self.convertToIceTime(timer)
		else:
			timer = self.convertToTime(timer)
		if pump == 1:
			self.pump1.setTime(timer)
			self.pump1.setAction('Mix')
		elif pump == 2:
			self.pump2.setTime(timer)
			self.pump2.setAction('Mix')
		elif pump == 3:
			self.pump3.setTime(timer)
			self.pump3.setAction('Mix')
		elif pump == 4:
			self.pump4.setTime(timer)
			self.pump4.setAction('Mix')
		elif pump == 5:
			self.pump5.setTime(timer)
			self.pump5.setAction('Mix')
		elif pump == 6:
			self.pump6.setTime(timer)
			self.pump6.setAction('Mix')
		elif pump == 7:
			self.pump7.setTime(timer)
			self.pump7.setAction('Mix')
		elif pump == 8:
			self.pump8.setTime(timer)
			self.pump8.setAction('Mix')
		elif pump == 9:
			self.pump9.setTime(timer)
			self.pump9.setAction('Mix')
		elif pump == 10:
			self.pump10.setTime(timer)
			self.pump10.setAction('Mix')
		elif pump == 11:
			self.pump11.setTime(timer)
			self.pump11.setAction('Mix')
		elif pump == 12:
			self.pump12.setTime(timer)
			self.pump12.setAction('Mix')
		else:
			print("No Pump with that number found")

	# Pours as long as button is being held down
	def holdPour(self, pump):
		# Will pour while button is held
		print("This will looop over a pour")

	def stopPour(self, pumpyBoi):
		# Will pour while button is held
		if pumpyBoi == 1:
			self.pump1.setAction('StopAll')
		elif pumpyBoi == 2:
			self.pump2.setAction('StopAll')
		elif pumpyBoi == 3:
			self.pump3.setAction('StopAll')
		elif pumpyBoi == 4:
			self.pump4.setAction('StopAll')
		elif pumpyBoi == 5:
			self.pump5.setAction('StopAll')
		elif pumpyBoi == 6:
			self.pump6.setAction('StopAll')
		elif pumpyBoi == 7:
			self.pump7.setAction('StopAll')
		elif pumpyBoi == 8:
			self.pump8.setAction('StopAll')
		elif pumpyBoi == 9:
			self.pump9.setAction('StopAll')
		elif pumpyBoi == 10:
			self.pump10.setAction('StopAll')
		elif pumpyBoi == 11:
			self.pump11.setAction('StopAll')
		elif pumpyBoi == 12:
			self.pump12.setAction('StopAll')
		
		print("This will stop the pour")
	def startPour(self, pumpyBoi):
		# Will pour while button is held
		if pumpyBoi == 1:
			self.pump1.setAction('Config')
		elif pumpyBoi == 2:
			self.pump2.setAction('Config')
		elif pumpyBoi == 3:
			self.pump3.setAction('Config')
		elif pumpyBoi == 4:
			self.pump4.setAction('Config')
		elif pumpyBoi == 5:
			self.pump5.setAction('Config')
		elif pumpyBoi == 6:
			self.pump6.setAction('Config')
		elif pumpyBoi == 7:
			self.pump7.setAction('Config')
		elif pumpyBoi == 8:
			self.pump8.setAction('Config')
		elif pumpyBoi == 9:
			self.pump9.setAction('Config')
		elif pumpyBoi == 10:
			self.pump10.setAction('Config')
		elif pumpyBoi == 11:
			self.pump11.setAction('Config')
		elif pumpyBoi == 12:
			self.pump12.setAction('Config')

		print("This will start the pour")

	def killAll(self):
		# Will pour while button is held
		self.pump1.setFlag()
		self.pump2.setFlag()
		self.pump3.setFlag()
		self.pump4.setFlag()
		self.pump5.setFlag()
		self.pump6.setFlag()
		self.pump7.setFlag()
		self.pump8.setFlag()
		self.pump9.setFlag()
		self.pump10.setFlag()
		self.pump11.setFlag()
		self.pump12.setFlag()
			
	def restartPour(self, pumpy, action):
		self.pump1.setFlag()
		self.pump1.setAction(action)
		self.pump1.run()

	# Converts given Oz to a time for the pump to be on
	# This math will be calculated through trials
	# 300 is the number of ML in a red solo cup
	def convertToTime(self, number):
		return(((number/80) * 300)/6.5)
	
	# Converts given Oz to a time for the pump to be on
	# This math will be calculated with the idea that someone
	# is a psyco path and will fill the entire cup with ice
	def convertToIceTime(self, number):
		return(((number/115) * 300)/6.5)

# testy = PumpsHandler()
# 
# testy.pour(2, testy.convertToTime(10))
##testy.pour(1, testy.convertToTime(2))
##testy.pour(4, testy.convertToTime(5))
#time.sleep(2)
# testy.stopPour()
# time.sleep(4)
# testy.startPour()
# testy.stopThread(2)
# print("test")
# testy.restartPour()



