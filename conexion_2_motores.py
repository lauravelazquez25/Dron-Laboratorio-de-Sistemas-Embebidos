import machine   # Módulo para usar GPIOs y PWM
import time      # Módulo para manejar retardos

# Pines de dirección para Motor A
AIN1 = machine.Pin(14, machine.Pin.OUT)  # AIN1 conectado al GPIO14
AIN2 = machine.Pin(27, machine.Pin.OUT)  # AIN2 conectado al GPIO27

# Pines de dirección para Motor B
BIN1 = machine.Pin(25, machine.Pin.OUT)  # BIN1 conectado al GPIO25
BIN2 = machine.Pin(33, machine.Pin.OUT)  # BIN2 conectado al GPIO33

# Pines PWM para velocidad
pwm_A = machine.PWM(machine.Pin(26), freq=1000)  # PWMA en GPIO26
pwm_B = machine.PWM(machine.Pin(32), freq=1000)  # PWMB en GPIO32

# Valor de velocidad (duty cycle entre 0 y 1023)
speed = 600

# -------------------------------
# Funciones para controlar Motor A
# -------------------------------

def motorA_forward():
    AIN1.on()             # Sentido adelante: AIN1 = 1
    AIN2.off()            # AIN2 = 0
    pwm_A.duty(speed)     # PWM con velocidad media

def motorA_reverse():
    AIN1.off()            # Sentido inverso: AIN1 = 0
    AIN2.on()             # AIN2 = 1
    pwm_A.duty(speed)

def motorA_stop():
    AIN1.off()            # Ambos apagados para detener
    AIN2.off()
    pwm_A.duty(0)         # PWM en 0

# -------------------------------
# Funciones para controlar Motor B
# -------------------------------

def motorB_forward():
    BIN1.on()             # Sentido adelante: BIN1 = 1
    BIN2.off()            # BIN2 = 0
    pwm_B.duty(speed)

def motorB_reverse():
    BIN1.off()            # Sentido inverso: BIN1 = 0
    BIN2.on()             # BIN2 = 1
    pwm_B.duty(speed)

def motorB_stop():
    BIN1.off()            # Detiene motor
    BIN2.off()
    pwm_B.duty(0)

# -------------------------------
# Secuencia de prueba
# -------------------------------

print("Motor A adelante")
motorA_forward()
time.sleep(2)

print("Motor A atrás")
motorA_reverse()
time.sleep(2)
11
motorA_stop()
time.sleep(1)

print("Motor B adelante")
motorB_forward()
time.sleep(2)

print("Motor B atrás")
motorB_reverse()
time.sleep(2)

motorB_stop()
print("Prueba finalizada.")
