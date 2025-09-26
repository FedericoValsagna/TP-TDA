def ej2(arr):
    subarreglos = []
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
            subarreglos.append(arr[i:len(arr)])
            return subarreglos
        else:
            subarreglos.append(arr[i: punto_de_quiebre])
            i = punto_de_quiebre + 1
    return subarreglos
        
            
print(ej2([3,-5, 7, -4, 1, -8, 3, -7, 5, -9, 5, -2, 4]))