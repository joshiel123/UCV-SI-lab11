# UCV-SI-lab11: Búsqueda Adversaria (Minimax y Poda Alfa-Beta)

[![CI Pipeline](https://img.shields.io/badge/CI%20Pipeline-success-green?logo=github)](https://github.com/joshiel123/UCV-SI-lab11/actions)
[![SonarCloud Quality Gate](https://img.shields.io/badge/SonarCloud-Passed-brightgreen?logo=sonarcloud)](https://sonarcloud.io/dashboard?id=joshiel123_UCV-SI-lab11)
[![SonarCloud Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen?logo=sonarcloud)](https://sonarcloud.io/dashboard?id=joshiel123_UCV-SI-lab11)

Este repositorio contiene la implementación y análisis comparativo de algoritmos de búsqueda adversaria para el laboratorio de Inteligencia Artificial. El proyecto se compone de dos partes fundamentales:

1. **Comparador y Auditoría de Rendimiento**: Evaluación de árboles de juego genéricos mediante Minimax y Poda Alfa-Beta tradicionales.
2. **Reto Adicional (Tres en Raya)**: Un juego interactivo de Tres en Raya (Tic-Tac-Toe) por consola con una IA invencible usando la estructura de Programación Orientada a Objetos (POO).

---

## 1. Introducción Teórica

### Algoritmo Minimax

Minimax es un método de decisión utilizado en teoría de juegos de suma cero e información perfecta. Su objetivo principal es encontrar la jugada óptima asumiendo que el rival también juega óptimamente. El algoritmo desciende recursivamente por el árbol de juego alternando entre turnos de **Maximización** (nuestro mejor escenario) y **Minimización** (el peor escenario impuesto por el rival).

### Poda Alfa-Beta

La Poda Alfa-Beta es una optimización del algoritmo Minimax clásico que reduce drásticamente el número de nodos evaluados sin alterar el resultado del juego. Emplea dos cotas durante la búsqueda recursiva:

- **Alfa ($\alpha$)**: El mejor puntaje (máximo) asegurado hasta el momento para el maximizador.
- **Beta ($\beta$)**: El mejor puntaje (mínimo) asegurado hasta el momento para el minimizador.

Si durante la recursión se cumple que $\beta \leq \alpha$, se poda el subárbol restante, omitiendo cálculos innecesarios.

---

## 2. Estructura del Repositorio

```text
UCV-SI-lab11/
├── src/
│   ├── __init__.py
│   ├── alpha_beta.py        # Algoritmo de Poda Alfa-Beta para árboles de juego genéricos
│   ├── game_tree.py         # Estructuras de árboles de juego (Simple, Mediano, Optimizado)
│   ├── main.py              # Auditoría de rendimiento y comparador de velocidad de algoritmos
│   ├── minimax.py           # Algoritmo de Minimax clásico para árboles de juego genéricos
│   └── tres_en_raya.py      # [RETO] Lógica de Tres en Raya (POO) y juego interactivo
├── tests/
│   ├── __init__.py
│   ├── test_algorithms.py   # Pruebas unitarias/integración para algoritmos de árboles genéricos
│   └── test_tres_en_raya.py # [RETO] Pruebas unitarias para Tres en Raya
├── requirements.txt         # Dependencias necesarias para ejecutar el proyecto (pytest, pytest-cov)
├── sonar-project.properties # Configuración del análisis de SonarCloud
└── README.md                # Documentación del proyecto (este archivo)
```

---

## 3. Parte 1: Comparador y Auditoría de Rendimiento

El proyecto modela árboles de juego genéricos mediante tipos anidados utilizando Python TypeAlias:
`GameTree = int | list["GameTree"]`. Las hojas del árbol representan los puntajes de evaluación final y las sublistas representan las ramas.

### Árboles de Prueba Implementados (`src/game_tree.py`):

1. **Árbol Simple**: `[[3, 5], [2, 9]]` (Evaluación de 2 niveles).
2. **Árbol Mediano**: `[[[3, 5], [6, 9]], [[1, 2], [0, -1]], [[7, 4], [8, 6]]]` (Evaluación de 3 niveles).
3. **Árbol Optimizado para Poda**: `[[[10, 9], [8, 7]], [[6, 5], [4, 3]], [[2, 1], [0, -1]]]` (Ordenado estratégicamente para maximizar las podas).

### Ejecutar el Analizador de Rendimiento:

Para comparar la consistencia y la velocidad (en milisegundos) de ambos algoritmos en estos árboles estáticos, ejecuta:

```bash
python src/main.py
```

El script imprimirá un reporte detallado con el siguiente formato:

```text
============================================================
      AUDITORÍA DE RENDIMIENTO: MINIMAX VS PODA ALFA-BETA
============================================================

[+] Analizando: Árbol Simple
  -> Minimax Clásico : Resultado = 3 | Tiempo = 0.0150 ms
  -> Poda Alfa-Beta   : Resultado = 3 | Tiempo = 0.0120 ms
  -> Verificación de Consistencia: ÉXITO ✅

[+] Analizando: Árbol Mediano
  -> Minimax Clásico : Resultado = 7 | Tiempo = 0.0450 ms
  -> Poda Alfa-Beta   : Resultado = 7 | Tiempo = 0.0380 ms
  -> Verificación de Consistencia: ÉXITO ✅
```

---

## 4. Parte 2: Reto Adicional - Tres en Raya (Tic-Tac-Toe)

La lógica del juego clásico está encapsulada en la clase `TresEnRaya` dentro de `src/tres_en_raya.py`.

### Inteligencia Artificial Invencible

El agente de computadora ejecuta una versión adaptada del algoritmo Minimax con poda Alfa-Beta para calcular el mejor movimiento posible basándose en la profundidad actual. El sistema penaliza las derrotas y beneficia las victorias más rápidas mediante una puntuación dinámica:

- **Victoria IA**: `10 - profundidad`
- **Victoria Humano**: `-10 + profundidad`
- **Empate**: `0`

Esto resulta en un oponente perfecto al que **es imposible ganarle**.

### Formato y Mapeo en Consola

El tablero interactivo se representa en consola con casillas numeradas del **1 al 9**:

```text
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

### Ejecutar el Juego de Tres en Raya:

Para iniciar una partida contra la IA en tu terminal:

```bash
python src/tres_en_raya.py
```

---

## 5. Pruebas Unitarias y Cobertura (CI/CD)

El proyecto cuenta con integración continua configurada en GitHub Actions y SonarCloud. La cobertura de código en todo el proyecto es del **100%**.

### Instalar dependencias locales:

```bash
# Crear entorno virtual
python -m venv .venv
# Activar entorno virtual (Windows)
.venv\Scripts\activate
# Activar entorno virtual (Linux/macOS)
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Correr las pruebas unitarias y generar reporte de cobertura:

Para ejecutar todos los tests (`test_algorithms.py` y `test_tres_en_raya.py`):

```bash
pytest --cov=src --cov-report=term-missing
```

Esto generará el reporte en terminal demostrando la consistencia de los resultados y que todas las líneas de código (excepto el bucle de ejecución directa del juego de consola marcado con `# pragma: no cover`) están completamente valida das.
