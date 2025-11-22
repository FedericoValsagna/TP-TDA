def ej2(arr):
    cantidad_de_subarreglos = 0
    i = 0
    while i < len(arr):
        sumatoria = 0
        punto_de_quiebre = None
        for j in range(i, len(arr)):
            if sumatoria > 0:
                if sumatoria + arr[j] <= 0:
                    punto_de_quiebre = j
            sumatoria += arr[j]
        if sumatoria > 0:
            cantidad_de_subarreglos += 1
            break
        elif punto_de_quiebre is not None:
            cantidad_de_subarreglos += 1
            i = punto_de_quiebre + 1
        else:
            i += 1
    return cantidad_de_subarreglos