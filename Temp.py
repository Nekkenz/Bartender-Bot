import json
import RPi.GPIO as GPIO
import time
import threading


from drinks import drink_list

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

FLOW_RATE = 1

class Bartender:

    def __init__(self):
        self.pump_configuration = Bartender.read_pump_config()
        for pump in self.pump_configuration.keys():
            GPIO.setup(self.pump_configuration[pump]["pin"], GPIO.OUT, initial=GPIO.HIGH)
    


    @staticmethod
    def read_pump_config():
        return json.load(open("pump_config.json"))

    @staticmethod
    def write_pump_config(configuration):
        with open("pump_config.json", "w") as jsonFile:
            json.dump(configuration, jsonFile, indent=4)

    def config_pump(self, pump_name, pump_value):
        for pump in self.pump_configuration:
            pump = self.pump_configuration[pump]
            if pump["name"] == pump_name:
                pump["value"] = pump_value
                Bartender.write_pump_config(self.pump_configuration)
                return
        print("No pump with that name found...")


    def get_pumps(self):
        """
        Get the name and value of all the pumps in the system
        :return: List of pump-value tuples
        """
        pumps = []
        for pump in self.pump_configuration:
            pumps.append((self.pump_configuration[pump]["name"], self.pump_configuration[pump]["value"]))
        return pumps

    def pour(self,pin,wait_time=10):
        GPIO.output(pin, GPIO.LOW)
        time.sleep(wait_time)
        GPIO.output(pin, GPIO.HIGH)


    def make_drink(self,user_drink):
        # first find the drink the user wants to make
        drink = None
        for d in drink_list:
            if d["name"] == user_drink:
                drink = d
                break
        if drink is None:
                raise Exception("No Drink")


        drink_name = drink["name"]
        ingredients = drink["ingredients"]

        
        #Jock the Jockies
        pump_threads = []
        for ing in ingredients:
            for pump in self.pump_configuration:
                if ing == self.pump_configuration[pump]["value"]:
                    pump_time = ingredients[ing] * FLOW_RATE
                    pump_t = threading.Thread(target=self.pour,args=(self.pump_configuration[pump]["pin"],pump_time))
                    pump_threads.append(pump_t)

        #run the pumps

        for thread in pump_threads:
            thread.start()
        for thread in pump_threads: #stops the progress untill all pumps have pumped
            thread.join()
    


