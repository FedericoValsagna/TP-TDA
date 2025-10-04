from wrapper import ejercicio3
import math
FILEPATH = "tests.txt"



def test(array_input, subarray_esperado, suma_maxima_esperada, numero_de_test):
    print(f"TEST {numero_de_test}:")
    print(f"Arreglo: {array_input}")
    print(f"Suma Máxima esperada: {suma_maxima_esperada}: {subarray_esperado}")
    subarray_obtenido, suma_maxima_obtenida = ejercicio3(array_input)
    print(f"Suma Máxima obtenida {suma_maxima_obtenida}: {subarray_obtenido}")
    assert suma_maxima_esperada == suma_maxima_obtenida
    assert subarray_esperado == subarray_obtenido
    print(f"TEST OK")
    print("")


def parse_item(item):
    item = item.split(",")
    item = list(map(int, item))
    return item

def parse_test(line):
    line.replace(" ", "")
    items = line.split("/")
    input_inicial, subarray_esperado, suma_maxima_esperada = parse_item(items[0]), parse_item(items[1]), int(items[2])
    return input_inicial, subarray_esperado, suma_maxima_esperada

def tests():
    with open(FILEPATH) as file:
        numero_de_test = 1
        for line in file:
            if len(line) < 2:
                continue
            array_input, subarray_esperado, suma_maxima_esperada = parse_test(line)
            test(array_input, subarray_esperado, suma_maxima_esperada, numero_de_test)
            numero_de_test += 1


tests()