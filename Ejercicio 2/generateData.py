import random

random.seed(2500)

CASOS_POR_TAMANO = 6

casos_base = [
    ([10, -5, 2, -1, 5], 1),
    ([3, -5, 7, -3, 1, -8, 3, -7, 5, -9, 5, -2, 4], 3),
    ([5, -8, 4, -3], 1),
    ([-10, -20, 5, 5, 5], 1),
    ([10, -5, 10, -5, 10, -25, 1, 1], 2),
    ([-1, -2, -3, -4, -5], 0)
]

tamanos = [250_000, 500_000, 750_000, 1_000_000, 1_250_000, 1_500_000, 1_750_000, 2_000_000]

def generar_arreglo_aleatorio(tamano, numero_test):
    random_local = random.Random(2500 + numero_test)
    return [random_local.randint(-100, 100) for _ in range(tamano)]

def generar_casos_de_prueba():
    for caso in casos_base:
        yield caso

    numero_test = 0
    for tamano in tamanos:
        for _ in range(CASOS_POR_TAMANO):
            arreglo = generar_arreglo_aleatorio(tamano, numero_test)
            resultado_esperado = None
            yield (arreglo, resultado_esperado)
            numero_test += 1
