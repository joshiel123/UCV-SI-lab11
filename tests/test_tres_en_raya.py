"""Pruebas unitarias para la clase TresEnRaya."""

from src.tres_en_raya import TresEnRaya


def test_winner_detection():
    """Valida la correcta detección de estados de victoria en horizontal, vertical y diagonal."""
    # Victoria horizontal
    game = TresEnRaya(board=["X", "X", "X", " ", "O", "O", " ", " ", " "])
    assert game.check_winner() == "X"
    assert game.is_game_over() is True

    # Victoria vertical
    game = TresEnRaya(board=["O", "X", " ", "O", "X", " ", "O", " ", " "])
    assert game.check_winner() == "O"
    assert game.is_game_over() is True

    # Victoria diagonal
    game = TresEnRaya(board=["X", "O", " ", "O", "X", " ", " ", " ", "X"])
    assert game.check_winner() == "X"
    assert game.is_game_over() is True

    # Sin ganador
    game = TresEnRaya(board=["X", "O", "X", " ", "O", " ", " ", " ", " "])
    assert game.check_winner() is None
    assert game.is_game_over() is False


def test_ai_blocks_opponent():
    """Valida que la IA bloquee movimientos del oponente que llevarían a una derrota inmediata."""
    # Humano (X) está a punto de ganar en la fila 0: [X, X, vacío]
    # La IA (O) debe bloquear eligiendo el índice 2.
    game = TresEnRaya(board=["X", "X", " ", " ", "O", " ", " ", " ", " "])
    best_move = game.get_best_move()
    assert best_move == 2

    # Humano (X) está a punto de ganar en la columna 1: [1, 4, 7]
    # La IA (O) debe bloquear eligiendo el índice 7.
    game = TresEnRaya(board=["O", "X", " ", " ", "X", " ", " ", " ", " "])
    best_move = game.get_best_move()
    assert best_move == 7


def test_ai_wins_when_possible():
    """Valida que la IA tome la jugada ganadora si se presenta en el turno actual."""
    # La IA (O) tiene jugada ganadora en la fila 1: [O, O, vacío]
    game = TresEnRaya(board=["X", "X", " ", "O", "O", " ", " ", " ", " "])
    best_move = game.get_best_move()
    assert best_move == 5

    # La IA (O) tiene jugada ganadora en la diagonal principal: [0, 4, vacío]
    game = TresEnRaya(board=["O", " ", "X", " ", "O", "X", " ", " ", " "])
    best_move = game.get_best_move()
    assert best_move == 8


def test_is_board_full():
    """Valida que se identifique correctamente un tablero lleno (empate)."""
    game = TresEnRaya()
    assert game.is_board_full() is False

    game.board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert game.is_board_full() is True
    assert game.is_game_over() is True
    assert game.check_winner() is None  # Empate


def test_reset_and_make_move():
    """Valida los métodos auxiliares de reinicio y realización de movimientos."""
    game = TresEnRaya()
    assert game.make_move(0, "X") is True
    assert game.board[0] == "X"
    # Movimiento inválido en celda ocupada
    assert game.make_move(0, "O") is False
    # Movimiento fuera de límites
    assert game.make_move(9, "O") is False
    assert game.make_move(-1, "O") is False

    game.reset()
    assert game.board == [" "] * 9


def test_print_board(capsys):
    """Valida la correcta impresión del tablero."""
    game = TresEnRaya(board=["X", "O", "X", " ", " ", " ", " ", " ", " "])
    game.print_board()
    captured = capsys.readouterr()
    assert " X | O | X " in captured.out
    assert "-----------" in captured.out

