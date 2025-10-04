def ej2(arr):
    cantidad_intervalos = 0
    punto_de_quiebre = 0
    i = 0
    while i < len(arr):
        sumatoria = 0
        for j in range(i, len(arr)):
            if sumatoria > 0:
                if sumatoria + arr[j] <= 0:
                    punto_de_quiebre = j
            sumatoria += arr[j]
        if sumatoria > 0:
            cantidad_intervalos += 1
            return cantidad_intervalos
        else:
            cantidad_intervalos += 1
            i = punto_de_quiebre + 1
    return cantidad_intervalos