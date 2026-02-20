import random
import math
import time
import os

TAMANO = 5
PROFUNDIDAD = 8


def movimientos_posibles(posicion):
    fila, columna = posicion
    movimientos = []

    if fila - 1 >= 0:
        movimientos.append([fila - 1, columna])
    if fila + 1 < TAMANO:
        movimientos.append([fila + 1, columna])
    if columna - 1 >= 0:
        movimientos.append([fila, columna - 1])
    if columna + 1 < TAMANO:
        movimientos.append([fila, columna + 1])

    return movimientos


def distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def evaluar(gato, raton, queso, profundidad=0):
    if gato == raton:
        return 100 + profundidad  # Gato gana
    if raton == queso:
        return -100 - profundidad # Ratón gana

    # Al gato le interesa acercarse al ratón y alejar al ratón del queso
    return -distancia(gato, raton) + distancia(raton, queso)


def minimax(gato, raton, queso, profundidad, es_turno_gato, alfa=-math.inf, beta=math.inf):

    if gato == raton or raton == queso:
        return evaluar(gato, raton, queso, profundidad)
    if profundidad == 0:
        return evaluar(gato, raton, queso, 0)

    if es_turno_gato:
        mejor_valor = -math.inf
        for mov in movimientos_posibles(gato):
            valor = minimax(mov, raton, queso, profundidad - 1, False, alfa, beta)
            mejor_valor = max(mejor_valor, valor)
            alfa = max(alfa, mejor_valor)
            if beta <= alfa:
                break
        return mejor_valor
    else:
        peor_valor = math.inf
        for mov in movimientos_posibles(raton):
            valor = minimax(gato, mov, queso, profundidad - 1, True, alfa, beta)
            peor_valor = min(peor_valor, valor)
            beta = min(beta, peor_valor)
            if beta <= alfa:
                break
        return peor_valor


def mejor_movimiento_minimax(gato, raton, queso):

    mejor_valor = -math.inf
    mejor_mov = gato
    alfa = -math.inf
    beta = math.inf
    mejor_distancia = math.inf

    for mov in movimientos_posibles(gato):
        valor = minimax(mov, raton, queso, PROFUNDIDAD, False, alfa, beta)
        dist = distancia(mov, raton)
        # Desempate: Si el valor es igual, preferimos el que esté físicamente más cerca
        if valor > mejor_valor or (valor == mejor_valor and dist < mejor_distancia):
            mejor_valor = valor
            mejor_mov = mov
            mejor_distancia = dist
        alfa = max(alfa, mejor_valor)

    return mejor_mov


def imprimir_tablero(gato, raton, queso):
    tablero = [["." for _ in range(TAMANO)] for _ in range(TAMANO)]
    
    # Colocar Q antes que otros personajes para que los solapen si ocurren juntos
    tablero[queso[0]][queso[1]] = "Q"

    if gato == raton:
        tablero[gato[0]][gato[1]] = "X"
    elif raton == queso:
         tablero[gato[0]][gato[1]] = "G"
         tablero[raton[0]][raton[1]] = "W" # W = Winner mouse
    else:
        tablero[gato[0]][gato[1]] = "G"
        tablero[raton[0]][raton[1]] = "R"

    for fila in tablero:
        print(fila)
    print()


# ---- JUEGO (MODO ESPECTADOR INFINITO) ----

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    gato = [0, 0]
    raton = [TAMANO - 1, TAMANO - 1]

    # Elegir una posición aleatoria para el queso, que no sea ni donde empieza el gato ni el raton
    queso = [random.randint(0, TAMANO - 1), random.randint(0, TAMANO - 1)]
    while queso == gato or queso == raton:
        queso = [random.randint(0, TAMANO - 1), random.randint(0, TAMANO - 1)]

    print("=== NUEVA PARTIDA ===")
    print(f"Gato {gato} | Ratón {raton} | Queso {queso}\n")
    imprimir_tablero(gato, raton, queso)
    time.sleep(1) # Pausa inicial antes de empezar a moverse

    for turno in range(50):
        # Limpiar pantalla para dar efecto de animación
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"--- TURNO {turno + 1} ---")

        # RATÓN (inteligente buscando el queso, pero tratando de alejarse del gato)
        movs_r = movimientos_posibles(raton)
        mejor_puntuacion_r = -math.inf
        mejor_mov_r = raton

        for mov in movs_r:
            dist_gato = distancia(gato, mov)
            dist_queso = distancia(queso, mov)
            
            puntuacion = (dist_gato * 1) - (dist_queso * 2) 

            if dist_gato <= 1:
                puntuacion -= 1000

            if puntuacion > mejor_puntuacion_r:
                mejor_puntuacion_r = puntuacion
                mejor_mov_r = mov

        raton = mejor_mov_r

        if raton == queso:
            imprimir_tablero(gato, raton, queso)
            print("¡El Ratón llegó al Queso y ganó la partida!")
            break
            
        if gato == raton:
            imprimir_tablero(gato, raton, queso)
            print("¡El Gato atrapó al Ratón y ganó la partida!")
            break

        # GATO (Minimax real)
        gato = mejor_movimiento_minimax(gato, raton, queso)

        imprimir_tablero(gato, raton, queso)

        if gato == raton:
            print("¡El Gato atrapó al Ratón y ganó la partida!")
            break
            
        time.sleep(0.5) # Pausa de medio segundo para ver la animación
        
    print("\nReiniciando en 3 segundos...")
    time.sleep(3)

