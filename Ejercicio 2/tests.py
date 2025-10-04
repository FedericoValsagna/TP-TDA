from ej2 import ej2
FILEPATH = "./tests.txt"


def test(array_input, output_esperado, numero_de_test):
    print(f"TEST {numero_de_test}:")
    print(f"Arreglo: {array_input}")
    print(f"Cantidad de intervalos esperados: {output_esperado}")
    output_obtenido = ej2(array_input)
    print(f"Cantidad de intervalos obtenidos: {output_obtenido}")
    assert output_esperado == output_obtenido
    print(f"TEST OK")
    print("")


def parse_item(item):
    item = item.split(",")
    item = list(map(int, item))
    return item

def parse_test(line):
    line.replace(" ", "")
    items = line.split("/")
    input_inicial = parse_item(items[0])
    output_esperado = int(items[1])
    return input_inicial, output_esperado

def tests():
    with open(FILEPATH) as file:
        numero_de_test = 1
        for line in file:
            if len(line) < 2:
                continue
            array_input, output_esperado = parse_test(line)
            test(array_input, output_esperado, numero_de_test)
            numero_de_test += 1


tests()