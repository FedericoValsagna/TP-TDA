from ej1 import ej1_wrapper
FILEPATH = "./tests.txt"


def test(array_input, output_esperado, numero_de_test):
    print(f"TEST {numero_de_test}:")
    print(f"Arreglo: {array_input}")
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
    line.replace(" ", "")
    items = line.split("/")
    input = list(map(parse_item, items))
    input_inicial, output_esperado = input[0], input[1]
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