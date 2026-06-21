"""Game tree examples for the Minimax and Alpha-Beta laboratory."""
from typing import TypeAlias

# Definimos que un Árbol de Juego puede ser un número entero (hoja) 
# o una lista que contiene más Árboles de Juego (ramas).
GameTree: TypeAlias = int | list["GameTree"]

def sample_tree() -> GameTree:
    """Árbol básico de prueba."""
    return [[3, 5], [2, 9]]

def medium_tree() -> GameTree:
    """Árbol de profundidad 3 para pruebas más complejas."""
    return [[[3, 5], [6, 9]], [[1, 2], [0, -1]], [[7, 4], [8, 6]]]

def ordered_tree_for_pruning() -> GameTree:
    """Árbol ordenado de mayor a menor para forzar y demostrar 
    la máxima eficiencia de la Poda Alfa-Beta."""
    return [[[10, 9], [8, 7]], [[6, 5], [4, 3]], [[2, 1], [0, -1]]]