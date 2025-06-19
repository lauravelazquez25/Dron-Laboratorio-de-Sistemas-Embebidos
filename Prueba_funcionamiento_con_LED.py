from machine import Pin
import time

# Configurar el LED interno (en GPIO2) como salida
led = Pin(2, Pin.OUT)

# Bucle infinito para parpadear
while True:
    led.value(1)  # LED encendido
    time.sleep(0.5)  # Espera 0.5 segundos
    led.value(0)  # LED apagado
    time.sleep(0.5)  # Espera 0.5 segundos
