import time
import statistics
from main import ej2
from generateData import generar_casos_de_prueba

TIMES_OUTPUT_FILEPATH = "./times.txt"

def test(array_input, output_esperado, numero_de_test):
    print(f"TEST {numero_de_test}:")
    if output_esperado is not None:
        print(f"Cantidad de intervalos esperados: {output_esperado}")
    else:
        print("Test de volumen, no se conoce la cantidad de intervalos esperados.")
    output_obtenido = ej2(array_input)
    print(f"Cantidad de intervalos obtenidos: {output_obtenido}")
    if output_esperado is not None:
        assert output_esperado == output_obtenido
    print(f"TEST OK")
    print("")

def tests():
    times = {}
    numero_de_test = 1

    for array_input, output_esperado in generar_casos_de_prueba():
        start_time = time.time()
        test(array_input, output_esperado, numero_de_test)
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
