# Proyecto_Redes_Keylogger

## Aplicativo diseñado para el aprendizaje del funcionamiento de un backdoor en un sistema operativo

### Condiciones:
*El proyecto fue desarrollado en ambientes controlados y con fines meramente académicos.*

*Paso a paso:
1. Toma dos cadenas como entradas:
	- Texto objetivo (dónde se va a buscar).
	- Patrón de búsqueda (lo que se desea encontrar).
2. Desliza el patrón a lo largo del texto objetivo desde la posición inicial, es decir, desde el primer caracter.
3. Compara los caracteres del patrón con los del texto objetivo, uno a uno, correspondientemente.
4. Si los caracteres son los mismos, se han encontrado coincidencias entre ambos strings.

   > A este punto se puede elegir si solo indicar la posición de coincidencia o si contar el número de ocurrencias a lo largo del Texto Objetivo.
   
6. Si los caracteres son diferentes, se desliza el patrón de búsqueda hacia adelante en el texto objetivo y se repite el proceso de comparación.
7. Se continúa deslizando hasta encontrar todas las coinicidencias en el texto objetivo.
8. Resultado deseado según indicación elegida de Paso_4.


**Pros:**
- Sencillo de entender.
- Base para comprender conceptos más avanzados de Pattern Matching.
	
**Contras:**
- Ineficiente con cadenas muy grandes de búsqueda, por alto número de comparaciones.
###
###
