import time
from ej4 import ej4
from generateData import generar_casos_de_prueba

TEST_FILEPATH = "./tests.txt"
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


def parse_item(item):
    item = item.split(",")
    item = list(map(int, item))
    return item

def parse_test(line):
    line = line.replace(" ", "")
    items = line.split("/")
    input_inicial, subarray_esperado, suma_maxima_esperada = parse_item(items[0]), parse_item(items[1]), int(items[2])
    return input_inicial, subarray_esperado, suma_maxima_esperada

def tests():
    generar_casos_de_prueba(TEST_FILEPATH)
    times = {}
    with open(TEST_FILEPATH) as file:
        numero_de_test = 1
        for line in file:
            if len(line) < 2:
                continue
            array_input, subarray_esperado, suma_maxima_esperada = parse_test(line)
            start_time = time.time()
            test(array_input, subarray_esperado, suma_maxima_esperada, numero_de_test)
            end_time = time.time()
            times[len(array_input)] = end_time - start_time
            numero_de_test += 1

    with open(TIMES_OUTPUT_FILEPATH, 'w') as file:
        for tamaño, tiempo in times.items():
            file.write(f"{tamaño} {tiempo}\n")

tests()