def ej4(arreglo):
    # Caso todos negativos
    todos_negativos = True
    for numero in arreglo:
        if numero > 0:
            todos_negativos = False
            break
    
    if todos_negativos:
        mayor_negativo = max(arreglo)
        return [mayor_negativo], mayor_negativo


    suma_resultado = [0] * len(arreglo) 
    suma_actual = [0] * len(arreglo)

    suma_resultado[0] = arreglo[0]
    suma_actual[0] = arreglo[0]

    for i in range(1, len(arreglo)):
        s = suma_actual[i-1] + arreglo[i]
        if s <= 0:
            suma_actual[i] = 0
        else:
            suma_actual[i] = s
 
        suma_resultado[i] = max(suma_actual[i], suma_resultado[i -1])
    return reconstruccion(suma_resultado, suma_actual, arreglo), suma_resultado[-1]

        
def reconstruccion(suma_resultado, suma_actual, arreglo):
    inicio = True
    subarreglo = []
    for i in range(len(arreglo) - 1,1 ,-1):
        if inicio:
            if suma_resultado[i] - arreglo[i] != suma_actual[i - 1]:
                continue
            subarreglo.append(arreglo[i])
            inicio = False
        else:
            if suma_actual[i] - arreglo[i] == 0:
                subarreglo.append(arreglo[i])
                subarreglo.reverse()
                return subarreglo
            else:
                subarreglo.append(arreglo[i])