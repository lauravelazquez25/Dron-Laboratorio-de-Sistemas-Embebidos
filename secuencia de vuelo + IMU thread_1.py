import machine          # Módulo para acceder a GPIOs, I2C, PWM
import time             # Módulo para manejar retardos
import _thread          # Módulo para ejecutar hilos concurrentes en MicroPython
from MPU6050 import MPU6050  # Clase para manejar el sensor MPU6050

# ---------- Inicialización del sensor MPU6050 ----------
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))  # Configura I2C con SCL en GPIO22 y SDA en GPIO21
mpu = MPU6050(i2c)  # Crea el objeto MPU6050 usando ese bus I2C

# ---------- Hilo concurrente que imprime los datos del sensor ----------
def hilo_sensor():
    while True:  # Bucle infinito
        accel = mpu.read_accel_data()         # Lee datos del acelerómetro (x, y, z)
        gyro = mpu.read_gyro_data()           # Lee datos del giroscopio (x, y, z)
        temp = mpu.read_temperature()         # Lee temperatura interna del sensor

        print("📡 Acelerómetro:", accel)      # Imprime el vector de aceleración
        print("🎯 Giroscopio:", gyro)          # Imprime el vector de rotación
        print("🌡️ Temp:", temp)               # Imprime la temperatura en grados Celsius
        print("-----------------------------")  # Separador visual

        time.sleep(0.5)  # Espera medio segundo entre lecturas

# ---------- Pines de motores ----------
# Motor 1
AIN1_M1 = machine.Pin(14, machine.Pin.OUT)  # Dirección IN1 del Motor 1
AIN2_M1 = machine.Pin(27, machine.Pin.OUT)  # Dirección IN2 del Motor 1
PWM_M1 = machine.PWM(machine.Pin(26), freq=1000)  # PWM del Motor 1 por GPIO26

# Motor 2
BIN1_M2 = machine.Pin(25, machine.Pin.OUT)  # Dirección IN1 del Motor 2
BIN2_M2 = machine.Pin(33, machine.Pin.OUT)  # Dirección IN2 del Motor 2
PWM_M2 = machine.PWM(machine.Pin(32), freq=1000)  # PWM del Motor 2

# Motor 3
BIN1_M3 = machine.Pin(18, machine.Pin.OUT)  # Dirección IN1 del Motor 3
BIN2_M3 = machine.Pin(19, machine.Pin.OUT)  # Dirección IN2 del Motor 3
PWM_M3 = machine.PWM(machine.Pin(15), freq=1000)  # PWM del Motor 3

# Motor 4
AIN1_M4 = machine.Pin(4, machine.Pin.OUT)   # Dirección IN1 del Motor 4
AIN2_M4 = machine.Pin(16, machine.Pin.OUT)  # Dirección IN2 del Motor 4
PWM_M4 = machine.PWM(machine.Pin(17), freq=1000)  # PWM del Motor 4

# ---------- Velocidad base para los motores ----------
BASE_SPEED = 600  # Velocidad media (duty cycle entre 0 y 1023)

# ---------- Función para encender un motor en un sentido ----------
def encender_motor(pin1, pin2, pwm, velocidad=BASE_SPEED):
    pin1.on()            # Activa IN1 (dirección adelante)
    pin2.off()           # Desactiva IN2
    pwm.duty(velocidad)  # Aplica PWM con la velocidad deseada

# ---------- Función para detener un motor ----------
def detener_motor(pin1, pin2, pwm):
    pin1.off()           # Apaga IN1
    pin2.off()           # Apaga IN2
    pwm.duty(0)          # PWM en 0

# ---------- Función para detener todos los motores ----------
def detener_todos():
    detener_motor(AIN1_M1, AIN2_M1, PWM_M1)
    detener_motor(BIN1_M2, BIN2_M2, PWM_M2)
    detener_motor(BIN1_M3, BIN2_M3, PWM_M3)
    detener_motor(AIN1_M4, AIN2_M4, PWM_M4)

# ---------- Secuencia automatizada de vuelo ----------
def secuencia_de_vuelo():
    print("Esperando despegue... (levantar dron manualmente)")
    while True:
        accel = mpu.read_accel_data()   # Lee los datos del acelerómetro
        if accel['z'] > 11:             # Si el eje Z supera 11 (despegue detectado)
            print("¡Despegue detectado!")
            break
        time.sleep(0.1)  # Espera corta antes de volver a leer

    # --- Etapa 1: Despegue vertical ---
    print("Motores encendidos: despegue")
    encender_motor(AIN1_M1, AIN2_M1, PWM_M1)
    encender_motor(BIN1_M2, BIN2_M2, PWM_M2)
    encender_motor(BIN1_M3, BIN2_M3, PWM_M3)
    encender_motor(AIN1_M4, AIN2_M4, PWM_M4)
    time.sleep(2)

    # --- Etapa 2: Avanzar hacia adelante ---
    print("Avance hacia adelante")
    encender_motor(BIN1_M3, BIN2_M3, PWM_M3, BASE_SPEED + 100)  # M3 más rápido
    encender_motor(AIN1_M4, AIN2_M4, PWM_M4, BASE_SPEED + 100)  # M4 más rápido
    time.sleep(2)

    # --- Etapa 3: Girar hacia la derecha ---
    print("Giro a la derecha")
    encender_motor(AIN1_M1, AIN2_M1, PWM_M1, BASE_SPEED + 150)  # M1 más rápido
    encender_motor(BIN1_M3, BIN2_M3, PWM_M3, BASE_SPEED + 150)  # M3 más rápido
    encender_motor(BIN1_M2, BIN2_M2, PWM_M2, BASE_SPEED - 100)  # M2 más lento
    encender_motor(AIN1_M4, AIN2_M4, PWM_M4, BASE_SPEED - 100)  # M4 más lento
    time.sleep(2)

    # --- Etapa 4: Volver al punto de partida ---
    print("Regreso al punto de partida")
    encender_motor(AIN1_M1, AIN2_M1, PWM_M1, BASE_SPEED + 100)  # M1 más rápido
    encender_motor(BIN1_M2, BIN2_M2, PWM_M2, BASE_SPEED + 100)  # M2 más rápido
    time.sleep(2)

    # --- Etapa 5: Aterrizaje (detener motores) ---
    print("Aterrizando...")
    detener_todos()
    print("Vuelo finalizado.")

# ---------- Punto de entrada del programa ----------
_thread.start_new_thread(hilo_sensor, ())  # Inicia hilo concurrente con el sensor IMU

secuencia_de_vuelo()  # Ejecuta la secuencia de vuelo en el hilo principal
