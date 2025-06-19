import network

ssid = 'Personal-437'
password = '3795016500'

def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a la red WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Conectado! IP:', wlan.ifconfig()[0])
    return wlan.ifconfig()[0]

if __name__ == '__main__':
    conectar_wifi()

