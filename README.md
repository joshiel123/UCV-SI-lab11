# UCV-SI-lab11: Búsqueda Adversaria (Minimax y Poda Alfa-Beta)

[![CI Pipeline](https://img.shields.io/badge/CI%20Pipeline-success-green?logo=github)](https://github.com/joshiel123/UCV-SI-lab11/actions)
[![SonarCloud Quality Gate](https://img.shields.io/badge/SonarCloud-Passed-brightgreen?logo=sonarcloud)](https://sonarcloud.io/dashboard?id=joshiel123_UCV-SI-lab11)
[![SonarCloud Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen?logo=sonarcloud)](https://sonarcloud.io/dashboard?id=joshiel123_UCV-SI-lab11)

Este repositorio contiene la implementación y análisis de algoritmos de búsqueda adversaria para el laboratorio de Inteligencia Artificial. Se comparan el algoritmo clásico **Minimax** y su versión optimizada **Poda Alfa-Beta**, además de resolver el reto adicional mediante la creación de un juego de Tres en Raya con un agente de IA invencible.

---

## 1. Introducción teórica

### Algoritmo Minimax
Minimax es un método de decisión empleado en teoría de juegos y toma de decisiones en inteligencia artificial. Su objetivo es encontrar el movimiento óptimo para un jugador, asumiendo que el oponente también juega de manera óptima. Evalúa recursivamente el árbol de juego alternando turnos de maximización (nuestro turno) y minimización (turno del oponente).

### Poda Alfa-Beta
La Poda Alfa-Beta es una optimización del algoritmo Minimax que reduce drásticamente el número de nodos evaluados en el árbol de búsqueda sin alterar el resultado final. Utiliza dos valores de control:
- **Alfa ($\alpha$)**: La mejor opción encontrada hasta el momento para el jugador Maximizado (cota inferior).
- **Beta ($\beta$)**: La mejor opción encontrada hasta el momento para el jugador Minimizado (cota superior).

Si en algún subárbol se detecta que $\beta \leq \alpha$, se detiene la exploración de esa rama (poda) debido a que el jugador previo ya tiene garantizada una mejor opción por otra vía.

---

## 2. Estructura del Repositorio

El proyecto se encuentra estructurado de la siguiente forma:

```text
UCV-SI-lab11/
├── src/
│   ├── __init__.py
│   ├── alpha_beta.py        # Implementación genérica del algoritmo Poda Alfa-Beta
│   ├── game_tree.py         # Definición de la estructura de árbol de juego y muestras
│   ├── main.py              # Punto de entrada de análisis de rendimiento de árboles
│   ├── minimax.py           # Implementación genérica del algoritmo Minimax clásico
│   └── tres_en_raya.py      # [RETO] Lógica de Tres en Raya (POO) y juego interactivo
├── tests/
│   ├── __init__.py
│   ├── test_algorithms.py   # Pruebas para algoritmos en árboles de juego base
│   └── test_tres_en_raya.py # [RETO] Pruebas unitarias para el Tres en Raya
├── requirements.txt         # Dependencias del entorno de Python
├── sonar-project.properties # Configuración del análisis de SonarCloud
└── README.md                # Documentación del proyecto
```

---

## 3. Estado de la Integración Continua (CI)

- **GitHub Actions (CI/CD)**: Configurado para ejecutar el análisis sintáctico y las pruebas unitarias automáticamente con cada push a la rama principal. El estado actual es **Success ✅**.
- **SonarCloud**: La calidad de código y cobertura del proyecto superan el Quality Gate. Logramos un **100% de cobertura de código** mediante pruebas unitarias exhaustivas en todos los algoritmos y lógica matemática del juego.

---

## 4. Reto Adicional: Tres en Raya (Tic-Tac-Toe)

Se ha implementado el clásico juego del Tres en Raya en consola dentro de la clase `TresEnRaya` en `src/tres_en_raya.py`.

### Comportamiento de la IA
La computadora actúa como el agente inteligente de forma **invencible**. Para ello, utiliza el algoritmo Minimax con Poda Alfa-Beta para evaluar cada posible jugada hasta el final del juego, garantizando que el usuario humano nunca pueda ganarle (solo se obtienen empates o victorias para la IA).

### Mapeo de la Consola
El tablero está representado por una lista de 9 posiciones. Para interactuar con el juego en la consola, las posiciones se mapean del **1 al 9** de la siguiente manera:

```text
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
```

### Ejecutar el Juego de Consola
Para jugar interactivamente contra la IA en tu terminal, ejecuta el siguiente comando:

```bash
python src/tres_en_raya.py
```

---

## 5. Instalación y Ejecución Local

Sigue estos pasos para configurar tu entorno y correr las pruebas locales:

### Paso 1: Configurar el Entorno Virtual (Recomendado)
En tu consola, crea e inicializa un entorno virtual de Python:

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual (Windows)
.venv\Scripts\activate

# Activar entorno virtual (Linux/macOS)
source .venv/bin/activate
```

### Paso 2: Instalar Dependencias
Instala los paquetes necesarios definidos en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar las Pruebas Unitarias
Para correr toda la suite de pruebas unitarias y verificar el reporte de cobertura de código (que alcanza el 100%):

```bash
pytest --cov=src --cov-report=term-missing
```