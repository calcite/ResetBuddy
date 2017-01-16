# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:20:54 2016

@author: ALCZ11511047
"""

from mcp2210 import MCP2210
import time

class RBUDDY(object):
    def __init__(self):
        """inicialization of MCP2210 main chip which allow communication from system to display"""
        VID = 0x04D8
        PID = 0x00DE
        
        #self.communication = MCP2210(0x04D8, 0x00DE)
        try:
            self.communication = MCP2210(VID,PID)
        except Exception as e:
            print (e)
            raise Exception('Failed to open USB chanel')

        #gpio local variables
        self._gpio = self.communication.gpio
        self._gpio_direction = self.communication.gpio_direction
        
        """
        GPIO designations 	- 0x00 is GPIO, 0x01 is Chip selects, 0x02 is Dedicated function pin
        GPIO direction 		- 0x00 is Output, 0x01 is Input
        """
        #pins set as GPIO 
        self.communication.gpio_direction.pin_designations = [0] * 9
        #pins set as output           
        self.communication.gpio_direction = [0] * 9
        #clear pins
        self.communication.gpio = [0] * 9  
         
        
    def set_pin(self, pin, value):
        """Sets or clears GPIO"""
        self._gpio[pin-1] = value
        print ('pin ' + repr(pin) + ' set to ' + repr(value))
        
    def get_pin(self, pin):
        """returns value of a GPIO""" 
        value = self._gpio[pin-1]
        print ('pin ' + repr(pin) + ' is set to ' + repr(value))
        return self._gpio[pin-1]
        
    def reset_pin(self,pin,seconds):
        """sets and clears pin after selected time in seconds (reset)"""
        print ('reset pin ' + repr(pin) + ' for ' + repr(seconds) + ' second(s)')
        self._gpio[pin-1] = 1
        time.sleep(seconds)
        self._gpio[pin-1] = 0
        
    def reverse_reset_pin(self,pin,seconds):
        """ clears and sets pin after selected time in seconds (reverse reset)"""
        print ('reverse reset pin ' + repr(pin) + ' for ' + repr(seconds) + ' second(s)')
        self._gpio[pin-1] = 0
        time.sleep(seconds)
        self._gpio[pin-1] = 1    
          
    def clear_all(self):
        """clears all GPIOs"""
        for i in range (9):
            self._gpio[i] = 0
        print ('ALL CLEARED!') 
        
    def test(self):
        """all pin visual test"""
        for i in range (9):
            time.sleep(0.25)
            self._gpio[i] = 1
            time.sleep(0.25)
            self._gpio[i] = 0   
        print ('TEST COMPLETED')     
        
    def crazy(self):
        """all pin visual test"""
        for j in range (30):
            for i in range (9):
                time.sleep(0.002)
                self._gpio[i] = 1
                time.sleep(0.002)
                self._gpio[i] = 0 
        for j in range (10):
            for i in range (9):
                time.sleep(0.01)
                self._gpio[i] = 1
                time.sleep(0.01)
                self._gpio[i] = 0              
                
        print ('TEST COMPLETED')     
       

"""   USAGE EXAMPLE  
     
USER = RBUDDY()

USER.set_pin(3,1)
time.sleep(0.5)

USER.get_pin(2)
time.sleep(0.5)

USER.set_pin(2,1)
time.sleep(0.5)

USER.clear_all()
time.sleep(0.5)

USER.reset_pin(2,0.1)


"""

