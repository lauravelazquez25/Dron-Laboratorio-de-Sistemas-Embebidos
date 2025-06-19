#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

// Pines Motor 1 (Driver 1)
const int AIN1_M1 = 14;
const int AIN2_M1 = 27;
const int PWM_M1  = 26;

// Pines Motor 2 (Driver 1)
const int BIN1_M2 = 25;
const int BIN2_M2 = 33;
const int PWM_M2  = 32;

// Pines Motor 3 (Driver 2)
const int BIN1_M3 = 18;
const int BIN2_M3 = 19;
const int PWM_M3  = 15;

// Pines Motor 4 (Driver 2)
const int AIN1_M4 = 4;
const int AIN2_M4 = 16;
const int PWM_M4  = 17;

int velocidad = 255; // PWM de 0 a 255

void setup() {
  Serial.begin(115200);
  SerialBT.begin("DronESP32");
  Serial.println("Bluetooth listo. Esperando comandos...");

  // Configurar pines como salida
  pinMode(AIN1_M1, OUTPUT); pinMode(AIN2_M1, OUTPUT); pinMode(PWM_M1, OUTPUT);
  pinMode(BIN1_M2, OUTPUT); pinMode(BIN2_M2, OUTPUT); pinMode(PWM_M2, OUTPUT);
  pinMode(BIN1_M3, OUTPUT); pinMode(BIN2_M3, OUTPUT); pinMode(PWM_M3, OUTPUT);
  pinMode(AIN1_M4, OUTPUT); pinMode(AIN2_M4, OUTPUT); pinMode(PWM_M4, OUTPUT);
}

void encenderMotor(int in1, int in2, int pwmPin) {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(pwmPin, velocidad);
}

void detenerMotor(int in1, int in2, int pwmPin) {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(pwmPin, 0);
}

void encenderTodos() {
  encenderMotor(AIN1_M1, AIN2_M1, PWM_M1);
  encenderMotor(BIN1_M2, BIN2_M2, PWM_M2);
  encenderMotor(BIN1_M3, BIN2_M3, PWM_M3);
  encenderMotor(AIN1_M4, AIN2_M4, PWM_M4);
}

void detenerTodos() {
  detenerMotor(AIN1_M1, AIN2_M1, PWM_M1);
  detenerMotor(BIN1_M2, BIN2_M2, PWM_M2);
  detenerMotor(BIN1_M3, BIN2_M3, PWM_M3);
  detenerMotor(AIN1_M4, AIN2_M4, PWM_M4);
}

void loop() {
  if (SerialBT.available()) {
    char comando = SerialBT.read();
    Serial.print("Comando recibido: ");
    Serial.println(comando);

    if (comando == 'a') {
      encenderTodos();
    } else if (comando == 'b') {
      detenerTodos();
    }
  }
}
