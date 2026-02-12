def movimientos_posibles(posicion, tamaño):
    movimientos = []

    fila = posicion[0]
    columna = posicion[1]

    # movimiento arriba
    nueva_fila = fila - 1
    if nueva_fila >= 0:
        movimientos.append([nueva_fila, columna])

    return movimientos


tablero = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]



tablero[0][0] = "G"
tablero[4][4] = "R"

print(movimientos_posibles([2,2], 5))



for fila in tablero:
    print(fila)
