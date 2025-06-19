import machine         # Para I2C
import time            # Para delays
from MPU6050 import MPU6050  # Asegurate de haber guardado como 'MPU6050.py'

# Inicializar I2C en GPIO22 (SCL) y GPIO21 (SDA)
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))

# Crear objeto del sensor
mpu = MPU6050(i2c)

# Bucle de lectura
print("Iniciando lectura del MPU6050...")

while True:
    accel = mpu.read_accel_data()     # Devuelve un diccionario con 'x', 'y', 'z'
    gyro = mpu.read_gyro_data()       # También devuelve 'x', 'y', 'z'
    temp = mpu.read_temperature()     # Temperatura en °C

    # Mostrar los valores en consola
    print("Acelerómetro:", accel)
    print("Giroscopio:", gyro)
    print("Temperatura:", temp)

    time.sleep(1)
