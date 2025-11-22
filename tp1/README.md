# TP 1 - Teoría de Algoritmos

### Grupo
* La Rosa, Martina - 97056
* Valsagna Indri, Federico Martín - 106010
* Riedel, Nicolás Agustín - 102130
* La Torre, Gabriel - 87796

### Requerimientos previos 
* Python 3.6 o superior

### Estructura del repositorio
El repositorio cuenta con 4 directorios principales, cada uno haciendo referencia a un ejercicio del enunciado.

```
TP-TDA/
├── ejercicio_1/
│   ├── main.py              # Implementación principal
│   ├── tests.py             # Suite de pruebas
│   ├── generateData.py      # Generador de casos de prueba
│   └── times.txt            # Log de tiempos de ejecución
├── ejercicio_2/
├── ejercicio_3/
├── ejercicio_4/
└── Graficos/
    ├── graficos.ipynb       # Notebook con análisis
    └── graficos.pdf         # Gráficos exportados
```

Dentro de cada directorio de ejercicio se encuentran 3 archivos principales:
- `main.py`: La implementación principal del algoritmo
- `tests.py`: Suite de pruebas para validar la correctness y medir performance
- `generateData.py`: Archivo auxiliar utilizado por `tests.py` para generar los casos de prueba

Luego de cada ejecución de `tests.py`, se genera un archivo llamado `times.txt` donde se registran los tiempos de ejecución de cada conjunto de pruebas.

### ¿Cómo correr los tests?
1. Navegar dentro de la carpeta deseada, por ejemplo:
   ```bash
   cd ejercicio_1
   ```
2. Ejecutar el suite de tests:
   ```bash
   python tests.py
   ```

### Gráficos
Los gráficos fueron generados usando Google Colab.
Se puede ver el notebook exportado en `/Graficos`.
