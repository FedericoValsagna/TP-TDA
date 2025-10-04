import random
import os

random.seed(2025)

casos_base = [
    "3, -5, 7, -4, 1, -8, 3, -7, 5, -9, 5, -2, 4 / 3, -5, 7, -4, 1 / 3, -7, 5 / 5, -2, 4"
]

def generar_arreglo_simple(tamano):
    arreglo = []
    for i in range(tamano):
        arreglo.append(random.randint(-10, 10))
    return arreglo

def generar_casos_de_prueba():
    casos_de_prueba = casos_base.copy()
    tamanos = [5, 10, 1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    
    for tamano in tamanos:
        print(f"Generando caso de prueba para tamaño {tamano}...")
        
        for _ in range(2):
            arreglo = generar_arreglo_simple(tamano)
            caso_de_prueba = f"{', '.join(map(str, arreglo))}"
            casos_de_prueba.append(caso_de_prueba)
    
    return casos_de_prueba

def escribir_archivo_de_prueba(casos_de_prueba, filename="tests.txt"):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    with open(filepath, 'w') as f:
        for caso_de_prueba in casos_de_prueba:
            f.write(caso_de_prueba + '\n')
    
    print(f"Casos de prueba escritos en {filepath}")
    print(f"Total casos de prueba generados: {len(casos_de_prueba)}")

def main():
    print("Generando casos de prueba para algoritmo greedy de intervalos positivos...")
    casos_de_prueba = generar_casos_de_prueba()
    escribir_archivo_de_prueba(casos_de_prueba)

if __name__ == "__main__":
    main()
