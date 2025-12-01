import sys
import csv
import networkx as nx

def leer_grafo(archivo, fuente=1, sumidero=10):
    """
    Lee un grafo desde un archivo CSV
    Formato esperado: origen,destino,capacidad
    Retorna: grafo doblemente direccionado
    como lista de adyacencias implementado como
    diccionario de diccionarios.
    """
    grafo = {}
    
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Saltar header si existe
            header = next(reader, None)
            
            # Verificar si la primera línea es header o datos
            if header and header[0].isdigit():
                # No es header procesarla como dato
                origen, destino, capacidad = header
                origen = int(origen)
                destino = int(destino)
                capacidad = int(capacidad)
                adyacencias = grafo.get(origen, {})
                adyacencias[destino] = capacidad
                grafo[origen] = adyacencias

                if origen != fuente and destino != sumidero:
                    adyacencias_rev = grafo.get(destino, {})
                    adyacencias_rev[origen] = capacidad
                    grafo[destino] = adyacencias_rev
            
            # Leer el resto de las líneas
            for fila in reader:
                origen, destino, capacidad = int(fila[0]), int(fila[1]), int(fila[2])

                adyacencias = grafo.get(origen, {})
                adyacencias[destino] = capacidad
                grafo[origen] = adyacencias

                if origen != fuente and destino != sumidero:
                    adyacencias_rev = grafo.get(destino, {})
                    adyacencias_rev[origen] = capacidad
                    grafo[destino] = adyacencias_rev
        # print(f"Grafo formado '{grafo}'")
        return grafo
        
    except FileNotFoundError:
        print(f"No se encontró el archivo '{archivo}'")
        sys.exit(1)
    except ValueError as e:
        print(f"Error al parsear el archivo: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

def resolver_ford_fulkerson(grafo, fuente, sumidero):
    """
    Crear al grafo digirido para networkx y ejecutar Ford-Fulkerson
    """
    G = nx.DiGraph()

    for u in grafo:
        for v in grafo[u]:
            capacidad = grafo[u][v]
            G.add_edge(u, v, capacity=capacidad)

    flujo_valor, flujo_dict = nx.maximum_flow(G, fuente, sumidero, 
                                              flow_func=nx.algorithms.flow.shortest_augmenting_path)
    return flujo_valor, flujo_dict
    
def minimizar_aristas_greedy(grafo, fuente, sumidero, flujo_objetivo):
    """
    Estrategia greedy: comenzar con todas las aristas de
    menor a mayor flujo y eliminar una por una
    las que no afecten el flujo máximo.
    """
    grafo_actual = {}
    for u in grafo:
        grafo_actual[u] = grafo[u].copy()
    
    # podría recibir esto por parámetro para no recalcularlo
    # pero como uso flujo_dict para trabajar abajo igual
    # tendría que copiarlo
    _, flujo_dict = resolver_ford_fulkerson(grafo_actual, fuente, sumidero)
    
    # lista de aristas usadas ordenadas por flujo de menor a mayor
    aristas_con_flujo = [(u, v, flujo_dict[u][v]) for u in flujo_dict 
                         for v in flujo_dict[u] if flujo_dict[u][v] > 0]
    aristas_con_flujo.sort(key=lambda x: x[2])
    
    # intentar eliminar cada arista
    for u, v, _ in aristas_con_flujo:
        if u in grafo_actual and v in grafo_actual[u]:

            capacidad_original = grafo_actual[u][v]
            
            del grafo_actual[u][v]
            if not grafo_actual[u]:
                del grafo_actual[u]
            
            # verificar si aún alcanzamos el flujo objetivo
            try:
                flujo_test, flujo_dict_test = resolver_ford_fulkerson(grafo_actual, fuente, sumidero)
                
                if flujo_test >= flujo_objetivo:
                    # podemos vivir sin esta arista
                    flujo_dict = flujo_dict_test
                else:
                    # necesitábamos esta arista
                    if u not in grafo_actual:
                        grafo_actual[u] = {}
                    grafo_actual[u][v] = capacidad_original
            except:
                # por si borramos una arista importante
                if u not in grafo_actual:
                    grafo_actual[u] = {}
                grafo_actual[u][v] = capacidad_original
    
    return flujo_dict

def resolver_ejercicio_2(archivo, fuente=1, sumidero=10):
    
    grafo = leer_grafo(archivo, fuente, sumidero)
    
    # obtengo el flujo máximo posible
    flujo_max, _ = resolver_ford_fulkerson(grafo, fuente, sumidero)
    print(f"Flujo máximo posible: {flujo_max}")
    
    flujo_dict = minimizar_aristas_greedy(grafo, fuente, sumidero, flujo_max)
    
    flujo_valor = sum(flujo_dict.get(fuente, {}).values())
    return flujo_valor, flujo_dict

def main():

    archivo_entrada = 'grafico.csv'
    fuente = 1
    sumidero = 10

    if len(sys.argv) == 4:
        archivo_entrada = sys.argv[1]
        fuente = int(sys.argv[2])
        sumidero = int(sys.argv[3])
    else:
        print(f"Usando '{archivo_entrada}, {fuente}, {sumidero}' por defecto")
    
    flujo_valor, flujo_dict = resolver_ejercicio_2(archivo_entrada, fuente, sumidero)

    # Contar cantidad de aristas usadas (con flujo > 0)
    # por la libreria que usamos en realidad son todas las que existen en flujo_dict
    aristas_usadas = sum(1 for u in flujo_dict for v in flujo_dict[u] if flujo_dict[u][v] > 0)

    print(f"El flujo máximo desde el nodo {fuente} al nodo {sumidero} es: {flujo_valor}")
    print(f"Cantidad de aristas usadas: {aristas_usadas}")
    print("Flujos por arista:")
    for u in flujo_dict:
        for v in flujo_dict[u]:
            if flujo_dict[u][v] > 0:
                print(f"  {u} -> {v}: {flujo_dict[u][v]}")


if __name__ == "__main__":
    main()