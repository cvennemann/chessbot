import chess
from chess import Board, Move, square_name
from beepduel.BeepDuel import get_best_move


def test_should_capture_hanging_piece():
    board: Board = Board()
    board.set_board_fen("K7/8/8/3r4/3R4/8/8/7k")
    expected_move: Move = Move(chess.D4, chess.D5)

    played_move: Move = get_best_move(board).move

    assert square_name(played_move.from_square) == square_name(expected_move.from_square)
    assert square_name(played_move.to_square) == square_name(expected_move.to_square)
    assert played_move == expected_move
