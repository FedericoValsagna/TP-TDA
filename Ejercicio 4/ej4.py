def ej4(arreglo):
    # Caso todos negativos: La idea es que el algoritmo no funciona por como está planteado en este caso, pero de ser todos negativos entonces la
    # resolución es trivial, el subarreglo de suma máxima debe ser el mayor elemento del subarreglo (Ya que por consigna debe tener al menos 1 elemento)
    todos_negativos = True
    for numero in arreglo:
        if numero > 0:
            todos_negativos = False
            break
    if todos_negativos:
        mayor_negativo = max(arreglo)
        return [mayor_negativo], mayor_negativo


    # Caso general: Se tienen 2 arreglos, uno que calcula el resultado óptimo para el subarreglo correspondiente y otro que calcule la sumatoria actual.
    # Por sumatoria actual se entiende que cuando una sumatoria cae por debajo de 0 entonces arranca un nuevo subarreglo posible con sumatoria más alta.
    # La ecuación de recurrencia de SR (Suma Resultado) es SR[i] = max(SA[i], SR[i-1]) (Donde SA es la sumatoria actual). Así mismo la ecuación de recurrencia
    # de SA es SA[i] = SA[i - 1] + SA[i] Si la suma > 0, sino SA[i] = 0 arrancando una nueva sumatoria.

    suma_resultado = [0] * len(arreglo) 
    suma_actual = [0] * len(arreglo)

    if arreglo[0] > 0:
        suma_resultado[0] = arreglo[0]
        suma_actual[0] = arreglo[0]
    else:
        suma_resultado[0] = 0
        suma_actual[0] = 0

    for i in range(1, len(arreglo)):
        suma_en_paso_actual = suma_actual[i-1] + arreglo[i]
        if suma_en_paso_actual <= 0:
            suma_actual[i] = 0
        else:
            suma_actual[i] = suma_en_paso_actual
 
        suma_resultado[i] = max(suma_actual[i], suma_resultado[i -1])
    print(f" A: {arreglo}")
    print(f"SR: {suma_resultado}")
    print(f"SA: {suma_actual}")
    return reconstruccion(suma_resultado, suma_actual, arreglo), suma_resultado[-1]

        
def reconstruccion(suma_resultado, suma_actual, arreglo):
    inicio = True
    subarreglo = []
    for i in range(len(arreglo) - 1, -1,-1):
        # La idea es que el primer elemento del subarreglo se identifica desde la sumatoria total, los subsiguientes se identifican a partir
        # no del total sino del acumulado.
        if inicio:
            if suma_resultado[i] - arreglo[i] != suma_actual[i - 1]:
                continue
            subarreglo.append(arreglo[i])

            # Este corte es por si el subarreglo es de largo 1
            if suma_actual[i- 1] == 0:
                break
            inicio = False
        else:
            # Si la sumatoria actual menos el item actual dan 0 eso indica que estamos en el comienzo de la sumatoria, por lo cual
            # encontramos el subarreglo máximo
            if suma_actual[i] - arreglo[i] == 0:
                subarreglo.append(arreglo[i])
                break
            else:
                # Acá tomamos en cuenta que estamos en un punto medio del subarreglo máximo, en ese caso todo elemento intermedio entre el comienzo
                # y fin del subarreglo automáticamente se encuentra dentro del subarreglo ya que debe ser continuo.
                subarreglo.append(arreglo[i])

    subarreglo.reverse()
    return subarreglo