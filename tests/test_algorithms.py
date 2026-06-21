"""Unit and integration tests for Minimax and Alpha-Beta algorithms."""
import math
from src.game_tree import sample_tree, medium_tree, ordered_tree_for_pruning
from src.minimax import minimax
from src.alpha_beta import alpha_beta

def test_minimax_sample_tree():
    tree = sample_tree()
    assert minimax(tree, True) == 3

def test_alpha_beta_sample_tree():
    tree = sample_tree()
    assert alpha_beta(tree, -math.inf, math.inf, True) == 3

def test_algorithms_match_medium_tree():
    """Ambos algoritmos deben devolver el mismo resultado exacto."""
    tree = medium_tree()
    res_minimax = minimax(tree, True)
    res_ab = alpha_beta(tree, -math.inf, math.inf, True)
    assert res_minimax == res_ab == 7

def test_algorithms_match_ordered_tree():
    tree = ordered_tree_for_pruning()
    res_minimax = minimax(tree, True)
    res_ab = alpha_beta(tree, -math.inf, math.inf, True)
    assert res_minimax == res_ab == 8

def test_main_execution(capsys):
    """Prueba de Integración: Valida que main.py corra de extremo a extremo."""
    from src.main import run_analysis
    run_analysis()
    captured = capsys.readouterr()
    assert "AUDITORÍA DE RENDIMIENTO" in captured.out
    assert "ÉXITO ✅" in captured.out