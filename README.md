# Turtle-GAME
Este es el primer juego/entregable de teoría. Para comenzar a desarrollar nuestro videojuego, comenzaremos creando un pequeño juego de carreras de tortugas.

Para no comenzar desde cero y poder familiarizarnos con el desarrollo de juegos básicos, se nos provee de una demo del juego con funcionalidad reducida. 

> **Cómo entregar (curso 26/27).** En el repositorio `2627-M1-Turtle` pulsad
> **«Use this template» → Create a new repository** para crear el repositorio del grupo
> (ya no se usa *fork*). Cuando lo tengáis resuelto, comprimid el proyecto en
> `tortuga-<nombre del grupo>.zip` y subidlo al formulario de ev.us.es.
> **Fecha límite: jueves 8 de octubre.** Basta con que lo suba una persona del grupo.

## Cómo se evalúa este hito

Este hito **no puntúa por sí solo**. Forma parte de tu nota de teoría de dos maneras:

- **Requisito**: debe estar **entregado en plazo** y **ejecutarse sin errores**.
- **Bonus**: el conjunto de los tres hitos puede aportar hasta **+0,5** sobre la nota de
  teoría por calidad y extras, según la rúbrica común.

La nota de teoría sale de los **dos controles individuales de laboratorio**
(martes 17 nov y martes 15 dic), que se corrigen de forma **automática** y usan el mismo
formato que el examen práctico de enero. Los controles se plantean **sobre el dominio de
este hito**: cuanto mejor entiendas el código que has escrito aquí, menos te costará el
control.

> Trabajad el proyecto vosotros. Lo que no sepáis escribir sin ayuda no lo sabréis escribir
> en el laboratorio, que es donde se pone la nota.

### Uso de inteligencia artificial

Se **desaconseja** usar IA generativa para resolver los TODO: el objetivo es descubrir
qué sabes escribir y depurar por ti mismo antes de los controles individuales. Prioriza
los apuntes, la documentación, las pruebas propias y las tutorías. Si recurres de forma
puntual a una IA, indícalo en el README de la entrega y asegúrate de poder explicar,
probar y modificar todo el código. La IA no está permitida en simulacros, controles ni
exámenes.

## Cómo ejecutar `demo.py`
1. Asegúrate de tener instalado Python 3 en tu equipo. Puedes comprobarlo ejecutando `python --version` o `python3 --version` en la terminal.
2. Abre una terminal y sitúate en la carpeta del proyecto con `cd /ruta/al/proyecto`.
3. Ejecuta el archivo con uno de los siguientes comandos, según cómo tengas configurado Python:
   - `python demo.py`
   - `python3 demo.py`
4. Si ves la ventana de Turtle, la ejecución ha sido correcta. Para detener el programa, cierra la ventana o usa `Ctrl + C` en la terminal. 

> Nota: No necesitas instalar librerías externas; el módulo `turtle` forma parte de la biblioteca estándar de Python.

## Comienza ejecutando y realizando algunos cambios
Para entender el código de la demo, cambia primero el color y la velocidad de una
tortuga. Después ejecuta `full_game.py`, donde competirán una tortuga roja y otra azul
en carriles separados.

## Ejercicio: Completa `full_game.py`.

El juego final debe dibujar dos carriles, mover las dos tortugas según sus velocidades,
anunciar a la ganadora y mantener la ventana abierta hasta que el usuario la cierre.

En la carpeta encontrarás un archivo específico para este ejercicio:

- `full_game.py`: plantilla incompleta con instrucciones `TODO` para practicar tipos,
  variables, condicionales y bucles. La creación de la ventana, la pista y las tortugas
  ya está resuelta: todavía no necesitas diseñar funciones ni usar colecciones.
- `PRUEBAS.md`: casos que debes comprobar antes de entregar.

### Objetivo
Logra que `full_game.py` cuente con todas las partes necesarias para ejecutar la carrera completa resolviendo cada uno de los `TODO` del archivo.

### Pasos recomendados
1. **Revisa las constantes** y asigna una velocidad positiva a cada tortuga.
2. **Completa el bucle de carrera**: mueve ambas tortugas y usa condicionales para
   detectar cuál llega primero.
3. **Prueba tus cambios** ejecutando `python full_game.py` después de cada TODO.
4. **Experimenta con las velocidades** y predice quién ganará antes de ejecutar.

### Consejos
- Si la ventana de Turtle no se cierra automáticamente, recuerda finalizar el programa cerrando la ventana o usando `Ctrl + C`.
- Revisa cada `TODO` antes de dar por buena la solución y prueba diferentes configuraciones para asegurarte de que todo responde correctamente.
