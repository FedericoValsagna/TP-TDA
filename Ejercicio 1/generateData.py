import random
import os

random.seed(2025)

casos_base = [
    "-1,0,1,3,4 / 3",
    "0,1,2,3,4,5 / 2", 
    "-4,2,3,4,5 / -1",
    "-1,0,1,3 / 3",
    "0,1,3,4 / 1",
    "-4,2,3,4 / -1",
    "0,2,3,4,5,6 / 0",
    "0,2,3,4,5 / 0",
    "-1,0,1,2,4 / 4",
    "-1,0,1,2,3,5 / 5"
]

def generar_arreglo_ordenado_con_punto_fijo(tamano, tiene_punto_fijo=True):
    arreglo = []
    
    if tiene_punto_fijo:
        indice_punto_fijo = random.randint(0, tamano - 1)
        
        for i in range(tamano):
            if i < indice_punto_fijo:
                arreglo.append(i - random.randint(1, 5))
            elif i == indice_punto_fijo:
                arreglo.append(i)
            else:
                arreglo.append(i + random.randint(1, 5))
        
        return arreglo, indice_punto_fijo
    else:
        offset = random.randint(1, 5)
        for i in range(tamano):
            arreglo.append(i + offset)
        return arreglo, -1

def generar_arreglos_de_prueba():
    casos_de_prueba = casos_base.copy()
    tamanos = [5, 10, 1000, 10_000, 100_000, 1_000_000, 10_000_000]
    
    for tamano in tamanos:
        
        for tiene_punto_fijo in [True, False]:
            arreglo, resultado_esperado = generar_arreglo_ordenado_con_punto_fijo(tamano, tiene_punto_fijo)
            caso_de_prueba = f"{', '.join(map(str, arreglo))} / {resultado_esperado}"
            casos_de_prueba.append(caso_de_prueba)
    
    return casos_de_prueba

def escribir_archivo_de_prueba(test_cases, filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    with open(filepath, 'w') as f:
        for test_case in test_cases:
            f.write(test_case + '\n')
    
    print(f"Total casos de prueba generados: {len(test_cases)}")


def generar_casos_de_prueba(filename="tests.txt"):
    test_cases = generar_arreglos_de_prueba()
    escribir_archivo_de_prueba(test_cases, filename)

if __name__ == "__main__":
    generar_casos_de_prueba()
