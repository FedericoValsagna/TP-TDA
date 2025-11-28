from ejercicio_2 import resolver_ejercicio_2

def test_grafico_completo():
    """
    Test con el grafo completo del problema (grafico.csv)
    """
    print("TEST 1: Grafo completo (grafico.csv)")
    
    flujo_maximo, flujo_dict = resolver_ejercicio_2('grafico.csv', fuente=1, sumidero=10)
    
    print(f"Flujo máximo: {flujo_maximo}")
    
    # Contar aristas con flujo > 0
    aristas_usadas = []
    for origen in flujo_dict:
        for destino, flujo in flujo_dict[origen].items():
            if flujo > 0:
                aristas_usadas.append((origen, destino, flujo))
    
    print(f"Cantidad de enlaces utilizados: {len(aristas_usadas)}")
    print(f"Aristas utilizadas:")
    for origen, destino, flujo in aristas_usadas:
        print(f"  {origen} → {destino} (flujo: {flujo})")
    
    # Verificar que el flujo máximo sea al menos 10 MB
    assert flujo_maximo >= 10, f"El flujo máximo debe ser al menos 10 MB, pero es {flujo_maximo}"
    
    print("TEST OK\n")


def test_ejemplo_reducido():
    """
    Test con el ejemplo reducido del punto 3 (ejemplo_reducido.csv)
    Grafo: 1 → 6 con 6 nodos
    Flujo esperado: 7 MB
    """
    print("TEST 2: Ejemplo reducido (ejemplo_reducido.csv)")
    
    flujo_maximo, flujo_dict = resolver_ejercicio_2('ejemplo_reducido.csv', fuente=1, sumidero=6)
    
    print(f"Flujo máximo: {flujo_maximo}")
    print(f"Flujo dict: {flujo_dict}")
    
    # Contar aristas con flujo > 0
    aristas_usadas = []
    for origen in flujo_dict:
        for destino, flujo in flujo_dict[origen].items():
            if flujo > 0:
                aristas_usadas.append((origen, destino, flujo))
    
    print(f"Cantidad de enlaces utilizados: {len(aristas_usadas)}")
    print(f"Aristas utilizadas:")
    for origen, destino, flujo in aristas_usadas:
        print(f"  {origen} → {destino} (flujo: {flujo})")
    
    # Verificar que el flujo máximo sea 7 MB (según el seguimiento)
    assert flujo_maximo == 7, f"El flujo máximo esperado es 7 MB, pero es {flujo_maximo}"
    
    # Verificar que se usen 7 aristas (según el seguimiento)
    assert len(aristas_usadas) == 5, f"Se esperan 5 aristas, pero hay {len(aristas_usadas)}"
    
    print("TEST OK\n")


if __name__ == "__main__":
    test_grafico_completo()
    test_ejemplo_reducido()
    print("Todos los tests pasaron correctamente ✓")
