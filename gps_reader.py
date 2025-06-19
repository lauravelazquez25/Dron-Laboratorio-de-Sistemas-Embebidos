from machine import UART
import time
import _thread

class GPSData:
    def __init__(self):
        self.hora = "Esperando señal"
        self.lat = "-"
        self.lon = "-"
        self.velocidad = "-"
        self.lock = False
        self.uart = UART(1, baudrate=9600, tx=5, rx=2)
        _thread.start_new_thread(self.leer_datos, ())

    def convertir_coordenada(self, coord, direccion):
        try:
            if not coord or coord == '':
                return 0.0
            coord = float(coord)
            grados = int(coord / 100)
            minutos = coord - (grados * 100)
            decimal = grados + minutos / 60
            if direccion in ['S', 'W']:
                decimal = -decimal
            return round(decimal, 6)
        except:
            return "?"

    def parsear_hora_argentina(self, hora_raw):
        try:
            if not hora_raw or '.' not in hora_raw:
                return "sin señal UTC"
            hora_str = hora_raw.split('.')[0].zfill(6)
            hh = int(hora_str[0:2])
            mm = hora_str[2:4]
            ss = hora_str[4:6]
            hh_local = (hh - 3) % 24
            return f"{hh_local:02}:{mm}:{ss} (ARG)"
        except:
            return "?"

    def leer_datos(self):
        while True:
            try:
                if self.uart.any():
                    line = self.uart.readline()
                    if line and b'GPRMC' in line:
                        datos = line.decode('utf-8').strip().split(',')
                        if len(datos) >= 8 and datos[2] == 'A':
                            self.hora = self.parsear_hora_argentina(datos[1])
                            self.lat = self.convertir_coordenada(datos[3], datos[4])
                            self.lon = self.convertir_coordenada(datos[5], datos[6])
                            self.velocidad = datos[7]
            except:
                pass
            time.sleep(0.1)

    def obtener_datos(self):
        return {
            "hora": self.hora,
            "lat": self.lat,
            "lon": self.lon,
            "velocidad": self.velocidad
        }

gps = GPSData()
