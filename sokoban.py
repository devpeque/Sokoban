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
            [2,4,4,0,3,4,2], 
            [2,4,4,4,4,4,2],
            [2,2,2,2,2,2,2]
        ]

        self.personaje_fila = 2
        self.personaje_columna = 3

    def imprimirMapa(self) -> None:
        for fila in self.mapa:
            print(fila)

    def personajemeta(self) -> None:
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and
            self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3
        ):
            # Coloca camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca personaje_meta donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            # Actualiza la posición del personaje
            self.personaje_columna += 1

    def derecha(self) -> None:
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] in [0,6]
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] in [3,4]
        ):
                # Si estaba sobre una meta
            if self.mapa[self.personaje_fila][self.personaje_columna] == 6:
                self.mapa[self.personaje_fila][self.personaje_columna] = 3
            else:
                self.mapa[self.personaje_fila][self.personaje_columna] = 4

            # Si entra a una meta
            if self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3:
                self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            else:
                self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            #Actualiza la posicion del personaje
            self.personaje_columna += 1

    def izquierda(self) -> None:
            if (
                        self.mapa[self.personaje_fila][self.personaje_columna] in [0,6]
                        and self.mapa[self.personaje_fila][self.personaje_columna - 1] in [3,4]
                    ):
                            # Si estaba sobre una meta
                        if self.mapa[self.personaje_fila][self.personaje_columna] == 6:
                            self.mapa[self.personaje_fila][self.personaje_columna] = 3
                        else:
                            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            
                        # Si entra a una meta
                        if self.mapa[self.personaje_fila][self.personaje_columna - 1] == 3:
                            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
                        else:
                            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
                        #Actualiza la posicion del personaje
                        self.personaje_columna -= 1  

    def arriba(self)->None:
        if (   self.mapa[self.personaje_fila][self.personaje_columna] == 0
                    and self.mapa[self.personaje_fila - 1][self.personaje_columna]==4
                ):
                    #Coloca un camino donde estaba el personaje
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    #Coloca el personaje donde estaba el camino
                    self.mapa[self.personaje_fila - 1 ][self.personaje_columna ] = 0
                    #Actualiza la posicion del personaje
                    self.personaje_fila -= 1

    def abajo(self) -> None:
         if (
                        self.mapa[self.personaje_fila][self.personaje_columna] == 0
                        and self.mapa[self.personaje_fila + 1][self.personaje_columna ]==4
                    ):
                        #Coloca un camino donde estaba el personaje
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        #Coloca el personaje donde estaba el camino
                        self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 0
                        #Actualiza la nueva posicion del personaje
                        self.personaje_fila += 1 
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
        elif movimiento == "a":
            self.izquierda()
        elif movimiento == "w":
            self.arriba()
        elif movimiento == "s":
            self.abajo()


soko = Sokoban()
while True:
    soko.jugar()