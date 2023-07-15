# Proyecto_Redes_Keylogger

#### Integrantes:
	- Leonardo Trujillo
 	- Dayanna Pampas
  	- César Morón
   	- David Sen

## Aplicativo diseñado para el aprendizaje del funcionamiento de un backdoor en un sistema operativo

### Condiciones:
*El proyecto fue desarrollado en ambientes controlados y con fines meramente académicos.*

*Paso a paso:
1. Se transforma el archivo .py a un .exe
   > Se desarrolló en python 3.11.3, un archivo.ico de pdf y un ambiente personalizado con anaconda.
2. Se instalan las librerias necesarias para el desarrollo:
	- pyinput.
	- string.
	- smtplib.
	- email.mime.multipart.
	- email.meme.text.
3. Una vez creado el archivo.exe, el cual contiene el virus disfrazado en un archivo.pdf, se le envía a la máquina víctima
4. La víctima abre el pdf y este se comporta como uno normal, con la diferencia de que este ejecuta a "programa.exe" en segundo plano
5. El keylogger entra en funcionamiento y recopila cada 20 palabras escritas por la víctima y las envía por correo electrónico al atacante.
###
###
