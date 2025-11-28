import random
import time


def ejecutar_prueba_volumen(funcion, n):
    """
    Ejecuta una prueba de volumen para una función de bin packing.
    
    Args:
        funcion: Función a probar (implementación de next_fit)
        n: Tamaño del array aleatorio a generar
    
    Returns:
        Tiempo de ejecución en segundos
    """
    # Generar array aleatorio de n elementos entre 0 y 1
    lista_objetos = [random.random() for _ in range(n)]
    
    # Medir tiempo de ejecución
    inicio = time.perf_counter()
    funcion(lista_objetos)
    fin = time.perf_counter()
    
    # Tiempo de ejecución en segundos
    return fin - inicio
