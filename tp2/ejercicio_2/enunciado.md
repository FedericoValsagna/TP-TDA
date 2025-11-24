## PROBLEMA 1 - Programación Lineal
La red de telecomunicaciones de la Facultad se compone de varios nodos y enlaces, cada uno con una capacidad definida. En el diagrama presentamos el esquema general, donde las aristas representan la capacidad medida en MB. Se desea enviar un archivo de 10 MB desde el nodo 1 hasta el nodo 10. El protocolo de comunicación es TCP/IP, así que el archivo puede ser fragmentado en partes más pequeñas en cualquiera de los nodos de la red, y el protocolo mismo se encargará de reconstruirlo en el orden correcto al llegar al nodo 10.

Plantear y resolver un modelo de Programación Lineal que permita determinar cuál será la mejor forma de fragmentar y enviar el archivo utilizando la menor cantidad posible de enlaces.

![Diagrama de la red (Problema 1)](./img/problema_1.png)

## PROBLEMA 2 - Redes de flujo

Resolver el Problema 1 usando Redes de Flujo.

Se pide:

1.  **Análisis:**
    a.  Identificar supuestos, condiciones, limitaciones y/o premisas bajo los cuales funcionará el algoritmo desarrollado
2.  **Diseño:**
    a.  Explicación en prosa de cómo se adaptan los datos de entrada a una red de flujo, y de cómo se debe interpretar la salida del algoritmo de Ford-Fulkerson para resolver este problema. Se recomienda incluir diagramas de apoyo.
    b.  Incluir un Pseudocódigo del algoritmo a desarrollar (asumir que ya se cuenta con un algoritmo que resuelve Redes de Flujo).
    c.  Detallar las estructuras de datos utilizadas. Justificar su elección.
3.  **Seguimiento:** Mostrar un ejemplo de seguimiento con un set de datos reducido
4.  **Complejidad:** Realizar un análisis de la complejidad temporal a partir del pseudocódigo
5.  **Solución:**
    a.  Opción 1: resolver manualmente, indicando paso a paso cómo el algoritmo planteado encuentra los caminos de aumento y construye la red residual
    b.  Opción 2: Desarrollar un programa que resuelva el modelo usando Python y una biblioteca de Redes de Flujo (propia o de terceros). Incluir todos los archivos necesarios para la ejecución. Incluir un archivo con el resultado obtenido.
6.  **Informe de Resultados:**
    a.  Redactar un informe de la solución, indicando cómo se debe fragmentar y distribuir el archivo
    b.  Para resolver este problema, ¿es mejor utilizar Programación Lineal o Redes de Flujo? Justificar el criterio utilizado para comparar las dos técnicas
