# TP 1 - Teoría de Algoritmos

Este repositorio contiene la implementación del trabajo práctico 1 de la materia Teoría de Algoritmos.

## Ejercicio 1: Búsqueda de Punto Fijo

### Descripción del Problema

Dado un array ordenado de enteros, encontrar un índice `i` tal que `arr[i] = i`. Si no existe tal índice, retornar -1.

### Implementación

El algoritmo está implementado en `Ejercicio 1/ej1.py` y utiliza búsqueda binaria para encontrar el punto fijo de manera eficiente.

## Ejercicio 3: Suma Máxima de Subarray Contiguo (Backtracking)

### Descripción del Problema

Encontrar la subsecuencia contigua de números que produzca la suma máxima utilizando un algoritmo de backtracking.

### Implementación

El algoritmo está implementado en `Ejercicio 3/ej3.py` y utiliza backtracking para explorar todas las posibles subsecuencias contiguas.

### Representación de Estados

- Los estados se representan como arrays binarios donde `1` indica que el elemento está incluido en la subsecuencia y `0` que no
- Ejemplo: `[0, 1, 1, 0, 0]` representa una subsecuencia que incluye los elementos en las posiciones 1 y 2

### Casos de Prueba

#### Ejercicio 1

El archivo `tests.py` genera y comprueba casos donde:

- Casos donde existe un punto fijo
- Casos donde no existe un punto fijo
- Arrays con elementos negativos
- Arrays de diferentes tamaños
- Casos límite

##### Ejemplos de Arrays de Prueba

```python
[-1, 0, 1, 3, 4]    # Resultado: 3 (arr[3] = 3)
[0, 1, 2, 3, 4, 5]  # Resultado: 2 (arr[2] = 2)
[-4, 2, 3, 4, 5]    # Resultado: -1 (no existe punto fijo)
```

#### Ejercicio 3

El archivo `tests.py` utiliza pytest y contiene tests para verificar:

- Subsecuencia de un solo elemento
- Subsecuencia de elementos del medio del array
- Subsecuencia que incluye todo el array

##### Ejemplos de Arrays de Prueba

```python
[-2, 10, -5, -3, -1]    # Resultado: suma=10, estado=[0,1,0,0,0]
[-5, -2, 3, 4, 5, -3, -6]  # Resultado: suma=12, estado=[0,0,1,1,1,0,0]  
[1, 3, 2, 4, 1]         # Resultado: suma=11, estado=[1,1,1,1,1]
```

## Cómo Ejecutar

### Requisitos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Configuración del Entorno

#### 1. Crear el entorno virtual

```bash
# En Windows (PowerShell)
py -m venv .venv

# En macOS/Linux
python3 -m venv .venv
```
Distintas versiones pueden funcionar según el python
instalado como `python`, `python3.7`, etc.

#### 2. Activar el entorno virtual

```bash
# En Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# En Windows (Command Prompt)
.venv\Scripts\activate.bat

# En macOS/Linux
source .venv/bin/activate
```

#### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecución de Tests

#### Ejercicio 1

```bash
cd "Ejercicio 1"
python tests.py
```

#### Ejercicio 3

```bash
cd "Ejercicio 3"

# Ejecutar con pytest (recomendado)
pytest tests.py -v

# O directamente
python tests.py
```