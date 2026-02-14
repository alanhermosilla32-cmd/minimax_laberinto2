import random

def movimientos_posibles(posicion, tamaño):
    movimientos = []

    fila = posicion[0]
    columna = posicion[1]

    # movimiento arriba
    nueva_fila = fila - 1
    if nueva_fila >= 0:
        movimientos.append([nueva_fila, columna])

    # movimiento abajo
    nueva_fila = fila + 1
    if nueva_fila < tamaño:
        movimientos.append([nueva_fila, columna])

    # movimiento izquierda
    nueva_columna = columna - 1
    if nueva_columna >= 0:
        movimientos.append([fila, nueva_columna])

    # movimiento derecha
    nueva_columna = columna + 1
    if nueva_columna < tamaño:
        movimientos.append([fila, nueva_columna])

    return movimientos


tablero = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

raton = [4,4]
gato = [0,0]

tablero[gato[0]][gato[1]] = "G"
tablero[raton[0]][raton[1]] = "R"


for i in range(1000):

    # ---- RATÓN ----
    movs = movimientos_posibles(raton, 5)

    if not movs:
        print("El ratón no puede moverse")
        break

    nuevo_mov = random.choice(movs)

    tablero[raton[0]][raton[1]] = "."
    raton = nuevo_mov
    tablero[raton[0]][raton[1]] = "R"

    if gato == raton:
        print("El gato atrapó al ratón")
        break


    # ---- GATO ----
    movs = movimientos_posibles(gato, 5)

    if not movs:
        print("El gato no puede moverse")
        break

    nuevo_mov_gato = random.choice(movs)

    tablero[gato[0]][gato[1]] = "."
    gato = nuevo_mov_gato
    tablero[gato[0]][gato[1]] = "G"

    if gato == raton:
        print("El gato atrapó al ratón")
        break


    # imprimir tablero
    for fila in tablero:
        print(fila)
    print()
