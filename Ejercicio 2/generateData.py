import random
import os
from main import ej2

random.seed(2025)

casos_base = [
    "10, -5, 2, -1, 5 / 1",
    "3, -5, 7, -3, 1, -8, 3, -7, 5, -9, 5, -2, 4 / 3",
    "5, -8, 4, -3 / 1",
    "-10, -20, 5, 5, 5/ 1",
    "10, -5, 10, -5, 10, -25, 1, 1 / 2",
    "-1, -2, -3, -4, -5 / 0",
    #"4, -100, 100, -4, -2, 1, -8, 1, -1, 2 / 2"
]

def generar_arreglo_aleatorio(tamano):
    arreglo = []
    for _ in range(tamano):
        arreglo.append(random.randint(-10, 10))
    return arreglo

def generar_arreglos_de_prueba():
    casos_de_prueba = casos_base.copy()
    tamanos = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000]

    for tamano in tamanos:
        arreglo = generar_arreglo_aleatorio(tamano)
        resultado_esperado = ej2(arreglo)
        caso_de_prueba = f"{', '.join(map(str, arreglo))} / {resultado_esperado}"
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
