#!/usr/bin/env python3
import os
print(os.getcwd())
print("its working")
# Vehicle  = parent or superclass. create child classes, aka subclasses for different types of VEHICLES
class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number 

    def go(self):
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        return "filling up!"
    
    #instances of VEHICLE initialize with a wheel size and number. go and fill tank are instance methods of common behavior
    

