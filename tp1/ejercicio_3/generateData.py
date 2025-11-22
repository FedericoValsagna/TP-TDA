import random
from wrapper import ejercicio3

random.seed(3000)

CASOS_POR_TAMANO = 5

casos_base = [
    ([3,-4,2,3,-4, 2,-2,2,4,-3], [2,3,-4, 2,-2,2,4], 7),
    ([4, -4, 2, -1, 4, -2, 5, -4, 2, 4], [4, -4, 2, -1, 4, -2, 5, -4, 2, 4], 10),
    ([-4, -3, -1, -5], [-1], -1),
    ([2, 4, -2, 1, -6, 4], [2, 4], 6),
    ([-3, 2, 4], [2, 4], 6),
    ([2, 4, -7, 0], [2, 4], 6),
    ([-2, -1, 3, 4, -5, 4], [3, 4], 7),
    ([2,2,2,2], [2,2,2,2], 8),
    ([2, 3, -5, 7], [2, 3, -5, 7], 7),
    ([-2, 10, -5, -3, -1], [10], 10),
    ([-5, -2, 3, 4, 5, -3, -6], [3, 4, 5], 12),
    ([1, 3, 2, 4, 1], [1, 3, 2, 4, 1], 11)
]

tamanos = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1_000]

def generar_arreglo_aleatorio(tamano):
    return [random.randint(-10, 10) for _ in range(tamano)]

def generar_casos_de_prueba():
    for caso in casos_base:
        yield caso

    for tamano in tamanos:
        for _ in range(CASOS_POR_TAMANO):
            arreglo = generar_arreglo_aleatorio(tamano)
            subarreglo, suma_maxima = ejercicio3(arreglo)
            yield (arreglo, subarreglo, suma_maxima)
