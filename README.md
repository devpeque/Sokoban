# SOKOBAN

## 1. Objetivo

### 1.1 General

Programar el juego Sokoban en una versión retro para consola, utilizando Python y programación orientada a objetos.

### 1.2 Específicos

- Aplicar los conocimientos básicos de programación orientada a objetos con Python (clases, objetos, métodos, variables, arreglos, bucles, lectura desde teclado, decisiones, etc.).
- Utilizar ingeniería de software para analizar, diseñar y desarrollar el juego.
- Utilizar Kanban para dar seguimiento a las actividades a realizar: ToDo, Doing y Done.
- Utilizar hitos (Milestones) para cada una de las etapas del desarrollo.
- Documentar el código generado.
- Implementar el movimiento del personaje y el desplazamiento de cajas sobre el mapa.
- Permitir la carga de niveles desde archivos de texto independientes.
- Implementar la opción de reiniciar el nivel actual.
- Detectar la finalización de un nivel para intentar cargar el siguiente.

## 2. Reglas del juego

El juego Sokoban consiste en recorrer un mapa en forma de laberinto para empujar cajas que están repartidas en el mapa hacia puntos determinados por las metas.

Las reglas son las siguientes:

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar una caja a la vez hacia arriba, abajo, izquierda o derecha.
3. El personaje se moverá dentro de un mapa predefinido.
4. Para terminar un nivel, todas las cajas deben estar acomodadas sobre las metas.
5. El nivel de dificultad no está determinado necesariamente por la cantidad de cajas y metas.
6. El personaje no puede atravesar paredes.
7. Una caja no puede moverse si la posición siguiente está ocupada por una pared u otra caja.
8. Cuando el personaje se encuentra sobre una meta, el mapa debe conservar esa información.
9. El usuario puede reiniciar el nivel actual mediante la tecla `r`.
10. Los niveles se pueden cargar desde archivos de texto independientes.

## 3. Elementos del juego

Sokoban tiene dos partes principales: el mapa donde se va a jugar y los elementos que lo componen (personaje, cajas, metas, paredes y camino).

### 3.1 Mapa de juego

Cada nivel se representa mediante un arreglo bidimensional de Python. Cada posición contiene un número que representa un elemento del juego.

El mapa inicial definido en el constructor de la clase `Sokoban` es el siguiente:

```python
self.mapa = [
    [2,2,2,2,2,2,2],
    [2,4,4,4,4,4,2],
    [2,4,0,1,3,4,2],
    [2,4,4,4,4,4,2],
    [2,2,2,2,2,2,2]
]

self.personaje_fila = 2
self.personaje_columna = 2
```

En este mapa, el personaje se encuentra en la fila 2 y la columna 2. A su derecha hay una caja y, después de la caja, una meta.

La clase también guarda una copia del mapa inicial para permitir que el usuario reinicie el nivel sin perder su configuración original.

```python
self.mapa_inicial = [fila[:] for fila in self.mapa]
```

La expresión crea una copia independiente de cada fila del mapa. De esta manera, los movimientos realizados durante la partida no modifican la copia utilizada para reiniciar.

### 3.2 Lista de elementos

Para esta versión de Sokoban se utilizan números para representar los elementos del juego.

```python
"personaje": 0,
"caja": 1,
"pared": 2,
"meta": 3,
"camino": 4,
"caja_meta": 5,
"personaje_meta": 6
```

| Número | Interpretación |
| --- | --- |
| 0 | Personaje |
| 1 | Caja |
| 2 | Pared |
| 3 | Meta |
| 4 | Camino |
| 5 | Caja sobre una meta |
| 6 | Personaje sobre una meta |

El número 5 representa una caja colocada sobre una meta. El número 6 representa al personaje cuando ocupa una posición que contiene una meta.

Estos valores permiten conservar la información de las metas cuando una caja o el personaje se encuentran sobre ellas.

### 3.3 Variables principales de la clase

La clase `Sokoban` utiliza las siguientes variables para administrar el juego:

| Variable | Descripción |
| --- | --- |
| `mapa` | Matriz que representa el estado actual del nivel. |
| `personaje_fila` | Fila en la que se encuentra el personaje. |
| `personaje_columna` | Columna en la que se encuentra el personaje. |
| `nivel` | Número del nivel que se está jugando. |
| `fin` | Bandera que indica si el ciclo principal del juego debe terminar. |
| `mapa_inicial` | Copia del mapa utilizada para reiniciar el nivel. |
| `carpeta` | Ruta del directorio donde se encuentran los archivos de los niveles. |

## 4. Controles

Para moverse en el juego, el usuario utiliza las siguientes letras en minúscula:

| Letra | Dirección del movimiento | Método |
| --- | --- | --- |
| `a` | Izquierda | `izquierda()` |
| `d` | Derecha | `derecha()` |
| `w` | Arriba | `arriba()` |
| `s` | Abajo | `abajo()` |
| `r` | Reiniciar nivel | `reiniciar()` |

Después de escribir una letra, el usuario presiona Enter para ejecutar la acción.

Si el movimiento no es válido, por ejemplo, porque hay una pared o una caja bloqueada, el mapa permanece sin cambios.

## 5. Modo de juego

El juego muestra el mapa actual y solicita al usuario que escriba la letra correspondiente al movimiento que desea realizar.

El método `jugar()` controla la entrada del usuario y llama al método correspondiente según la tecla introducida.

El funcionamiento general es el siguiente:

1. Mostrar el mapa mediante `imprimirMapa()`.
2. Leer el movimiento con `input("Movimiento: ")`.
3. Identificar la tecla introducida.
4. Ejecutar el método correspondiente a la dirección elegida o reiniciar el nivel.
5. Limpiar la pantalla después de las acciones de movimiento o reinicio.
6. Comprobar si se cumple la condición de finalización del nivel mediante `caja()`.
7. Si se cumple la condición, ejecutar `siguienteNivel()`.
8. Repetir el proceso mientras la variable `fin` sea `False`.

El ciclo principal del programa se encuentra fuera de la clase:

```python
soko = Sokoban()

while not soko.fin:
    soko.jugar()
```

La variable `fin` permite controlar la ejecución del juego. Cuando no existe otro nivel disponible, `siguienteNivel()` cambia su valor a `True`, lo que provoca que el ciclo principal termine.

## 6. Funciones a implementar

Después de realizar un análisis del juego Sokoban se identifican las funciones necesarias para completarlo. A continuación, se presenta una tabla con la lista de estas funciones para llevar un mejor control sobre el avance del desarrollo del juego.

Para llevar un mejor control del avance del desarrollo se utiliza la metodología Kanban, indicando en qué estatus se encuentra cada función del juego.

| Valor | Interpretación |
| --- | --- |
| ToDo | Por hacer |
| Doing | Programando y validando |
| Done | Programada y validada con éxito |

### Seguimiento del avance

Estado actual de cada función según el código:

| No. | Función | Kanban | Método |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | Done | `cargarNivel()` y `siguienteNivel()` |
| 1. | Repetir el juego hasta terminar el nivel. | Done | `jugar()` dentro de `while not soko.fin` |
| 2. | Imprimir mapa. | Done | `imprimirMapa()` |
| 3. | Leer el movimiento. | Done | `jugar()` |
| 4. | Evaluar el movimiento del usuario. | Done | `jugar()` |
| 5. | Movimiento a la derecha (12 casos). | Done | `derecha()` |
| 6. | Movimiento a la izquierda (12 casos). | Done | `izquierda()` |
| 7. | Movimiento hacia arriba (12 casos). | Done | `arriba()` |
| 8. | Movimiento hacia abajo (12 casos). | Done | `abajo()` |
| 9. | Evaluar si el nivel está terminado. | Doing | `caja()` |
| 10. | Reiniciar el mapa con la letra `r`. | Done | `reiniciar()` |

### 6.1 Funciones generales

| No. | Función | Kanban | Método |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | Done | `cargarNivel()` y `siguienteNivel()` |
| 1. | Repetir el juego hasta terminar el nivel. | Done | `jugar()` dentro de `while not soko.fin` |
| 2. | Imprimir mapa. | Done | `imprimirMapa()` |
| 3. | Leer el movimiento. | Done | `jugar()` con `input("Movimiento: ")` |
| 4. | Evaluar el movimiento del usuario. | Done | `jugar()` con `if/elif` hacia `derecha()`, `izquierda()`, `arriba()`, `abajo()` y `reiniciar()` |

El ciclo principal del juego ya se encuentra implementado. Se repite mientras la variable `fin` sea `False`. Cuando no existe un siguiente nivel, el método `siguienteNivel()` cambia `fin` a `True` para terminar el programa.

### 6.2 Derecha

Implementado en `derecha()`. El método obtiene tres celdas mediante `obtener(fila, columna)`: `actual`, `siguiente` y `despues`. Esta última corresponde a la celda situada después de una posible caja.

Cada caso de la tabla se implementa mediante una condición `if/elif` que compara los valores de las celdas y modifica el mapa cuando el movimiento es válido.

En todos los casos, las posiciones se actualizan en el orden en que avanza el personaje. Si el movimiento no coincide con ninguno de los 12 casos, por ejemplo, porque existe una pared o una caja bloqueada, el mapa no se modifica.

El método `obtener()` devuelve `2` (pared) cuando la posición queda fuera del mapa, evitando movimientos fuera de los límites del arreglo.

| No. | Función | Kanban | Inicio | Fin |
| --- | --- | --- | --- | --- |
| 1. | Personaje, espacio | Done | `[0,4]` | `[4,0]` |
| 2. | Personaje, meta | Done | `[0,3]` | `[4,6]` |
| 3. | Personaje, caja, espacio | Done | `[0,1,4]` | `[4,0,1]` |
| 4. | Personaje, caja, meta | Done | `[0,1,3]` | `[4,0,5]` |
| 5. | Personaje, caja_meta, espacio | Done | `[0,5,4]` | `[4,6,1]` |
| 6. | Personaje, caja_meta, meta | Done | `[0,5,3]` | `[4,6,5]` |
| 7. | Personaje_meta, espacio | Done | `[6,4]` | `[3,0]` |
| 8. | Personaje_meta, meta | Done | `[6,3]` | `[3,6]` |
| 9. | Personaje_meta, caja, espacio | Done | `[6,1,4]` | `[3,0,1]` |
| 10. | Personaje_meta, caja, meta | Done | `[6,1,3]` | `[3,0,5]` |
| 11. | Personaje_meta, caja_meta, espacio | Done | `[6,5,4]` | `[3,6,1]` |
| 12. | Personaje_meta, caja_meta, meta | Done | `[6,5,3]` | `[3,6,5]` |

### 6.3 Izquierda

Implementado en `izquierda()`. Los casos son los mismos que en 6.2, aplicados al movimiento hacia la izquierda. Para esta dirección, las columnas disminuyen en uno y, cuando hay una caja, se consulta también la posición situada dos columnas a la izquierda.

| No. | Función | Kanban | Inicio | Fin |
| --- | --- | --- | --- | --- |
| 1. | Personaje, espacio | Done | `[0,4]` | `[4,0]` |
| 2. | Personaje, meta | Done | `[0,3]` | `[4,6]` |
| 3. | Personaje, caja, espacio | Done | `[0,1,4]` | `[4,0,1]` |
| 4. | Personaje, caja, meta | Done | `[0,1,3]` | `[4,0,5]` |
| 5. | Personaje, caja_meta, espacio | Done | `[0,5,4]` | `[4,6,1]` |
| 6. | Personaje, caja_meta, meta | Done | `[0,5,3]` | `[4,6,5]` |
| 7. | Personaje_meta, espacio | Done | `[6,4]` | `[3,0]` |
| 8. | Personaje_meta, meta | Done | `[6,3]` | `[3,6]` |
| 9. | Personaje_meta, caja, espacio | Done | `[6,1,4]` | `[3,0,1]` |
| 10. | Personaje_meta, caja, meta | Done | `[6,1,3]` | `[3,0,5]` |
| 11. | Personaje_meta, caja_meta, espacio | Done | `[6,5,4]` | `[3,6,1]` |
| 12. | Personaje_meta, caja_meta, meta | Done | `[6,5,3]` | `[3,6,5]` |

### 6.4 Arriba

Implementado en `arriba()`. Los casos son los mismos que en 6.2, aplicados al movimiento hacia arriba. Para esta dirección, las filas disminuyen en uno y, cuando hay una caja, se consulta también la posición situada dos filas arriba.

| No. | Función | Kanban | Inicio | Fin |
| --- | --- | --- | --- | --- |
| 1. | Personaje, espacio | Done | `[0,4]` | `[4,0]` |
| 2. | Personaje, meta | Done | `[0,3]` | `[4,6]` |
| 3. | Personaje, caja, espacio | Done | `[0,1,4]` | `[4,0,1]` |
| 4. | Personaje, caja, meta | Done | `[0,1,3]` | `[4,0,5]` |
| 5. | Personaje, caja_meta, espacio | Done | `[0,5,4]` | `[4,6,1]` |
| 6. | Personaje, caja_meta, meta | Done | `[0,5,3]` | `[4,6,5]` |
| 7. | Personaje_meta, espacio | Done | `[6,4]` | `[3,0]` |
| 8. | Personaje_meta, meta | Done | `[6,3]` | `[3,6]` |
| 9. | Personaje_meta, caja, espacio | Done | `[6,1,4]` | `[3,0,1]` |
| 10. | Personaje_meta, caja, meta | Done | `[6,1,3]` | `[3,0,5]` |
| 11. | Personaje_meta, caja_meta, espacio | Done | `[6,5,4]` | `[3,6,1]` |
| 12. | Personaje_meta, caja_meta, meta | Done | `[6,5,3]` | `[3,6,5]` |

### 6.5 Abajo

Implementado en `abajo()`. Los casos son los mismos que en 6.2, aplicados al movimiento hacia abajo. Para esta dirección, las filas aumentan en uno y, cuando hay una caja, se consulta también la posición situada dos filas abajo.

| No. | Función | Kanban | Inicio | Fin |
| --- | --- | --- | --- | --- |
| 1. | Personaje, espacio | Done | `[0,4]` | `[4,0]` |
| 2. | Personaje, meta | Done | `[0,3]` | `[4,6]` |
| 3. | Personaje, caja, espacio | Done | `[0,1,4]` | `[4,0,1]` |
| 4. | Personaje, caja, meta | Done | `[0,1,3]` | `[4,0,5]` |
| 5. | Personaje, caja_meta, espacio | Done | `[0,5,4]` | `[4,6,1]` |
| 6. | Personaje, caja_meta, meta | Done | `[0,5,3]` | `[4,6,5]` |
| 7. | Personaje_meta, espacio | Done | `[6,4]` | `[3,0]` |
| 8. | Personaje_meta, meta | Done | `[6,3]` | `[3,6]` |
| 9. | Personaje_meta, caja, espacio | Done | `[6,1,4]` | `[3,0,1]` |
| 10. | Personaje_meta, caja, meta | Done | `[6,1,3]` | `[3,0,5]` |
| 11. | Personaje_meta, caja_meta, espacio | Done | `[6,5,4]` | `[3,6,1]` |
| 12. | Personaje_meta, caja_meta, meta | Done | `[6,5,3]` | `[3,6,5]` |

### 6.6 Determina si se completó el nivel

Esta función determina si se cumple la condición de finalización del nivel. Cuando se cumple, se intenta cargar el siguiente nivel.

El método `caja()` ya está implementado. Recorre el mapa y comprueba que no existan cajas con valor `1` y que exista al menos una caja sobre una meta, representada por el valor `5`.

```python
def caja(self) -> bool:
    terminado = False

    for fila in self.mapa:
        if 1 in fila:
            return False

        if 5 in fila:
            terminado = True

    return terminado
```

Cuando el método devuelve `True`, `jugar()` llama a `siguienteNivel()`. Este método muestra el mapa completado, solicita que se presione Enter y carga el archivo correspondiente al siguiente nivel.

Si no existe el archivo del siguiente nivel, se muestra el mensaje `"No hay mas niveles"` y se establece `self.fin = True`, finalizando el ciclo principal del juego.

| No. | Función | Kanban |
| --- | --- | --- |
| 1. | Evaluar si el nivel está terminado y, si se cumple la condición, cargar el siguiente nivel desde un archivo de texto independiente. | Doing |
| 2. | Reiniciar el mapa con la letra `r`, volviendo a cargar el nivel que se está jugando. | Done |

La carga del siguiente nivel y el reinicio ya están implementados. La función de finalización se mantiene en **Doing** porque la condición actual no verifica que todas las metas estén cubiertas; únicamente comprueba que no queden cajas fuera de las metas y que haya al menos una caja sobre una meta.
