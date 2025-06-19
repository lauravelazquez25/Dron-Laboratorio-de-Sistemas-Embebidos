from machine import Pin, I2C
from vl53l0x import VL53L0X
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
tof = VL53L0X(i2c)
tof.start()

while True:
    distancia = tof.read()
    print("Distancia:", distancia, "mm")
    time.sleep(0.5)
