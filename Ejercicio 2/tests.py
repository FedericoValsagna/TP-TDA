from ej2 import ej2

def test(array_input, output_esperado, numero_de_test):
    output_obtenido = ej2(array_input)
    assert output_esperado == output_obtenido
    print(f"TEST {numero_de_test} OK")


def tests():
    test([3,-5, 7, -4, 1, -8, 3, -7, 5, -9, 5, -2, 4], [[3, -5, 7, -4, 1], [3, -7, 5], [5, -2, 4]], 1)

tests()