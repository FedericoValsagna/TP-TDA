# Resolución

## PROBLEMA 2 - Redes de flujo

1.  **Análisis:**
    a.  Identificar supuestos, condiciones, limitaciones y/o premisas bajo los cuales funcionará el algoritmo desarrollado.

    - Las conexiones entre los nodos son bidireccionales.
    - 1 actuará de fuente y es única.
    - 10 actuará de sumidero y es única.
    - No puede haber ciclos.
    - Las conexiones salientes de 1, es decir,
    la fuente, no son bidireccionales.
    - Las conexiones que llegan a 10, es decir,
    el sumidero, no son bidireccionales.
    - La información que entra en un nodo es igual
    a la información que sale.

2.  **Diseño:**
    a.  Explicación en prosa de cómo se adaptan los datos de entrada a una red de flujo, y de cómo se debe interpretar la salida del algoritmo de Ford-Fulkerson para resolver este problema. Se recomienda incluir diagramas de apoyo.

    La capacidad de memoria en las aristas será la
    capacidad de los enlaces entre los nodos.
    
    Reemplazaremos cada arista no dirigida, por dos aristas, una en un sentido y otra en el opuesto.
    
    Aplicamos Ford-Fulkerson y nos dará el flujo
    máximo del grafo. En el grafo residual de 
    Ford-Fulkerson, habrán aristas cuya recíproca
    tenga la misma carga pero en sentido opuesto.
    
    Estas aristas deberán ser las que se eliminan
    de la solución final para obtener la red con 
    la menor cantidad de enlaces.

    b.  Incluir un Pseudocódigo del algoritmo a desarrollar (asumir que ya se cuenta con un algoritmo que resuelve Redes de Flujo).
    
    Sea V la lista de aristas del grafo

    def resolver(V):

        Para cada v de V
            v_i, v_j, c = v
            Si v_i != 1 y v_j != 10:
                Agregar a V (v_j, v_i, c)
        
        flujo_maximo, residual = resolver_red(V)

        si flujo_maximo < 10:
            devolver [] # indicando que el problema no tiene solución
        
        solucion = []

        Para cada v de residual:
            v_i, v_j, c_v = v
            u = residual[v_j,v_i]
            u_i, u_j, c_u = u
            si c_v > c_u:
                solucion.agregar(v)
            sino:
                solucion.agregar(u)
            residual.eliminar(u)
            residual.eliminar(v)
        
        devolver solucion

    c.  Detallar las estructuras de datos utilizadas. Justificar su elección.

    Para el grafo y para el grafo residual,
    usaremos una lista de adyacencias, donde
    cada elemento de la lista representará un
    nodo y el valor que almacena será una lista
    de tuplas donde la primera posición
    indicará el nodo destino y el segundo la
    capacidad de la arista.
    Esta representación se elige porque, en el grafo
    propuesto, cada nodo tiene como mucho 4 aristas,
    razón por la cual, una matriz sería poco
    eficiente para representar este problema.

3.  **Seguimiento:** Mostrar un ejemplo de seguimiento con un set de datos reducido
4.  **Complejidad:** Realizar un análisis de la complejidad temporal a partir del pseudocódigo
5.  **Solución:**
    a.  Opción 1: resolver manualmente, indicando paso a paso cómo el algoritmo planteado encuentra los caminos de aumento y construye la red residual
    b.  Opción 2: Desarrollar un programa que resuelva el modelo usando Python y una biblioteca de Redes de Flujo (propia o de terceros). Incluir todos los archivos necesarios para la ejecución. Incluir un archivo con el resultado obtenido.
6.  **Informe de Resultados:**
    a.  Redactar un informe de la solución, indicando cómo se debe fragmentar y distribuir el archivo
    b.  Para resolver este problema, ¿es mejor utilizar Programación Lineal o Redes de Flujo? Justificar el criterio utilizado para comparar las dos técnicas
