import main as ej3
import math

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