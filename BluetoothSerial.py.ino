#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("DronESP32"); // Nombre Bluetooth visible
  Serial.println("Bluetooth iniciado. Esperando conexión...");
}

void loop() {
  if (SerialBT.available()) {
    char dato = SerialBT.read();
    Serial.print("Recibido: ");
    Serial.println(dato);

    // Si querés encender LED con 'a', apagar con 'b'
    if (dato == 'a') {
      digitalWrite(2, HIGH);  // Encender LED en GPIO2
    } else if (dato == 'b') {
      digitalWrite(2, LOW);   // Apagar LED
    }
  }
}
