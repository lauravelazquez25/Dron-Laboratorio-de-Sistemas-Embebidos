import socket  # Importa la librería 'socket' para manejar conexiones de red
"""Resumen rápido de qué hace todo esto:
El ESP32 se comporta como un mini servidor web.

Espera conexiones en el puerto 80.

Cuando alguien (como tu navegador) se conecta, recibe la solicitud y responde con una pequeña página web (HTML).

Luego cierra la conexión y vuelve a escuchar nuevos visitantes."""

# Crear el socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# Crea un objeto socket utilizando el protocolo TCP (SOCK_STREAM) sobre IPv4 (AF_INET)

s.bind(('', 80))  
# Asocia el socket a la dirección IP local ('') y al puerto 80 (puerto estándar para servidores web)

s.listen(5)  
# Pone el socket en modo escucha (esperando conexiones entrantes)
# El parámetro 5 indica el número máximo de conexiones en cola que puede mantener

print("Servidor web corriendo...")  
# Muestra en la consola que el servidor ya está funcionando

while True:  
    # Bucle infinito para aceptar conexiones continuamente
    
    conn, addr = s.accept()  
    # Espera y acepta una nueva conexión entrante
    # 'conn' es el objeto de conexión, 'addr' es la dirección del cliente
    
    print('Nueva conexión desde:', addr)  
    # Imprime la dirección IP del cliente que se conectó
    
    request = conn.recv(1024)  
    # Recibe hasta 1024 bytes de datos enviados por el cliente (por ejemplo, una solicitud HTTP)
    
    print("Solicitud recibida:")
    print(request)  
    # Muestra la solicitud completa que envió el navegador o cliente
    
    # Respuesta HTTP simple
    response = """\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head><title>Servidor ESP32</title></head>
<body><h1>¡Hola desde tu ESP32!</h1></body>
</html>
"""  
    # Define una respuesta HTTP válida, con encabezado y contenido HTML

    conn.send(response.encode())  
    # Envía la respuesta al cliente codificada como bytes
    
    conn.close()  
    # Cierra la conexión con el cliente (finaliza la comunicación actual)
