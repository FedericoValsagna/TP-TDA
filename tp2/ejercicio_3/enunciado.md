# PROBLEMA 3 - Algoritmos de Aproximación

Tenemos un conjunto de n objetos, donde el tamaño si del i-ésimo objeto cumple que
0<si<1. El objetivo es empaquetar todos los objetos en el mínimo número posible de
recipientes de tamaño unitario: cada recipiente puede contener cualquier subconjunto de los
objetos cuyo tamaño total no exceda 1. El problema así planteado es NP-Hard.

Se desea encontrar un algoritmo eficiente que encuentre una solución aproximada con una
garantía de a lo sumo 2 veces el valor de la solución óptima.

Se pide:

1. Análisis:
   a. Identificar supuestos, condiciones, limitaciones y/o premisas bajo los cuales
   funcionará el algoritmo desarrollado
   b. Analizar el tamaño del espacio de soluciones factibles del problema

2. Diseño:
   a. Incluir un Pseudocódigo
   b. Mostrar cómo se cumple con la garantía solicitada (se pueden usar citas y
   referencias)
   c. Detallar las estructuras de datos utilizadas. Justificar su elección.

3. Seguimiento: Mostrar un ejemplo de seguimiento con un set de datos reducido

4. Complejidad: Realizar un análisis de la complejidad temporal a partir del
pseudocódigo. Comparar con el tamaño del espacio de soluciones factibles.

5. Sets de datos: diseñar sets de datos apropiados.
   a. Se pueden generar utilizando una función random con una semilla fija, para
   permitir la reproducibilidad de los resultados, o ser generados externamente
   e incluidos como archivos que lee el programa.
   b. Cada set de datos debe ser incluido en la entrega, junto con el resultado
   obtenido en cada caso.
   c. El programa entregado debe generar los sets de datos en tiempo de
   ejecución o leerlos desde archivos incluidos en la entrega.

6. Tiempos de Ejecución: medir los tiempos de ejecución de cada set de datos y
presentarlos en un gráfico.

7. Informe de Resultados:
   a. Redactar un informe de resultados comparando los tiempos de ejecución con
   la complejidad temporal.
   b. El gráfico comparativo de tiempos debe incluir tanto la curva con los valores
   medidos como la curva correspondiente a la complejidad temporal
   determinada.