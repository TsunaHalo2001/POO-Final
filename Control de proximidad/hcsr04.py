from machine import *
from time import *

class HCSR04:
    def __init__(self, trigger, echo):
        self.tpin = Pin(trigger, Pin.OUT)
        self.epin = Pin(echo, Pin.IN)
        
    def getCm(self):
        self.tpin.off()
        sleep_us(2)
        self.tpin.on()
        sleep_us(10)
        self.tpin.off()
        
        duration = time_pulse_us(self.epin, 1)
        cm = duration * 0.343 / 20
        
        if cm < 0:
            cm = 0
        if cm > 200:
            cm = 200
            
        return cm