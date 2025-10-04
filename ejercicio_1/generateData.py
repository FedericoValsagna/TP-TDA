import random
from main import ej1_wrapper

random.seed(2000)

CASOS_POR_TAMANO = 5

casos_base = [
    ([-1,0,1,3,4], 3),
    ([0,1,2,3,4,5], 2),
    ([-4,2,3,4,5], -1),
    ([-1,0,1,3], 3),
    ([0,1,3,4], 1),
    ([-4,2,3,4], -1),
    ([0,2,3,4,5,6], 0),
    ([0,2,3,4,5], 0),
    ([-1,0,1,2,4], 4),
    ([-1,0,1,2,3,5], 5)
]

tamanos = [25_000_000, 50_000_000, 75_000_000, 100_000_000, 125_000_000, 150_000_000, 175_000_000, 200_000_000]

def generar_arreglo_ordenado(tamano):
    valor_inicial = random.randint(-tamano, tamano)
    return list(range(valor_inicial, valor_inicial + tamano))

def generar_casos_de_prueba():
    for caso in casos_base:
        yield caso

    for tamano in tamanos:
        for _ in range(CASOS_POR_TAMANO):
            arreglo = generar_arreglo_ordenado(tamano)
            resultado_esperado = ej1_wrapper(arreglo)
            yield (arreglo, resultado_esperado)
