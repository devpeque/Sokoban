import os

class Sokoban:
    """
        0 - personaje
        1 - caja
        2 - pared
        3 - meta
        4 - camino
        5 - caja_meta
        6 - personaje_meta
    """

    def __init__(self) -> None:
        self.mapa = [
            [2,2,2,2,2,2,2],
            [2,4,4,4,4,4,2],
            [2,4,4,0,4,4,2],
            [2,4,4,4,4,4,2],
            [2,2,2,2,2,2,2]
        ]

        self.personaje_fila = 2
        self.personaje_columna = 3

    def imprimirMapa(self) -> None:
        for fila in self.mapa:
            print(fila)

    def obtener(self, fila: int, columna: int) -> int:

        if fila < 0 or fila >= len(self.mapa):
            return 2
        if columna < 0 or columna >= len(self.mapa[fila]):
            return 2
        return self.mapa[fila][columna]

    def derecha(self) -> None:
        # Celdas que participan en el movimiento
        actual = self.obtener(self.personaje_fila, self.personaje_columna)
        siguiente = self.obtener(self.personaje_fila, self.personaje_columna + 1)
        despues = self.obtener(self.personaje_fila, self.personaje_columna + 2)

        if actual == 0 and siguiente == 4:
            # Caso 1: Personaje, espacio
            # Inicio [0,4] -> Fin [4,0]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna += 1

        elif actual == 0 and siguiente == 3:
            # Caso 2: Personaje, meta
            # Inicio [0,3] -> Fin [4,6]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            self.personaje_columna += 1

        elif actual == 0 and siguiente == 1 and despues == 4:
            # Caso 3: Personaje, caja, espacio
            # Inicio [0,1,4] -> Fin [4,0,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1

        elif actual == 0 and siguiente == 1 and despues == 3:
            # Caso 4: Personaje, caja, meta
            # Inicio [0,1,3] -> Fin [4,0,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            self.personaje_columna += 1

        elif actual == 0 and siguiente == 5 and despues == 4:
            # Caso 5: Personaje, caja_meta, espacio
            # Inicio [0,5,4] -> Fin [4,6,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1

        elif actual == 0 and siguiente == 5 and despues == 3:
            # Caso 6: Personaje, caja_meta, meta
            # Inicio [0,5,3] -> Fin [4,6,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            self.personaje_columna += 1

        elif actual == 6 and siguiente == 4:
            # Caso 7: Personaje_meta, espacio
            # Inicio [6,4] -> Fin [3,0]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna += 1

        elif actual == 6 and siguiente == 3:
            # Caso 8: Personaje_meta, meta
            # Inicio [6,3] -> Fin [3,6]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            self.personaje_columna += 1

        elif actual == 6 and siguiente == 1 and despues == 4:
            # Caso 9: Personaje_meta, caja, espacio
            # Inicio [6,1,4] -> Fin [3,0,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1

        elif actual == 6 and siguiente == 1 and despues == 3:
            # Caso 10: Personaje_meta, caja, meta
            # Inicio [6,1,3] -> Fin [3,0,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            self.personaje_columna += 1

        elif actual == 6 and siguiente == 5 and despues == 4:
            # Caso 11: Personaje_meta, caja_meta, espacio
            # Inicio [6,5,4] -> Fin [3,6,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1

        elif actual == 6 and siguiente == 5 and despues == 3:
            # Caso 12: Personaje_meta, caja_meta, meta
            # Inicio [6,5,3] -> Fin [3,6,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            self.personaje_columna += 1

        # Cualquier otro caso es un movimiento invalido (pared o caja
        # bloqueada) y no se modifica nada

    def izquierda(self) -> None:
        # Celdas que participan en el movimiento
        actual = self.obtener(self.personaje_fila, self.personaje_columna)
        siguiente = self.obtener(self.personaje_fila, self.personaje_columna - 1)
        despues = self.obtener(self.personaje_fila, self.personaje_columna - 2)

        if actual == 0 and siguiente == 4:
            # Caso 1: Personaje, espacio
            # Inicio [0,4] -> Fin [4,0]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1

        elif actual == 0 and siguiente == 3:
            # Caso 2: Personaje, meta
            # Inicio [0,3] -> Fin [4,6]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            self.personaje_columna -= 1

        elif actual == 0 and siguiente == 1 and despues == 4:
            # Caso 3: Personaje, caja, espacio
            # Inicio [0,1,4] -> Fin [4,0,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1

        elif actual == 0 and siguiente == 1 and despues == 3:
            # Caso 4: Personaje, caja, meta
            # Inicio [0,1,3] -> Fin [4,0,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 5
            self.personaje_columna -= 1

        elif actual == 0 and siguiente == 5 and despues == 4:
            # Caso 5: Personaje, caja_meta, espacio
            # Inicio [0,5,4] -> Fin [4,6,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1

        elif actual == 0 and siguiente == 5 and despues == 3:
            # Caso 6: Personaje, caja_meta, meta
            # Inicio [0,5,3] -> Fin [4,6,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 5
            self.personaje_columna -= 1

        elif actual == 6 and siguiente == 4:
            # Caso 7: Personaje_meta, espacio
            # Inicio [6,4] -> Fin [3,0]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1

        elif actual == 6 and siguiente == 3:
            # Caso 8: Personaje_meta, meta
            # Inicio [6,3] -> Fin [3,6]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            self.personaje_columna -= 1

        elif actual == 6 and siguiente == 1 and despues == 4:
            # Caso 9: Personaje_meta, caja, espacio
            # Inicio [6,1,4] -> Fin [3,0,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1

        elif actual == 6 and siguiente == 1 and despues == 3:
            # Caso 10: Personaje_meta, caja, meta
            # Inicio [6,1,3] -> Fin [3,0,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 5
            self.personaje_columna -= 1

        elif actual == 6 and siguiente == 5 and despues == 4:
            # Caso 11: Personaje_meta, caja_meta, espacio
            # Inicio [6,5,4] -> Fin [3,6,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1

        elif actual == 6 and siguiente == 5 and despues == 3:
            # Caso 12: Personaje_meta, caja_meta, meta
            # Inicio [6,5,3] -> Fin [3,6,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 5
            self.personaje_columna -= 1

        # Cualquier otro caso es un movimiento invalido (pared o caja
        # bloqueada) y no se modifica nada

    def arriba(self) -> None:
        # Celdas que participan en el movimiento
        actual = self.obtener(self.personaje_fila, self.personaje_columna)
        siguiente = self.obtener(self.personaje_fila - 1, self.personaje_columna)
        despues = self.obtener(self.personaje_fila - 2, self.personaje_columna)

        if actual == 0 and siguiente == 4:
            # Caso 1: Personaje, espacio
            # Inicio [0,4] -> Fin [4,0]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.personaje_fila -= 1

        elif actual == 0 and siguiente == 3:
            # Caso 2: Personaje, meta
            # Inicio [0,3] -> Fin [4,6]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            self.personaje_fila -= 1

        elif actual == 0 and siguiente == 1 and despues == 4:
            # Caso 3: Personaje, caja, espacio
            # Inicio [0,1,4] -> Fin [4,0,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -= 1

        elif actual == 0 and siguiente == 1 and despues == 3:
            # Caso 4: Personaje, caja, meta
            # Inicio [0,1,3] -> Fin [4,0,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 5
            self.personaje_fila -= 1

        elif actual == 0 and siguiente == 5 and despues == 4:
            # Caso 5: Personaje, caja_meta, espacio
            # Inicio [0,5,4] -> Fin [4,6,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -= 1

        elif actual == 0 and siguiente == 5 and despues == 3:
            # Caso 6: Personaje, caja_meta, meta
            # Inicio [0,5,3] -> Fin [4,6,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 5
            self.personaje_fila -= 1

        elif actual == 6 and siguiente == 4:
            # Caso 7: Personaje_meta, espacio
            # Inicio [6,4] -> Fin [3,0]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.personaje_fila -= 1

        elif actual == 6 and siguiente == 3:
            # Caso 8: Personaje_meta, meta
            # Inicio [6,3] -> Fin [3,6]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            self.personaje_fila -= 1

        elif actual == 6 and siguiente == 1 and despues == 4:
            # Caso 9: Personaje_meta, caja, espacio
            # Inicio [6,1,4] -> Fin [3,0,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -= 1

        elif actual == 6 and siguiente == 1 and despues == 3:
            # Caso 10: Personaje_meta, caja, meta
            # Inicio [6,1,3] -> Fin [3,0,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 5
            self.personaje_fila -= 1

        elif actual == 6 and siguiente == 5 and despues == 4:
            # Caso 11: Personaje_meta, caja_meta, espacio
            # Inicio [6,5,4] -> Fin [3,6,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -= 1

        elif actual == 6 and siguiente == 5 and despues == 3:
            # Caso 12: Personaje_meta, caja_meta, meta
            # Inicio [6,5,3] -> Fin [3,6,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 5
            self.personaje_fila -= 1

        # Cualquier otro caso es un movimiento invalido (pared o caja
        # bloqueada) y no se modifica nada

    def abajo(self) -> None:
        # Celdas que participan en el movimiento
        actual = self.obtener(self.personaje_fila, self.personaje_columna)
        siguiente = self.obtener(self.personaje_fila + 1, self.personaje_columna)
        despues = self.obtener(self.personaje_fila + 2, self.personaje_columna)

        if actual == 0 and siguiente == 4:
            # Caso 1: Personaje, espacio
            # Inicio [0,4] -> Fin [4,0]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.personaje_fila += 1

        elif actual == 0 and siguiente == 3:
            # Caso 2: Personaje, meta
            # Inicio [0,3] -> Fin [4,6]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            self.personaje_fila += 1

        elif actual == 0 and siguiente == 1 and despues == 4:
            # Caso 3: Personaje, caja, espacio
            # Inicio [0,1,4] -> Fin [4,0,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila += 1

        elif actual == 0 and siguiente == 1 and despues == 3:
            # Caso 4: Personaje, caja, meta
            # Inicio [0,1,3] -> Fin [4,0,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 5
            self.personaje_fila += 1

        elif actual == 0 and siguiente == 5 and despues == 4:
            # Caso 5: Personaje, caja_meta, espacio
            # Inicio [0,5,4] -> Fin [4,6,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila += 1

        elif actual == 0 and siguiente == 5 and despues == 3:
            # Caso 6: Personaje, caja_meta, meta
            # Inicio [0,5,3] -> Fin [4,6,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 5
            self.personaje_fila += 1

        elif actual == 6 and siguiente == 4:
            # Caso 7: Personaje_meta, espacio
            # Inicio [6,4] -> Fin [3,0]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.personaje_fila += 1

        elif actual == 6 and siguiente == 3:
            # Caso 8: Personaje_meta, meta
            # Inicio [6,3] -> Fin [3,6]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            self.personaje_fila += 1

        elif actual == 6 and siguiente == 1 and despues == 4:
            # Caso 9: Personaje_meta, caja, espacio
            # Inicio [6,1,4] -> Fin [3,0,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila += 1

        elif actual == 6 and siguiente == 1 and despues == 3:
            # Caso 10: Personaje_meta, caja, meta
            # Inicio [6,1,3] -> Fin [3,0,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 5
            self.personaje_fila += 1

        elif actual == 6 and siguiente == 5 and despues == 4:
            # Caso 11: Personaje_meta, caja_meta, espacio
            # Inicio [6,5,4] -> Fin [3,6,1]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila += 1

        elif actual == 6 and siguiente == 5 and despues == 3:
            # Caso 12: Personaje_meta, caja_meta, meta
            # Inicio [6,5,3] -> Fin [3,6,5]
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 5
            self.personaje_fila += 1

        # Cualquier otro caso es un movimiento invalido (pared o caja
        # bloqueada) y no se modifica nada

    def jugar(self) -> None:
        """
            a - Izquierda
            d - Derecha
            w - Arriba
            s - Abajo
        """
        self.imprimirMapa()
        movimiento = input("Movimiento: ")
        if movimiento == "d":
            self.derecha()
            os.system("cls")

        elif movimiento == "a":
            self.izquierda()
            os.system("cls")
        elif movimiento == "w":
            self.arriba()
            os.system("cls")
        elif movimiento == "s":
            self.abajo()
            os.system("cls")
soko = Sokoban()
while True:
    soko.jugar()