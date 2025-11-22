import time
import statistics
from main import ej4
from generateData import generar_casos_de_prueba

TIMES_OUTPUT_FILEPATH = "./times.txt"

def test(array_input, subarray_esperado, suma_maxima_esperada, numero_de_test):
    print(f"TEST {numero_de_test}:")
    print(f"Suma Máxima esperada: {suma_maxima_esperada}")
    subarray_obtenido, suma_maxima_obtenida = ej4(array_input)
    print(f"Suma Máxima obtenida {suma_maxima_obtenida}")
    assert suma_maxima_esperada == suma_maxima_obtenida
    assert subarray_esperado == subarray_obtenido
    print(f"TEST OK")
    print("")

def tests():
    times = {}
    numero_de_test = 1

    for array_input, subarray_esperado, suma_maxima_esperada in generar_casos_de_prueba():
        start_time = time.time()
        test(array_input, subarray_esperado, suma_maxima_esperada, numero_de_test)
        end_time = time.time()

        tamano = len(array_input)
        if tamano not in times:
            times[tamano] = []
        times[tamano].append(end_time - start_time)
        numero_de_test += 1

    with open(TIMES_OUTPUT_FILEPATH, 'w') as file:
        for tamaño, tiempos in times.items():
            mediana = statistics.median(tiempos)
            file.write(f"{tamaño} {mediana}\n")

tests()