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
                # No es header, procesarla como dato
                origen, destino, capacidad = header
                origen = int(origen)
                destino = int(destino)
                capacidad = int(capacidad)
                adyacencias = grafo.get(origen, {})
                adyacencias[destino] = capacidad
                grafo[origen] = adyacencias

                if origen != sumidero and destino != fuente:
                    adyacencias_rev = grafo.get(destino, {})
                    adyacencias_rev[origen] = capacidad
                    grafo[destino] = adyacencias_rev
            
            # Leer el resto de las líneas
            for fila in reader:
                origen, destino, capacidad = int(fila[0]), int(fila[1]), int(fila[2])

                adyacencias = grafo.get(origen, {})
                adyacencias[destino] = capacidad
                grafo[origen] = adyacencias

                if origen != sumidero and destino != fuente:
                    adyacencias_rev = grafo.get(destino, {})
                    adyacencias_rev[origen] = capacidad
                    grafo[destino] = adyacencias_rev
            
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

    flujo_valor, flujo_dict = nx.maximum_flow(G, fuente, sumidero, flow_func=nx.algorithms.flow.edmonds_karp)
    return flujo_valor, flujo_dict

def resolver_ejercicio_2(archivo, fuente=1, sumidero=10):
    # Leer grafo
    grafo = leer_grafo(archivo, fuente, sumidero)
    
    # si bien la librería tiene un modo de resolver grafos no digiridos,
    # vamos a respetar el pseudocódigo para hacer el proceso visto en clase
    flujo_valor, flujo_dict = resolver_ford_fulkerson(grafo, fuente, sumidero)
    return flujo_valor, flujo_dict

def main():

    archivo_entrada = 'grafico.csv'
    fuente = 1
    sumidero = 10

    # Determinar archivo de entrada
    if len(sys.argv) == 4:
        archivo_entrada = sys.argv[1]
        fuente = int(sys.argv[2])
        sumidero = int(sys.argv[3])
    else:
        print(f"Usando '{archivo_entrada}, {fuente}, {sumidero}' por defecto")
    
    flujo_valor, flujo_dict = resolver_ejercicio_2(archivo_entrada, fuente, sumidero)

    print(f"El flujo máximo desde el nodo {fuente} al nodo {sumidero} es: {flujo_valor}")
    print("Flujos por arista:")
    for u in flujo_dict:
        for v in flujo_dict[u]:
            if flujo_dict[u][v] > 0:
                print(f"  {u} -> {v}: {flujo_dict[u][v]}")


if __name__ == "__main__":
    main()