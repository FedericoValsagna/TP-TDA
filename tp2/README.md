# TP2 - Teoría de Algoritmos

## Instalación

### 1. Crear entorno virtual
```bash
python -m venv venv
```

### 2. Activar entorno virtual
**Windows:**
```bash
venv\Scripts\activate
```
**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
cd ejercicio_2
pip install -r requirements.txt
```

## Ejercicios

### Ejercicio 1 (Programación Lineal)
**Prerequisito:** Instalar GLPK (GNU Linear Programming Kit)
- Windows: Descargar de https://sourceforge.net/projects/winglpk/
- Linux: `sudo apt-get install glpk-utils`
- Mac: `brew install glpk`

En carpeta `ej1/`
- Modelo: `ej1.ltx`
- Resultado: `resultado.txt`
- Ejecutar: `glpsol --lp ej1.ltx -o resultado.txt`

### Ejercicio 2 (Flujo de Redes)
```bash
cd ejercicio_2
python ejercicio_2.py
```
O con archivo específico:
```bash
python ejercicio_2.py grafico.csv 1 10
```
(1=nodo fuente, 10=nodo sumidero)

### Ejercicio 3 (Next Fit)
```bash
cd ejercicio_3
python main.py
```

### Ejercicio 4 (Prueba de Conocimiento Cero)
```bash
cd ejercicio_4
python ej4.py
```

## Desactivar entorno virtual
```bash
deactivate
```
