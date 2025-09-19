from ej1 import ej1_wrapper, medio


def test(arr, valor_esperado, numero_de_test):
    valor_obtenido = ej1_wrapper(arr)
    assert valor_obtenido == valor_esperado
    print(f"Test {numero_de_test} OK")

def test_medio(valor_inicial, valor_final, valor_esperado, numero_de_test):
    valor_obtenido = medio(valor_inicial, valor_final)
    assert valor_obtenido == valor_esperado
    print(f"Test {numero_de_test} OK")

def tests():
    print("Test de funcion de medio")
    test_medio(0, 7, 3, 1) # 0 1 2 3 4 5 6 7
    test_medio(0, 6, 3, 2) # 0 1 2 3 4 5 6
    test_medio(2, 8, 5, 3) # 0 1 2 3 4 5 6 7 8 
    test_medio(2, 7, 4, 4) 
    test_medio(3,5, 4, 5)
    print("Test de ejercicio")
    test([-1,0,1,3,4], 3, 1)
    test([0,1,2,3,4,5], 2, 2)
    test([-4,2,3,4,5], -1, 3)
    test([-1,0,1,3], 3, 4)
    test([0,1,2,3,4], 2, 5)
    test([-4,2,3,4], -1, 6)
    test([0,2,3,4,5,6], 0, 7)
    test([0,2,3,4,5], 0, 8)
    test([-1,0,1,2,4], 4, 9)
    test([-1,0,1,2,3,5], 5, 10)

tests()