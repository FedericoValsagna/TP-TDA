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
    Aplicamos Ford-Fulkerson y nos dará el flujo
    máximo del grafo. Sabiendo eso, debemos empezar a quitar aristas que llegan al sumidero, es decir, al nodo 10, hasta encontrar el corte mínimo que incluye a la fuente, el nodo 1 y su
    flujo de salida es igual al flujo máximo.
    
    Estos serán los nodos y las aristas mínimos para 
    transferir los datos.

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
        
        devolver hallar_minimo(V, flujo_maximo)

    def hallar_minimo(V, residual):
        limpiar_v(V, residual)
        Ordenar las aristas que llegan a 10:
            # seguir mañana


    def limpiar_v(V, residual):
    '''
    Elimino los que tienen igual flujo en ambos lados
    porque se anulan, sus tráficos se van a compensar
    '''
        por cada v de V:
            v_i, v_j, c = v
            si V[v_i, v_j] == -c:
                eliminar_de_v(v,V)
                eliminar_de_v((v_j,v_i),V) # elimino la inversa también


    c.  Detallar las estructuras de datos utilizadas. Justificar su elección.

    Para guardar las aristas podría utilizar una matriz o un diccionario cuyoas valor v_i, v_j sean la clave.

3.  **Seguimiento:** Mostrar un ejemplo de seguimiento con un set de datos reducido
4.  **Complejidad:** Realizar un análisis de la complejidad temporal a partir del pseudocódigo
5.  **Solución:**
    a.  Opción 1: resolver manualmente, indicando paso a paso cómo el algoritmo planteado encuentra los caminos de aumento y construye la red residual
    b.  Opción 2: Desarrollar un programa que resuelva el modelo usando Python y una biblioteca de Redes de Flujo (propia o de terceros). Incluir todos los archivos necesarios para la ejecución. Incluir un archivo con el resultado obtenido.
6.  **Informe de Resultados:**
    a.  Redactar un informe de la solución, indicando cómo se debe fragmentar y distribuir el archivo
    b.  Para resolver este problema, ¿es mejor utilizar Programación Lineal o Redes de Flujo? Justificar el criterio utilizado para comparar las dos técnicas
