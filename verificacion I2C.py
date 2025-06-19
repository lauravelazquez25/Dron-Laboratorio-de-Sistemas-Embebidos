from machine import I2C, Pin

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
print("I2C encontrados:", i2c.scan())

#VL53L0X (sensor de distancia) -->41
#MPU -->104
