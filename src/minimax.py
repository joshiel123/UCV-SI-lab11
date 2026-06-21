"""Minimax algorithm implementation."""
import math
from src.game_tree import GameTree

def minimax(node: GameTree, is_maximizing: bool) -> int:
    """
    Evalúa un árbol de juego usando el algoritmo Minimax clásico.
    """
    # Condición de parada: Si el nodo es una hoja (entero), retorna su valor
    if isinstance(node, int):
        return node
    
    if is_maximizing:
        best_val = -math.inf
        for child in node:
            value = minimax(child, False)
            best_val = max(best_val, value)
        return int(best_val)
    else:
        best_val = math.inf
        for child in node:
            value = minimax(child, True)
            best_val = min(best_val, value)
        return int(best_val)