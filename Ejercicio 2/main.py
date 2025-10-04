def ej2(arr):
    subarreglos = []
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
            subarreglos.append(arr[i:len(arr)])
            break
        elif punto_de_quiebre is not None:
            subarreglos.append(arr[i: punto_de_quiebre])
            i = punto_de_quiebre + 1
        else:
            i += 1
    return len(subarreglos)