"""Main entry point to execute and compare adversarial search algorithms."""
import math
import time
from src.game_tree import sample_tree, medium_tree, ordered_tree_for_pruning
from src.minimax import minimax
from src.alpha_beta import alpha_beta

def run_analysis():
    """Ejecuta los algoritmos sobre los árboles base para comparar rendimiento."""
    trees = {
        "Árbol Simple": sample_tree(),
        "Árbol Mediano": medium_tree(),
        "Árbol Optimizado para Poda": ordered_tree_for_pruning()
    }
    
    print("=" * 60)
    print("      AUDITORÍA DE RENDIMIENTO: MINIMAX VS PODA ALFA-BETA")
    print("=" * 60)
    
    for name, tree in trees.items():
        print(f"\n[+] Analizando: {name}")
        
        # Evaluar Minimax Clásico
        start = time.perf_counter()
        res_minimax = minimax(tree, True)
        t_minimax = (time.perf_counter() - start) * 1000
        
        # Evaluar Poda Alfa-Beta
        start = time.perf_counter()
        res_ab = alpha_beta(tree, -math.inf, math.inf, True)
        t_ab = (time.perf_counter() - start) * 1000
        
        print(f"  -> Minimax Clásico : Resultado = {res_minimax} | Tiempo = {t_minimax:.4f} ms")
        print(f"  -> Poda Alfa-Beta   : Resultado = {res_ab} | Tiempo = {t_ab:.4f} ms")
        print(f"  -> Verificación de Consistencia: {'ÉXITO ✅' if res_minimax == res_ab else 'FALLO ❌'}")

if __name__ == "__main__":  # pragma: no cover
    run_analysis()