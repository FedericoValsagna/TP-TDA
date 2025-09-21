import math

# Datos del problema
numeros = [2, -3, 5, -1, 4]
A = len(numeros)
suma_maxima = {'suma': -math.inf, 'estado': None}

# Funciones auxiliares para manipular los estados
def obtener_posicion_del_uno(estado):
    try:
        return estado.index(1)
    except ValueError:
        return -1

def calcular_suma_estado(estado):
    suma = 0
    for i in range(len(estado)):
        if estado[i] == 1:
            suma += numeros[i]
    return suma

def agregar_un_uno_a_la_derecha(estado):
    # Encuentra el último 1, y si es posible, agrega otro 1 a su derecha.
    # Si no hay 1s, se asume que se está en el estado inicial de [1, 0, 0, ...].
    try:
        ultima_posicion_uno = [i for i, val in enumerate(estado) if val == 1][-1]
    except IndexError:
        ultima_posicion_uno = -1

    if ultima_posicion_uno + 1 < A:
        nuevo_estado = list(estado)
        nuevo_estado[ultima_posicion_uno + 1] = 1
        return nuevo_estado
    else:
        return -1

# Los estados son cada posición de un array indicando con 1 si se incluye y con 0 si no se incluye.
def tomar_decision(estado):
    suma = calcular_suma_estado(estado)
    if suma > suma_maxima['suma']:
      suma_maxima['estado'] = estado
      suma_maxima['suma'] = suma

# En cada iteración de backtracking, recibe un array con un 1 y todos ceros,
# y se van agregando unos a la derecha, eso nos asegura que los 1 a la izquierda
# ya se probaron en iteraciones anteriores.
def deshacer_decision(posicion_uno):
    if posicion_uno + 1 < A:
        nuevo_estado = [0] * A
        nuevo_estado[posicion_uno + 1] = 1
        return nuevo_estado
    return None # terminé de recorrer los números


def resolver_con_backtracking(estado_actual):
    # 1. Caso Base: Si el estado actual es una solución, terminamos.
    if estado_actual is None: # no me quedan más estados por probar
        return suma_maxima

    # 2. Iterar sobre las opciones para cada opción en las opciones
    # posibles desde estado_actual:
    posicion_uno = obtener_posicion_del_uno(estado_actual)
    tomar_decision(estado_actual)

    # Mientras se pueda agregar un uno a la derecha
    estado_actual = agregar_un_uno_a_la_derecha(estado_actual)
    while estado_actual != -1:
        # 3. Tomar una decision (intentar una opción)
        tomar_decision(estado_actual)
        estado_actual = agregar_un_uno_a_la_derecha(estado_actual)

    # 5. Retroceder (deshacer la decisión)
    estado_nuevo = deshacer_decision(posicion_uno)

    # 6. Llamada recursiva
    return resolver_con_backtracking(estado_nuevo)

# main: ojo hay datos arriba
estado_inicial = [0] * A
if A > 0:
    estado_inicial[0] = 1
else:
    exit("El array de números no puede estar vacío.")

resultado = resolver_con_backtracking(estado_inicial)
print(f"La suma máxima es: {resultado['suma']}")
print(f"El estado (secuencia contigua) que la produce es: {resultado['estado']}")