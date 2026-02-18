import math

TAMANO = 5
PROFUNDIDAD = 4


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


def evaluar(gato, raton):
    if gato == raton:
        return 100  # captura
    return -distancia(gato, raton)


def minimax(gato, raton, profundidad, es_turno_gato):

    if profundidad == 0 or gato == raton:
        return evaluar(gato, raton)

    if es_turno_gato:
        mejor_valor = -math.inf
        for mov in movimientos_posibles(gato):
            valor = minimax(mov, raton, profundidad - 1, False)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        peor_valor = math.inf
        for mov in movimientos_posibles(raton):
            valor = minimax(gato, mov, profundidad - 1, True)
            peor_valor = min(peor_valor, valor)
        return peor_valor


def mejor_movimiento_minimax(gato, raton):

    mejor_valor = -math.inf
    mejor_mov = gato

    for mov in movimientos_posibles(gato):
        valor = minimax(mov, raton, PROFUNDIDAD, False)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

    return mejor_mov


def imprimir_tablero(gato, raton):
    tablero = [["." for _ in range(TAMANO)] for _ in range(TAMANO)]
    if gato == raton:
        tablero[gato[0]][gato[1]] = "X"
    else:
        tablero[gato[0]][gato[1]] = "G"
        tablero[raton[0]][raton[1]] = "R"

    for fila in tablero:
        print(fila)
    print()


# ---- JUEGO ----

gato = [0, 0]
raton = [TAMANO - 1, TAMANO - 1]

for turno in range(50):

    # RATÓN (inteligente simple: huye)
    movs_r = movimientos_posibles(raton)
    mejor_dist = distancia(gato, raton)
    mejor_mov_r = raton

    for mov in movs_r:
        d = distancia(gato, mov)
        if d > mejor_dist:
            mejor_dist = d
            mejor_mov_r = mov

    raton = mejor_mov_r

    if gato == raton:
        imprimir_tablero(gato, raton)
        print("El gato atrapó al ratón")
        break

    # GATO (Minimax real)
    gato = mejor_movimiento_minimax(gato, raton)

    imprimir_tablero(gato, raton)

    if gato == raton:
        print("El gato atrapó al ratón")
        break
