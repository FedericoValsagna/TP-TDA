def ej1(arr, indice_inicial, indice_final):
    # if indice_final - indice_inicial == 1:


    if indice_final == indice_inicial:
        if arr[indice_inicial] == indice_inicial:
            return indice_inicial
        else:
            # Indicar que no existe
            return -1

    indice_medio = medio(indice_inicial, indice_final)
    if arr[indice_medio] == indice_medio:
        return indice_medio
    if arr[indice_medio] < indice_medio:
        return ej1(arr, indice_medio + 1, indice_final)
    else:
        return ej1(arr,indice_inicial, indice_medio)


def ej1_wrapper(arr):
    return ej1(arr, 0, len(arr) - 1)




def medio(indice_inicial, indice_final):
    return (indice_final - indice_inicial) // 2 + indice_inicial
