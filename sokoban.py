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
            [2,4,0,1,3,4,2],
            [2,4,4,4,4,4,2],
            [2,2,2,2,2,2,2]
        ]

        self.personaje_fila = 2
        self.personaje_columna = 2

        # Nivel que se esta jugando y bandera para terminar el juego
        self.nivel = 1
        self.fin = False

        # Guarda el mapa inicial para poder reiniciar el nivel
        self.mapa_inicial = [fila[:] for fila in self.mapa]

        # Los niveles siguientes estan en archivos de texto junto a este archivo
        self.carpeta = os.path.dirname(os.path.abspath(__file__))

    def imprimirMapa(self) -> None:
        for fila in self.mapa:
            print(fila)

    def buscarPersonaje(self) -> None:
        # Busca la posicion del personaje en el mapa
        for i, fila in enumerate(self.mapa):
            for j, celda in enumerate(fila):
                if celda in [0, 6]:
                    self.personaje_fila = i
                    self.personaje_columna = j

    def cargarNivel(self, numero: int) -> bool:
        # Carga el archivo nivel<numero>.txt, cada linea es una fila del mapa
        # Devuelve False si el archivo no existe
        ruta = os.path.join(self.carpeta, "nivel" + str(numero) + ".txt")
        if not os.path.exists(ruta):
            return False

        mapa = []
        with open(ruta, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    mapa.append([int(celda) for celda in linea])

        self.mapa = mapa
        self.mapa_inicial = [fila[:] for fila in mapa]
        self.nivel = numero
        self.buscarPersonaje()
        return True

    def reiniciar(self) -> None:
        # Vuelve a cargar el nivel que se esta jugando
        self.mapa = [fila[:] for fila in self.mapa_inicial]
        self.buscarPersonaje()

    def caja(self) -> bool:
        # El nivel esta terminado cuando ya no hay cajas fuera de una meta (1)
        # y hay al menos una caja sobre una meta (5)
        terminado = False
        for fila in self.mapa:
            if 1 in fila:
                return False
            if 5 in fila:
                terminado = True
        return terminado

    def siguienteNivel(self) -> None:
        # Carga el siguiente nivel, si ya no hay mas termina el juego
        self.imprimirMapa()
        print("Nivel completado")
        input("Presiona enter para continuar")
        os.system("cls")

        if not self.cargarNivel(self.nivel + 1):
            print("No hay mas niveles")
            self.fin = True

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
            r - Reiniciar
        """
        self.imprimirMapa()
        movimiento = input("Movimiento: ")
        if movimiento == "d":
            self.derecha()
            os.system("clear")

        elif movimiento == "a":
            self.izquierda()
            os.system("clear")
        elif movimiento == "w":
            self.arriba()
            os.system("clear")
        elif movimiento == "s":
            self.abajo()
            os.system("clear")
        elif movimiento == "r":
            self.reiniciar()
            os.system("clear")

        if self.caja():
            self.siguienteNivel()
soko = Sokoban()
while not soko.fin:
    soko.jugar()