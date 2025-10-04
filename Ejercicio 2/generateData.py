import random
from main import ej2

random.seed(3000)

CASOS_POR_TAMANO = 3

casos_base = [
    ([10, -5, 2, -1, 5], 1),
    ([3, -5, 7, -3, 1, -8, 3, -7, 5, -9, 5, -2, 4], 3),
    ([5, -8, 4, -3], 1),
    ([-10, -20, 5, 5, 5], 1),
    ([10, -5, 10, -5, 10, -25, 1, 1], 2),
    ([-1, -2, -3, -4, -5], 0)
]

tamanos = [1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000]

def generar_arreglo_aleatorio(tamano):
    return [random.randint(-10, 10) for _ in range(tamano)]

def generar_casos_de_prueba():
    for caso in casos_base:
        yield caso

    for tamano in tamanos:
        for _ in range(CASOS_POR_TAMANO):
            arreglo = generar_arreglo_aleatorio(tamano)
            resultado_esperado = ej2(arreglo)
            yield (arreglo, resultado_esperado)
