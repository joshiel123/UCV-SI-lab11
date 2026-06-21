"""Alpha-Beta Pruning algorithm implementation."""
import math
from src.game_tree import GameTree

def alpha_beta(node: GameTree, alpha: float, beta: float, is_maximizing: bool) -> int:
    """
    Evalúa un árbol de juego usando Minimax optimizado con Poda Alfa-Beta.
    """
    # Condición de parada: Si el nodo es una hoja (entero), retorna su valor
    if isinstance(node, int):
        return node
    
    if is_maximizing:
        best_val = -math.inf
        for child in node:
            value = alpha_beta(child, alpha, beta, False)
            best_val = max(best_val, value)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break  # Poda Beta (el minimizador previo tiene una mejor opción)
        return int(best_val)
    else:
        best_val = math.inf
        for child in node:
            value = alpha_beta(child, alpha, beta, True)
            best_val = min(best_val, value)
            beta = min(beta, best_val)
            if beta <= alpha:
                break  # Poda Alfa (el maximizador previo tiene una mejor opción)
        return int(best_val)