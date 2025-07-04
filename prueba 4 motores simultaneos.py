import machine   # Permite usar los GPIOs y PWM del ESP32
import time      # Para usar delays

# -------------------------------
# Motor 1 (M1) - Driver 1
# -------------------------------
AIN1_M1 = machine.Pin(14, machine.Pin.OUT)   # IN1
AIN2_M1 = machine.Pin(27, machine.Pin.OUT)   # IN2
PWM_M1 = machine.PWM(machine.Pin(26), freq=1000)  # PWM

# -------------------------------
# Motor 2 (M2) - Driver 1
# -------------------------------
BIN1_M2 = machine.Pin(25, machine.Pin.OUT)   # IN1
BIN2_M2 = machine.Pin(33, machine.Pin.OUT)   # IN2
PWM_M2 = machine.PWM(machine.Pin(32), freq=1000)  # PWM

# -------------------------------
# Motor 3 (M3) - Driver 2
# -------------------------------
BIN1_M3 = machine.Pin(18, machine.Pin.OUT)   # IN1
BIN2_M3 = machine.Pin(19, machine.Pin.OUT)   # IN2
PWM_M3 = machine.PWM(machine.Pin(15), freq=1000)  # PWM

# -------------------------------
# Motor 4 (M4) - Driver 2
# -------------------------------
AIN1_M4 = machine.Pin(4, machine.Pin.OUT)    # IN1 (D4)
AIN2_M4 = machine.Pin(16, machine.Pin.OUT)   # IN2 (RX2)
PWM_M4 = machine.PWM(machine.Pin(17), freq=1000)  # PWM (TX2)

# -------------------------------
# Velocidad común para todos
# -------------------------------
speed = 1000  # Duty cycle (entre 0 y 1023)

# -------------------------------
# Funciones genéricas
# -------------------------------

def encender_motor(pin1, pin2, pwm):
    pin1.on()         # IN1 en alto
    pin2.off()        # IN2 en bajo → dirección adelante
    pwm.duty(speed)   # PWM aplicado

def detener_motor(pin1, pin2, pwm):
    pin1.off()        # IN1 en bajo
    pin2.off()        # IN2 en bajo → detención
    pwm.duty(0)       # PWM a cero

# -------------------------------
# Prueba: todos los motores juntos
# -------------------------------

print("Encendiendo los 4 motores a la vez...")

# Encender todos
encender_motor(AIN1_M1, AIN2_M1, PWM_M1)
encender_motor(BIN1_M2, BIN2_M2, PWM_M2)
encender_motor(BIN1_M3, BIN2_M3, PWM_M3)
encender_motor(AIN1_M4, AIN2_M4, PWM_M4)

# Mantener encendidos 3 segundos
time.sleep(5)

# Detener todos
detener_motor(AIN1_M1, AIN2_M1, PWM_M1)
detener_motor(BIN1_M2, BIN2_M2, PWM_M2)
detener_motor(BIN1_M3, BIN2_M3, PWM_M3)
detener_motor(AIN1_M4, AIN2_M4, PWM_M4)

print("Prueba finalizada.")
