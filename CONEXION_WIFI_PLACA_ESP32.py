import network
import time

# Configurar la interfaz WiFi en modo STATION (cliente)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Datos de tu red WiFi
ssid = 'Personal-437'
password = '3795016500'

# Conectarse
print("Conectando a la red WiFi...")
wlan.connect(ssid, password)

# Esperar a que se conecte
max_retries = 10
retry = 0
while not wlan.isconnected() and retry < max_retries:
    print(".", end="")
    time.sleep(1)
    retry += 1

# Resultado
if wlan.isconnected():
    print("\n¡Conectado!")
    print("Configuración de red (IP, Gateway, etc):", wlan.ifconfig())
else:
    print("\nNo se pudo conectar a la red WiFi.")
