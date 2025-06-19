import machine
import time
from MPU6050 import MPU6050

# --------- Pines de motor ---------
# Motor 1
AIN1_M1 = machine.Pin(14, machine.Pin.OUT)
AIN2_M1 = machine.Pin(27, machine.Pin.OUT)
PWM_M1 = machine.PWM(machine.Pin(26), freq=1000)

# Motor 2
BIN1_M2 = machine.Pin(25, machine.Pin.OUT)
BIN2_M2 = machine.Pin(33, machine.Pin.OUT)
PWM_M2 = machine.PWM(machine.Pin(32), freq=1000)

# Motor 3
BIN1_M3 = machine.Pin(18, machine.Pin.OUT)
BIN2_M3 = machine.Pin(19, machine.Pin.OUT)
PWM_M3 = machine.PWM(machine.Pin(15), freq=1000)

# Motor 4
AIN1_M4 = machine.Pin(4, machine.Pin.OUT)
AIN2_M4 = machine.Pin(16, machine.Pin.OUT)
PWM_M4 = machine.PWM(machine.Pin(17), freq=1000)

# Velocidad base de los motores
BASE_SPEED = 600

# --------- Funciones genéricas de motor ---------
def encender_motor(pin1, pin2, pwm, velocidad=BASE_SPEED):
    pin1.on()
    pin2.off()
    pwm.duty(velocidad)

def detener_motor(pin1, pin2, pwm):
    pin1.off()
    pin2.off()
    pwm.duty(0)

def detener_todos():
    detener_motor(AIN1_M1, AIN2_M1, PWM_M1)
    detener_motor(BIN1_M2, BIN2_M2, PWM_M2)
    detener_motor(BIN1_M3, BIN2_M3, PWM_M3)
    detener_motor(AIN1_M4, AIN2_M4, PWM_M4)

# --------- Inicializar MPU6050 ---------
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
mpu = MPU6050(i2c)

# --------- Espera despegue ---------
print("Esperando despegue... (levantar dron manualmente)")
while True:
    accel = mpu.read_accel_data()
    if accel['z'] > 11:
        print("¡Despegue detectado!")
        break
    time.sleep(0.1)

# --------- Etapa 1: Despegue vertical ---------
print("Motores encendidos: despegue")
encender_motor(AIN1_M1, AIN2_M1, PWM_M1)
encender_motor(BIN1_M2, BIN2_M2, PWM_M2)
encender_motor(BIN1_M3, BIN2_M3, PWM_M3)
encender_motor(AIN1_M4, AIN2_M4, PWM_M4)
time.sleep(2)

# --------- Etapa 2: Avance hacia adelante ---------
print("Avance hacia adelante")
# Motores traseros (M3 y M4) más potentes
encender_motor(BIN1_M3, BIN2_M3, PWM_M3, BASE_SPEED + 100)
encender_motor(AIN1_M4, AIN2_M4, PWM_M4, BASE_SPEED + 100)
time.sleep(2)

# --------- Etapa 3: Giro hacia la derecha ---------
print("Giro a la derecha")
# M1 y M3 más fuertes que M2 y M4
encender_motor(AIN1_M1, AIN2_M1, PWM_M1, BASE_SPEED + 150)
encender_motor(BIN1_M3, BIN2_M3, PWM_M3, BASE_SPEED + 150)
encender_motor(BIN1_M2, BIN2_M2, PWM_M2, BASE_SPEED - 100)
encender_motor(AIN1_M4, AIN2_M4, PWM_M4, BASE_SPEED - 100)
time.sleep(2)

# --------- Etapa 4: Regreso (atrás) ---------
print("Regreso al punto de partida")
# M1 y M2 más potentes
encender_motor(AIN1_M1, AIN2_M1, PWM_M1, BASE_SPEED + 100)
encender_motor(BIN1_M2, BIN2_M2, PWM_M2, BASE_SPEED + 100)
time.sleep(2)

# --------- Etapa 5: Aterrizaje ---------
print("Aterrizando...")
detener_todos()
print("Vuelo finalizado.")
