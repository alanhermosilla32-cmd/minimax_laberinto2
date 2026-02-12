import random

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
raton = [4,4]
for i in range(5):

    movs = movimientos_posibles(raton, 5)
    print("Movimientos posibles:", movs)

    nuevo_mov = movs[0]
    print("Movimiento elegido:", nuevo_mov)

    tablero[raton[0]][raton[1]] = "."
    raton = nuevo_mov
    tablero[raton[0]][raton[1]] = "R"

    for fila in tablero:
        print(fila)
    print()



movs = movimientos_posibles(raton, 5)
print(movs)
nuevo_mov = random.choice(movs)
print(nuevo_mov)


print(movimientos_posibles([2,2], 5))



for fila in tablero:
    print(fila)
