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

# a = [-1,0,1,3,4]
# b = [0,1,2,3,4,5]
# c = [-4,2,3,4,5]
# d = [-1,0,1,3]
# e = [0,1,2,3,4]
# f = [-4,2,3,4]
# g = [0,2,3,4,5,6] # 0
# h = [0,2,3,4,5] # 0
# i = [-1,0,1,2,4] # 4
# j = [-1,0,1,2,3,5] # 5
# print(ej1_wrapper(a))
# print(ej1_wrapper(b))
# print(ej1_wrapper(c))
# print(ej1_wrapper(d))
# print(ej1_wrapper(e))
# print(ej1_wrapper(f))
# print(ej1_wrapper(g))
# print(ej1_wrapper(h))
# print(ej1_wrapper(i))
# print(ej1_wrapper(j))

# medio(0,7) # 0 1 2 3 4 5 6 7
# medio(0,6) # 0 1 2 3 4 5 6
# medio(2,8) # 0 1 2 3 4 5 6 7 8 
# medio(2,7) 
# print(medio(3,5))