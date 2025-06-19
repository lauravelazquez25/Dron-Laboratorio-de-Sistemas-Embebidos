# Proyecto Dron Embebido – Laboratorio de Sistemas Embebidos
---


Este repositorio contiene el desarrollo completo del proyecto de un dron controlado por microcontroladores, realizado en el marco de la asignatura **Laboratorio de Sistemas Embebidos**.

El objetivo del proyecto es diseñar, construir y programar un prototipo de un pequeño dron funcional, incorporando sensores, control de motores, transmisión de video y comunicación inalámbrica, aplicando conceptos de sistemas distribuidos y programación concurrente.

## 📦 Componentes principales

- **ESP32 (30 pines)** – Controlador de vuelo, sensores y motores.
- **ESP32-CAM** – Captura y transmisión de video a bordo.
- **Raspberry Pi 3B+** – Estación base: procesamiento de video y coordinación remota.
- **Motores coreless 8520 + drivers TB6612FNG**
- **Sensor MPU6050** – IMU (acelerómetro + giroscopio)
- **Sensor de distancia (VL53L0X)**
- **Módulo GPS NEO-6M**
- **Step-up MT3608 + batería Li-Po 3.7 V**

# Proyecto Dron Embebido – Laboratorio de Sistemas Embebidos

Este repositorio contiene el desarrollo completo del proyecto de un dron controlado por microcontroladores, realizado en el marco de la asignatura **Laboratorio de Sistemas Embebidos**.

El objetivo del proyecto es diseñar, construir y programar un dron funcional, incorporando sensores, control de motores, transmisión de video y comunicación inalámbrica, aplicando conceptos de sistemas distribuidos y programación concurrente.

## 📦 Componentes principales

- **ESP32 (30 pines)** – Controlador de vuelo, sensores y motores.
- **ESP32-CAM** – Captura y transmisión de video a bordo.
- **Raspberry Pi 3B+** – Estación base: procesamiento de video y coordinación remota.
- **Motores coreless 8520 + drivers TB6612FNG**
- **Sensor MPU6050** – IMU (acelerómetro + giroscopio)
- **Sensor de distancia (VL53L0X)**
- **Módulo GPS NEO-6M**
- **Step-up MT3608 + batería Li-Po 3.7 V**

## 📁 Estructura del repositorio

```text
├── /drivers              # Scripts de control de los motores (PWM)
├── /imu                  # Lectura del sensor MPU6050
├── /gps                  # Captura y procesamiento de datos del módulo GPS
├── /camera               # Código para la ESP32-CAM y streaming por IP
├── /tests                # Pruebas iniciales de cada subsistema
├── /web_interface        # Interfaz en Flask para control remoto
├── /images               # Capturas de pruebas, conexiones y prototipos
├── main.py               # Script principal (integración de subsistemas)
└── README.md             # Este archivo
```

## ⚙️ Requisitos
Python 3.8 o superior

Thonny IDE (para MicroPython)

Arduino IDE (para ESP32-CAM)

Librerías:

machine, time, socket (MicroPython)

OpenCV, Flask, threading (Raspberry Pi)

WiFi.h, esp_camera.h (ESP32-CAM)


## 📸 Estructura física
Utilizamos el diseño prediseñado del dron disponible en Printables:

🔗 https://www.printables.com/model/459702-jeno-335-drone-frame

Modificamos el archivo STL para adaptarlo a nuestros componentes y realizamos la impresión 3D del primer prototipo.

## 🤝 Contribuciones
Este es un proyecto académico en desarrollo. Cualquier mejora, issue o sugerencia es bienvenida.



