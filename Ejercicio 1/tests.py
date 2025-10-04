import time
from main import ej1_wrapper
from generateData import generar_casos_de_prueba

TEST_FILEPATH = "./tests.txt"
TIMES_OUTPUT_FILEPATH = "./times.txt"

def test(array_input, output_esperado, numero_de_test):
    print(f"TEST {numero_de_test}:")
    print(f"Indice esperado: {output_esperado}")
    output_obtenido = ej1_wrapper(array_input)
    print(f"Indice obtenido: {output_obtenido}")
    assert output_esperado == output_obtenido
    print(f"TEST OK")
    print("")


def parse_item(item):
    item = item.split(",")
    if len(item) > 1:
        item = list(map(int, item))
    else:
        item = int(item[0])
    return item

def parse_test(line):
    line = line.replace(" ", "")
    items = line.split("/")
    input_inicial = parse_item(items[0])
    output_esperado = int(items[1])
    return input_inicial, output_esperado

def tests():
    generar_casos_de_prueba(TEST_FILEPATH)
    times = {} ## Key: tamaño, Value: time
    with open(TEST_FILEPATH) as file:
        numero_de_test = 1
        for line in file:
            if len(line) < 2:
                continue
            array_input, output_esperado = parse_test(line)
            start_time = time.time()
            test(array_input, output_esperado, numero_de_test)
            end_time = time.time()
            times[len(array_input)] = end_time - start_time
            numero_de_test += 1
    
    with open(TIMES_OUTPUT_FILEPATH, 'w') as file:
        for tamaño, tiempo in times.items():
            file.write(f"{tamaño} {tiempo}\n")

tests()