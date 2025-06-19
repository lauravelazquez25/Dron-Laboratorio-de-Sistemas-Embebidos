from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
addr = 0x29

# Verifica si el sensor responde a lectura de registros
def leer_registro(reg):
    try:
        val = i2c.readfrom_mem(addr, reg, 1)[0]
        print(f"Registro 0x{reg:02X} = {val}")
    except Exception as e:
        print(f"Error leyendo 0x{reg:02X}:", e)

print("🧪 Diagnóstico VL53L0X")
print("Sensores detectados:", i2c.scan())

# Registros clave para probar
registros = [0xC0, 0xC1, 0xC2, 0x51, 0x52, 0x89, 0x91, 0xA8]

for r in registros:
    leer_registro(r)
