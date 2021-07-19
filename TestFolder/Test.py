import threading
import time
import RPi.GPIO as GPIO



exitFlag = 0

class myThread (threading.Thread):
	def __init__(self):
		self.e = threading.Event()
		self.t = threading.Thread(name='your_mum', 
                     target=self.wait_for_event,
                     args=(self.e,))
		self.t.start()
		
	def wait_for_event(self, e):
		while True:
			print( '\tTHREAD: This is the thread speaking, we are Waiting for event to start..')
			event_is_set = e.wait()
			print ('\tTHREAD:  WHOOOOOO HOOOO WE GOT A SIGNAL  : %s', event_is_set)
			e.clear()
			
	def setEvent(self):
		self.e.set()


testyBoi = myThread()
testyBoi1 = myThread()
testyBoi2 = myThread()
testyBoi3 = myThread()
testyBoi4 = myThread()
testyBoi5 = myThread()
testyBoi6 = myThread()
testyBoi7 = myThread()
testyBoi8 = myThread()
testyBoi9 = myThread()
testyBoi10 = myThread()
testyBoi11 = myThread()
while True:
	print ('MAIN LOOP: still in the main loop..')
	time.sleep(4)
	print ('MAIN LOOP: I just set the flag..')
	testyBoi.setEvent()
	print ('MAIN LOOP: now Im gonna do some processing n shi-t')
	time.sleep(4)
	print ('MAIN LOOP:  .. some more procesing im doing   yeahhhh')
	time.sleep(4)
	print ('MAIN LOOP: ok ready, soon we will repeat the loop..')
	time.sleep(2)
    