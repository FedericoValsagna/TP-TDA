import random
import os
from ej4 import ej4

random.seed(2025)

casos_base = [
    "3,-4,2,3,-4, 2,-2,2,4,-3 / 2,3,-4, 2,-2,2,4 / 7",
    "4, -4, 2, -1, 4, -2, 5, -4, 2, 4 / 2, -1, 4, -2, 5, -4, 2, 4 / 10",
    "-4, -3, -1, -5 / -1 / -1",
    "2, 4, -2, 1, -6, 4 / 2, 4 / 6",
    "-3, 2, 4 / 2, 4 / 6",
    "2, 4, -7, 0 / 2, 4 / 6",
    "-2, -1, 3, 4, -5 , 4 / 3, 4 / 7",
    "2,2,2,2 / 2,2,2,2 / 8",
    "2, 3, -5, 7 / 7 / 7"
]

def generar_arreglo_aleatorio(tamano):
    arreglo = []
    for _ in range(tamano):
        arreglo.append(random.randint(-10, 10))
    return arreglo

def generar_arreglos_de_prueba():
    casos_de_prueba = casos_base.copy()
    tamanos = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000, 500_000, 1_000_000, 1_500_000, 2_000_000]

    for tamano in tamanos:
        arreglo = generar_arreglo_aleatorio(tamano)
        subarreglo, suma_maxima = ej4(arreglo)
        caso_de_prueba = f"{', '.join(map(str, arreglo))} / {', '.join(map(str, subarreglo))} / {suma_maxima}"
        casos_de_prueba.append(caso_de_prueba)

    return casos_de_prueba

def escribir_archivo_de_prueba(test_cases, filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, 'w') as f:
        for test_case in test_cases:
            f.write(test_case + '\n')

    print(f"Total casos de prueba generados: {len(test_cases)}")


def generar_casos_de_prueba(filename="tests.txt"):
    if os.path.exists(filename):
        print(f"El archivo {filename} ya existe, en caso de querer generar nuevos casos, elimine el archivo")
        return
    test_cases = generar_arreglos_de_prueba()
    escribir_archivo_de_prueba(test_cases, filename)

if __name__ == "__main__":
    generar_casos_de_prueba()
