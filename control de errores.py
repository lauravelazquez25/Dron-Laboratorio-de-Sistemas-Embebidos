from machine import Pin, I2C

import time

try:
    from vl53l0x import VL53L0X

    # Inicializar el bus I2C
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    print("Escaneo I2C:", i2c.scan())

    # Crear el objeto del sensor
    tof = VL53L0X(i2c)

    # Iniciar el sensor
    tof.start()
    print("Sensor VL53L0X iniciado correctamente.")

    # Bucle de lectura
    while True:
        d = tof.read()
        print("Distancia:", d, "mm")
        time.sleep(0.5)

except Exception as e:
    print("⚠️ Error:", e)
