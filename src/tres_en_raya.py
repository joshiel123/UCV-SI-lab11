"""Módulo para el juego clásico de Tres en Raya (Tic-Tac-Toe) con IA invencible."""

import math
from typing import List, Optional, Tuple


class TresEnRaya:
    """Clase que encapsula la lógica matemática y de estado de Tres en Raya."""

    def __init__(self, board: Optional[List[str]] = None, ai_player: str = "O", human_player: str = "X") -> None:
        """
        Inicializa una partida de Tres en Raya.

        :param board: Tablero inicial como lista de 9 caracteres. Si es None, se crea vacío.
        :param ai_player: Símbolo usado por la inteligencia artificial (por defecto 'O').
        :param human_player: Símbolo usado por el jugador humano (por defecto 'X').
        """
        self.ai_player = ai_player
        self.human_player = human_player
        self.board = board if board is not None else [" "] * 9

    def reset(self) -> None:
        """Restablece el tablero a su estado inicial vacío."""
        self.board = [" "] * 9

    def get_empty_positions(self, board: Optional[List[str]] = None) -> List[int]:
        """
        Retorna la lista de índices (0-8) correspondientes a casillas vacías en el tablero.

        :param board: Tablero a evaluar. Si es None, usa el de la instancia.
        """
        target_board = board if board is not None else self.board
        return [i for i, val in enumerate(target_board) if val == " "]

    def is_board_full(self, board: Optional[List[str]] = None) -> bool:
        """
        Determina si el tablero está lleno (no hay casillas vacías).

        :param board: Tablero a evaluar. Si es None, usa el de la instancia.
        """
        target_board = board if board is not None else self.board
        return " " not in target_board

    def make_move(self, position: int, player: str, board: Optional[List[str]] = None) -> bool:
        """
        Realiza un movimiento para un jugador en la posición indicada.

        :param position: Índice de la casilla (0-8).
        :param player: Símbolo del jugador ('X' o 'O').
        :param board: Tablero sobre el que realizar el movimiento. Si es None, usa el de la instancia.
        :return: True si el movimiento se realizó exitosamente, False si no era válido.
        """
        target_board = board if board is not None else self.board
        if 0 <= position < 9 and target_board[position] == " ":
            target_board[position] = player
            return True
        return False

    def check_winner(self, board: Optional[List[str]] = None) -> Optional[str]:
        """
        Verifica si hay algún ganador en el tablero actual.

        :param board: Tablero a evaluar. Si es None, usa el de la instancia.
        :return: El símbolo del ganador ('X' o 'O') si hay uno; de lo contrario, None.
        """
        target_board = board if board is not None else self.board
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontales
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticales
            (0, 4, 8), (2, 4, 6)              # Diagonales
        ]
        for combo in win_conditions:
            if target_board[combo[0]] != " " and target_board[combo[0]] == target_board[combo[1]] == target_board[combo[2]]:
                return target_board[combo[0]]
        return None

    def is_game_over(self, board: Optional[List[str]] = None) -> bool:
        """
        Determina si el juego ha terminado.

        :param board: Tablero a evaluar. Si es None, usa el de la instancia.
        :return: True si hay un ganador o el tablero está lleno, False en caso contrario.
        """
        return self.check_winner(board) is not None or self.is_board_full(board)

    def minimax(
        self,
        board: List[str],
        depth: int,
        is_maximizing: bool,
        alpha: float = -math.inf,
        beta: float = math.inf
    ) -> Tuple[int, int]:
        """
        Algoritmo Minimax optimizado con Poda Alfa-Beta.

        :param board: El estado del tablero a evaluar.
        :param depth: Profundidad de búsqueda actual.
        :param is_maximizing: True si le toca a la IA, False si le toca al oponente.
        :param alpha: Cota inferior de la puntuación para maximizar.
        :param beta: Cota superior de la puntuación para minimizar.
        :return: Tupla con (mejor puntuación, mejor movimiento).
        """
        winner = self.check_winner(board)
        if winner == self.ai_player:
            return 10 - depth, -1
        if winner == self.human_player:
            return -10 + depth, -1
        if self.is_board_full(board):
            return 0, -1

        empty_positions = self.get_empty_positions(board)
        best_move = -1

        if is_maximizing:
            best_score = -math.inf
            for move in empty_positions:
                board[move] = self.ai_player
                score, _ = self.minimax(board, depth + 1, False, alpha, beta)
                board[move] = " "  # Deshacer movimiento
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return int(best_score), best_move
        else:
            best_score = math.inf
            for move in empty_positions:
                board[move] = self.human_player
                score, _ = self.minimax(board, depth + 1, True, alpha, beta)
                board[move] = " "  # Deshacer movimiento
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return int(best_score), best_move

    def get_best_move(self) -> int:
        """
        Calcula y retorna el mejor movimiento para la IA en el estado actual del juego.

        :return: Índice del mejor movimiento (0-8).
        """
        temp_board = list(self.board)
        _, move = self.minimax(temp_board, 0, True)
        return move

    def print_board(self) -> None:
        """Imprime el tablero actual en la consola."""
        b = self.board
        print("\n")
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print("-----------")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("-----------")
        print(f" {b[6]} | {b[7]} | {b[8]} ")
        print("\n")


if __name__ == "__main__":  # pragma: no cover
    print("=======================================")
    print("     BIENVENIDO A TRES EN RAYA IA      ")
    print("=======================================")
    print("Juegas como 'X' y la IA juega como 'O'.")
    print("Las posiciones están enumeradas del 1 al 9:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

    game = TresEnRaya()
    current_turn = "X"  # Empieza el humano

    while not game.is_game_over():
        game.print_board()
        if current_turn == "X":
            try:
                move_input = input("Ingresa tu movimiento (1-9): ")
                pos = int(move_input) - 1
                if 0 <= pos < 9:
                    if game.make_move(pos, "X"):
                        current_turn = "O"
                    else:
                        print("¡Casilla ya ocupada! Intenta de nuevo.")
                else:
                    print("Por favor, ingresa un número válido del 1 al 9.")
            except ValueError:
                print("Entrada inválida. Debe ser un número entero entre 1 y 9.")
        else:
            print("Turno del agente de IA...")
            best_pos = game.get_best_move()
            if best_pos != -1:
                game.make_move(best_pos, "O")
            current_turn = "X"

    game.print_board()
    winner_player = game.check_winner()
    if winner_player == "X":
        print("¡Increíble! ¡Has ganado!")
    elif winner_player == "O":
        print("¡La IA ha ganado! Mejor suerte la próxima vez.")
    else:
        print("¡Es un empate!")
