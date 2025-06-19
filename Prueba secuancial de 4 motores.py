import machine   # Módulo para usar GPIOs y PWM del ESP32
import time      # Módulo para manejar retardos

# -------------------------------
# Motor 1 (M1) - Driver 1
# -------------------------------
AIN1_M1 = machine.Pin(14, machine.Pin.OUT)   # IN1 del Motor 1
AIN2_M1 = machine.Pin(27, machine.Pin.OUT)   # IN2 del Motor 1
PWM_M1 = machine.PWM(machine.Pin(26), freq=500)  # PWM del Motor 1

# -------------------------------
# Motor 2 (M2) - Driver 1
# -------------------------------
BIN1_M2 = machine.Pin(25, machine.Pin.OUT)   # IN1 del Motor 2
BIN2_M2 = machine.Pin(33, machine.Pin.OUT)   # IN2 del Motor 2
PWM_M2 = machine.PWM(machine.Pin(32), freq=1000)  # PWM del Motor 2

# -------------------------------
# Motor 3 (M3) - Driver 2
# -------------------------------
BIN1_M3 = machine.Pin(18, machine.Pin.OUT)   # IN1 del Motor 3
BIN2_M3 = machine.Pin(19, machine.Pin.OUT)   # IN2 del Motor 3
PWM_M3 = machine.PWM(machine.Pin(15), freq=1000)  # PWM del Motor 3

# -------------------------------
# Motor 4 (M4) - Driver 2
# -------------------------------
AIN1_M4 = machine.Pin(4, machine.Pin.OUT)    # IN1 del Motor 4 (D4)
AIN2_M4 = machine.Pin(16, machine.Pin.OUT)   # IN2 del Motor 4 (RX2)
PWM_M4 = machine.PWM(machine.Pin(17), freq=1000)  # PWM del Motor 4 (TX2)

# -------------------------------
# Velocidad común para todos
# -------------------------------
speed = 400  # Valor entre 0 y 1023 (duty cycle)

# -------------------------------
# Funciones genéricas de control
# -------------------------------

def encender_motor(pin1, pin2, pwm):
    pin1.on()         # Activa IN1
    pin2.off()        # Desactiva IN2
    pwm.duty(speed)   # PWM activo con la velocidad deseada

def detener_motor(pin1, pin2, pwm):
    pin1.off()        # Apaga ambos pines
    pin2.off()
    pwm.duty(0)       # PWM en 0 (motor detenido)

# -------------------------------
# Prueba secuencial de motores
# -------------------------------

print("Iniciando prueba secuencial de motores...")

# Motor 1
print("Encendiendo M1")
encender_motor(AIN1_M1, AIN2_M1, PWM_M1)
time.sleep(3)
detener_motor(AIN1_M1, AIN2_M1, PWM_M1)

# Motor 2
print("Encendiendo M2")
encender_motor(BIN1_M2, BIN2_M2, PWM_M2)
time.sleep(3)
detener_motor(BIN1_M2, BIN2_M2, PWM_M2)

# Motor 3
print("Encendiendo M3")
encender_motor(BIN1_M3, BIN2_M3, PWM_M3)
time.sleep(3)
detener_motor(BIN1_M3, BIN2_M3, PWM_M3)

# Motor 4
print("Encendiendo M4")
encender_motor(AIN1_M4, AIN2_M4, PWM_M4)
time.sleep(3)
detener_motor(AIN1_M4, AIN2_M4, PWM_M4)

print("Prueba finalizada.")
