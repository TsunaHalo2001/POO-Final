from hcsr04 import *
import bluetooth
from BLE import *

#Pines
trigPin = 16
echoPin = 17

#Init bluetooth
name = 'ESP32 Tsuna'
ble = bluetooth.BLE()
uart = BLEUART(ble, name)
rx_buffer = ""
bandera_rx = 0

#HCSR04
d1 = HCSR04(trigPin, echoPin)

def on_rx():
    global rx_buffer, bandera_rx
    rx_buffer = uart.read().decode().strip()
    bandera_rx = 1
    
#Bluetooth event
uart.irq(handler = on_rx)

def run():
    while True:
        distancia = int(d1.getCm())
        uart.write(str(distancia))
        sleep_ms(100)

if __name__ == "__main__":
    run()