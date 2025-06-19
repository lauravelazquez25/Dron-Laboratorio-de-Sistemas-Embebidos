from machine import UART
import time

# Inicializa UART1 con los pines disponibles (TX=5, RX=2)
uart_gps = UART(1, baudrate=9600, tx=5, rx=2)

print("Esperando tramas $GPRMC del GPS NEO-6M...")

# Convierte coordenadas NMEA a grados decimales
def convertir_coordenada(coord, direccion):
    try:
        if not coord or coord == '':
            return 0.0
        coord = float(coord)
        # Detectar si es longitud (más de 5 dígitos antes del punto) o latitud
        if len(str(int(coord))) > 4:
            # Longitud: 3 grados + minutos
            grados = int(coord / 100)
            minutos = coord - (grados * 100)
        else:
            # Latitud: 2 grados + minutos
            grados = int(coord / 100)
            minutos = coord - (grados * 100)
        decimal = grados + minutos / 60
        if direccion in ['S', 'W']:
            decimal = -decimal
        return round(decimal, 6)
    except Exception as e:
        return f"Error en coordenada: {e}"


# Convierte hora UTC a hora local de Argentina (UTC-3)
def parsear_hora_argentina(hora_raw):
    try:
        if not hora_raw or '.' not in hora_raw:
            return "sin señal UTC"
        hora_str = hora_raw.split('.')[0]
        if len(hora_str) < 6:
            hora_str = hora_str.zfill(6)
        hh = int(hora_str[0:2])
        mm = hora_str[2:4]
        ss = hora_str[4:6]
        hh_local = (hh - 3) % 24
        return f"{hh_local:02}:{mm}:{ss} (ARG)"
    except Exception as e:
        return f"Error en hora: {e}"


while True:
    try:
        if uart_gps.any():
            line = uart_gps.readline()
            if line and b'GPRMC' in line:
                datos = line.decode('utf-8').strip().split(',')
                print("Datos crudos:", datos)

                if len(datos) >= 8 and datos[2] == 'A':  # Estado A = datos válidos
                    hora_local = parsear_hora_argentina(datos[1])
                    lat = convertir_coordenada(datos[3], datos[4])
                    lon = convertir_coordenada(datos[5], datos[6])
                    velocidad_nudos = datos[7]

                    print("Hora local:", hora_local)
                    print("Latitud:", lat)
                    print("Longitud:", lon)
                    print("Velocidad (nudos):", velocidad_nudos)
                    print("-" * 40)

    except Exception as e:
        print("⚠️  Error:", e)
    
    time.sleep(0.1)
