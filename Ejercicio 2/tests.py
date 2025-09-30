from ej2 import ej2
FILEPATH = "./tests.txt"


def test(array_input, output_esperado, numero_de_test):
    print(f"TEST {numero_de_test}:")
    print(f"Arreglo: {array_input}")
    print(f"Subarreglos esperados: {output_esperado}")
    output_obtenido = ej2(array_input)
    print(f"Subarreglos obtenidos: {output_obtenido}")
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
    input = list(map(parse_item, items))
    input_inicial, output_esperado = input[0], input[1:]
    return input_inicial, output_esperado
       

def read_file():
    with open(FILEPATH) as file:
            numero_de_test = 1
            for line in file:
                  array_input, output_esperado = parse_test(line)

                  test(array_input, output_esperado, numero_de_test)
                  numero_de_test += 1

def tests():
    #test([3,-5, 7, -4, 1, -8, 3, -7, 5, -9, 5, -2, 4], [[3, -5, 7, -4, 1], [3, -7, 5], [5, -2, 4]], 1)
    read_file()

tests()