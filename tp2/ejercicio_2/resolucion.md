# Resolución

## PROBLEMA 2 - Redes de flujo

1.  **Análisis:**
    a.  Identificar supuestos, condiciones, limitaciones y/o premisas bajo los cuales funcionará el algoritmo desarrollado.

    - El grafo original es no dirigido. Se 
    modelará como un grafo dirigido agregando
    aristas en ambas direcciones.
    - Las capacidades son simétricas en cada
    arista.
    - 1 actuará de fuente y es única.
    - 10 actuará de sumidero y es único.
    - Las aristas que salen de la fuente solo permiten flujo saliente.
    - Las conexiones que llegan al nodo 10,
    es decir, el sumidero, no son bidireccionales.
    - La información que entra en un nodo es igual
    a la información que sale.
    - Las capacidades son números enteros positivos.

2.  **Diseño:**
    a.  Explicación en prosa de cómo se adaptan los datos de entrada a una red de flujo, y de cómo se debe interpretar la salida del algoritmo de Ford-Fulkerson para resolver este problema. Se recomienda incluir diagramas de apoyo.

    La capacidad de memoria en las aristas será la
    capacidad de los enlaces entre los nodos.
    
    Reemplazaremos cada arista no dirigida, por dos aristas, una en un sentido y otra en el opuesto.
    
    Aplicamos Ford-Fulkerson y nos dará el flujo
    máximo del grafo. En el grafo de flujos 
    que devuelva Ford-Fulkerson, habrán 
    aristas cuya recíproca
    tenga la misma carga pero en sentido opuesto.
    Estas aristas, con flujo neto cero,
    deberán ser las que se omiten
    de la solución final ya que no se usan
    para obtener la red con 
    la menor cantidad de enlaces.

    b.  Incluir un Pseudocódigo del algoritmo a desarrollar (asumir que ya se cuenta con un algoritmo que resuelve Redes de Flujo).
    
    def obtener_complemento(flujos, v):
        # asumo flujos diccionario de diccionarios
        # o lista de adyacencias
        v_i, v_j, c = v
        u_c = flujos[v_j][v_i] # si no existe es 0
        u = (v_j, v_i, u_c)
        devolver u

    Sea V la lista de aristas del grafo

    def resolver(V):

        Para cada v de V
            v_i, v_j, c = v
            Si v_i != 1 y v_j != 10:
                Agregar a V (v_j, v_i, c)
        
        flujo_maximo, flujos = resolver_red(V)

        si flujo_maximo < 10:
            devolver [] # indicando que el problema no tiene solución
        
        sea solucion un set vacío
        sea aristas_procesadas un set vacío

        Para cada v de flujos:
            v_i, v_j, c_v = v
            u = obtener_complemento(flujos, v)

            si (v_i, v_j) no está en aristas_procesadas y (v_j, v_i) no está en aristas_procesadas:
                u_i, u_j, c_u = u
                flujo_neto = c_v - c_u
                si flujo_neto != 0:
                    si flujo_neto > 0:
                        nueva_v = v_i, v_j, flujo_neto
                        solucion.agregar(nueva_v)
                        aristas_procesadas.agregar((v_i, v_j))
                    sino:
                        nueva_u = (u_i, u_j, -flujo_neto)
                        solucion.agregar(nueva_u)
                        aristas_procesadas.agregar((u_i, u_j))
        
        devolver solucion

    c.  Detallar las estructuras de datos utilizadas. Justificar su elección.

    Para el grafo, usaremos una lista de adyacencias, donde
    cada elemento de la lista representará un
    nodo y el valor que almacena será una lista
    de tuplas donde la primera posición
    indicará el nodo destino y el segundo la
    capacidad de la arista.
    Esta representación se elige porque, 
    en el grafo propuesto, cada nodo tiene 
    como mucho 4 aristas,
    razón por la cual, una matriz sería poco
    eficiente para representar este problema.

    Para el grafo de flujos, podríamos usar una
    lista de adyacencias o un dicionario de
    diccionarios. En el primer nivel
    la clave sería 
    el nodo de origen y en el segundo, el nodo
    de destino, el valor sería el flujo.
    Esto permitiría buscar la arista recíproca
    de manera muy rápida.

    Adicionalmente, usamos un set 'aristas_procesadas' 
    para evitar procesar dos veces la misma arista del 
    grafo de flujos, ya que cada arista original genera
    dos dirigidas (u→v y v→u).

    Para la solución armamos un set de tuplas
    para no preocuparnos por procesar dos
    veces una arista

3.  **Seguimiento:** Mostrar un ejemplo de seguimiento con un set de datos reducido


4.  **Complejidad:** Realizar un análisis de la complejidad temporal a partir del pseudocódigo


5.  **Solución:**
    a.  Opción 1: resolver manualmente, indicando paso a paso cómo el algoritmo planteado encuentra los caminos de aumento y construye la red residual
    b.  Opción 2: Desarrollar un programa que resuelva el modelo usando Python y una biblioteca de Redes de Flujo (propia o de terceros). Incluir todos los archivos necesarios para la ejecución. Incluir un archivo con el resultado obtenido.
6.  **Informe de Resultados:**
    a.  Redactar un informe de la solución, indicando cómo se debe fragmentar y distribuir el archivo
    b.  Para resolver este problema, ¿es mejor utilizar Programación Lineal o Redes de Flujo? Justificar el criterio utilizado para comparar las dos técnicas
