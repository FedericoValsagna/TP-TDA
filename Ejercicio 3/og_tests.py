import math
import sys
import os
# import pytest
import ej3

def ejercicio3(numeros):
    res = ejecutar_algoritmo(numeros)
    sumatoria, elementos_del_arreglo = res['suma'], res['estado']
    subarreglo = []
    for i in range(len(elementos_del_arreglo)):
        if elementos_del_arreglo[i] == 1:
            subarreglo.append(numeros[i])
    return subarreglo, sumatoria




def ejecutar_algoritmo(numeros_test):
    """
    Función auxiliar para ejecutar el algoritmo con un array específico
    """
    # Modificar las variables globales del módulo ej3
    ej3.numeros = numeros_test
    ej3.A = len(numeros_test)
    ej3.suma_maxima = {'suma': -math.inf, 'estado': None}
    
    # Crear estado inicial
    estado_inicial = [0] * ej3.A
    if ej3.A > 0:
        estado_inicial[0] = 1
    
    # Ejecutar el algoritmo
    resultado = ej3.resolver_con_backtracking(estado_inicial)
    return resultado

def test_solucion_un_solo_numero():
    """
    La solución es solo 1 número del array
    Array donde el máximo elemento individual es mayor que cualquier suma de subarrays contiguos
    """
    numeros_test = [-2, 10, -5, -3, -1]
    solucion_esperada_estado = [0, 1, 0, 0, 0]
    suma_esperada = 10
    
    resultado = ejecutar_algoritmo(numeros_test)
    
    # Verificar que la suma sea correcta
    suma_calculada = sum(numeros_test[i] for i in range(len(resultado['estado'])) if resultado['estado'][i] == 1)
    
    assert resultado['suma'] == suma_esperada, f"Error: suma esperada {suma_esperada}, obtenida {resultado['suma']}"
    assert resultado['estado'] == solucion_esperada_estado, f"Error: estado esperado {solucion_esperada_estado}, obtenido {resultado['estado']}"
    assert suma_calculada == suma_esperada, f"Error: suma calculada {suma_calculada} no coincide con suma esperada {suma_esperada}"

def test_solucion_tres_numeros_medio():
    """
    La solución son los 3 números del medio de un array de 7
    Array donde los 3 números del medio tienen la suma máxima
    """
    numeros_test = [-5, -2, 3, 4, 5, -3, -6]
    solucion_esperada_estado = [0, 0, 1, 1, 1, 0, 0]
    suma_esperada = 12
    
    resultado = ejecutar_algoritmo(numeros_test)
    
    # Verificar que la suma sea correcta
    suma_calculada = sum(numeros_test[i] for i in range(len(resultado['estado'])) if resultado['estado'][i] == 1)
    
    assert resultado['suma'] == suma_esperada, f"Error: suma esperada {suma_esperada}, obtenida {resultado['suma']}"
    assert resultado['estado'] == solucion_esperada_estado, f"Error: estado esperado {solucion_esperada_estado}, obtenido {resultado['estado']}"
    assert suma_calculada == suma_esperada, f"Error: suma calculada {suma_calculada} no coincide con suma esperada {suma_esperada}"

def test_solucion_todo_el_array():
    """
    La solución es todo el array
    Array donde todos los números son positivos, por lo que la suma de todos es máxima
    """
    numeros_test = [1, 3, 2, 4, 1]
    solucion_esperada_estado = [1, 1, 1, 1, 1]
    suma_esperada = 11
    
    resultado = ejecutar_algoritmo(numeros_test)
    
    # Verificar que la suma sea correcta
    suma_calculada = sum(numeros_test[i] for i in range(len(resultado['estado'])) if resultado['estado'][i] == 1)
    
    assert resultado['suma'] == suma_esperada, f"Error: suma esperada {suma_esperada}, obtenida {resultado['suma']}"
    assert resultado['estado'] == solucion_esperada_estado, f"Error: estado esperado {solucion_esperada_estado}, obtenido {resultado['estado']}"
    assert suma_calculada == suma_esperada, f"Error: suma calculada {suma_calculada} no coincide con suma esperada {suma_esperada}"

if __name__ == "__main__":
    # Ejecutar los tests directamente
    test_solucion_un_solo_numero()
    test_solucion_tres_numeros_medio()
    test_solucion_todo_el_array()