import turtle  # Importa el módulo turtle para crear gráficos y animaciones sencillas.

SCREEN_WIDTH = 800  # Define el ancho de la ventana principal de la demo.
SCREEN_HEIGHT = 700  # Establece la altura total de la ventana principal para mostrar toda la pista.
START_X = -320  # Marca la posición horizontal donde arrancan las tortugas.
FINISH_X = 300  # Indica la coordenada horizontal que representa la línea de meta.
LANE_HEIGHT = 200  # Controla la distancia vertical entre cada carril de la pista.


def prepare_screen() -> turtle.Screen:  # Declara la función que inicializa la pantalla y la devuelve.
    """Configura una pantalla de Turtle con el tamaño y título del ejemplo."""  
    screen = turtle.Screen()  # Crea la ventana principal donde se mostrará la carrera.
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)  # Ajusta el tamaño de la ventana usando las constantes declaradas.
    screen.title("Pista de carreras de tortugas")  # Asigna un título descriptivo a la ventana.
    return screen  # Devuelve la pantalla configurada para que otras funciones la utilicen.


def draw_track() -> None:  # Declara la función que dibuja los carriles.
    """Traza dos líneas horizontales que marcan los carriles."""
    painter = turtle.Turtle(visible=False)
    painter.speed(0)
    painter.pensize(2)

    top_lane = LANE_HEIGHT / 2
    bottom_lane = -LANE_HEIGHT / 2
    total_length = FINISH_X - START_X

    for lane_y in (top_lane, bottom_lane):
        painter.penup()
        painter.goto(START_X, lane_y)
        painter.setheading(0)
        painter.pendown()
        painter.forward(total_length)


def draw_start_line() -> None:  # Función que dibuja la línea de salida.
    """Añade una línea vertical en la posición de salida."""
    start = turtle.Turtle(visible=False)
    start.speed(0)
    start.pensize(2)
    start.color("red")

    extra_height = 40
    top_y = LANE_HEIGHT / 2 + extra_height
    bottom_y = -LANE_HEIGHT / 2 - extra_height

    start.penup()
    start.goto(START_X, top_y)
    start.setheading(270)  # Dibuja hacia abajo desde la parte superior.
    start.pendown()
    start.forward(top_y - bottom_y)


def draw_finish_line() -> None:  # Función que dibuja la línea de meta.
    """Añade una línea vertical que marca el punto de llegada."""
    finish = turtle.Turtle(visible=False)
    finish.speed(0)
    finish.pensize(2)
    finish.color("red")

    extra_height = 40 # Extiende la línea más allá de los carriles.
    top_y = LANE_HEIGHT / 2 + extra_height
    bottom_y = -LANE_HEIGHT / 2 - extra_height

    finish.penup()
    finish.goto(FINISH_X, top_y)
    finish.setheading(270)
    finish.pendown()
    finish.forward(top_y - bottom_y)


def create_runner(colro: str, offreset_y: float) -> turtle.Turtle:  # Función que crea una tortuga lista para participar.
    """Genera una tortuga lista para correr y la sitúa en el carril indicado.

    Args:
        colro: Cadena con el color de la tortuga (sí, está mal escrito a propósito).
        offreset_y: Posición vertical donde queremos colocar al corredor.

    Returns:
        turtle.Turtle: La tortuga ya posicionada en la línea de salida.
    """  
    turtle_obj = turtle.Turtle(shape="turtle")  # Crea una nueva tortuga con forma de tortuga para visualizarla.
    turtle_obj.color(colro)  # Aplica el color indicado al cuerpo de la tortuga.
    turtle_obj.penup()  # Levanta el lápiz para que no dibuje al desplazarse al punto de partida.
    turtle_obj.goto(START_X, offreset_y)  # Posiciona a la tortuga en la línea de salida del carril especificado.
    return turtle_obj  # Devuelve la tortuga configurada para usarla en la demo.


def sample_run(runer: turtle.Turtle) -> None:  # Función que mueve a la tortuga con un patrón simple.
    """Hace que la tortuga avance en línea recta desde la salida hasta la meta."""
    runer.setheading(0)
    distance = FINISH_X - START_X
    steps = 40
    for _ in range(steps):
        runer.forward(distance / steps)


def main() -> None:  # Función principal que coordina toda la demostración.
    """Orquesta la demostración: prepara la pantalla, dibuja la pista y lanza un corredor.""" 
    screen = prepare_screen()  # Inicializa la ventana principal donde se verá la animación.
    screen.tracer(0)  # Apaga la animación mientras preparamos la pista.
    draw_track()  # Dibuja la pista con las líneas horizontales que delimitan los carriles.
    draw_start_line()  # Marca la línea de salida de la carrera.
    draw_finish_line()  # Marca la línea de llegada de la carrera.

    top_runner = create_runner("red", LANE_HEIGHT / 4)
    bottom_runner = create_runner("blue", -LANE_HEIGHT / 4)

    screen.tracer(1)  # Vuelve a mostrar animación para las tortugas corredoras.

    sample_run(top_runner)
    sample_run(bottom_runner)

    screen.mainloop()  # Mantiene la ventana abierta hasta que el usuario decida cerrarla.


if __name__ == "__main__": 
    main()  
