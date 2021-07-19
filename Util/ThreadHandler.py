import threading
import time
import RPi.GPIO as GPIO



exitFlag = 0

class myThread (threading.Thread):
	def __init__(self, threadID, name, pinNum):
		GPIO.setmode(GPIO.BCM)
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = 10
		self.time = 0
		self.action = 'Idle'
		self.Flag = True
		self.HasRunOnce = False
		self.Pin = pinNum
		
		
	def run(self):
		GPIO.setup(self.Pin, GPIO.IN)
		while (self.Flag):
			if self.action == 'Mix':
				print ("Starting " + self.name)
				# Start Pour
				GPIO.setup(self.Pin, GPIO.OUT, initial=False)
				self.pour(self.name, self.time)
				print ("Exiting " + self.name)
				self.action = 'StopAll'
			elif self.action == 'Idle':
				time.sleep(0.5)
				
			elif self.action == 'Config':
				#GPIO.output(self.Pin, GPIO.LOW)
				GPIO.setup(self.Pin, GPIO.OUT, initial=False)
				GPIO.output(self.Pin, True)
				
			elif self.action == 'StopAll':
				GPIO.output(self.Pin, False)
				GPIO.setup(self.Pin, GPIO.IN)
				#GPIO.cleanup()
				self.action = 'Idle'
			
	def setAction(self, ToDo):
		#exitFlag = 1
		self.action = ToDo
	def setTime(self, time):
		self.time = time
	def setFlag(self):
		self.Flag = False
	def getFlag(self):
		return self.Flag
	
	def getHasRun(self):
		return self.HasRunOnce
	
	def setHasRun(self, args):
		self.HasRunOnce = args
		
	def pour(self, threadName, timer):
		# Open Valve
		if (timer == -1):
			print("Wait till hold button triggers")
		else: 
			GPIO.output(self.Pin, True)
			time.sleep(timer)
		# Close Valve
		print(threadName, " has completed pour")

def print_time(threadName, delay, counter):
	while counter:
		print(exitFlag)
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print ("%s: %s" % (threadName, time.ctime(time.time())))
		counter -= 1


# Maybe use this 
# def pour(self, threadName, timer):
# 	# Open Valve
# 	if (timer == -1):
# 		print("Wait till hold button triggers")
# 	else: 
# 		GPIO.output(self.Pin, True)
# 		time.sleep(timer)
# 		GPIO.output(self.Pin, False)
# 	# Close Valve
# 	print(threadName, " has completed pour")



