import chess
from chess import Board, Move, square_name
from chess.engine import PlayResult

from beepduel.BeepDuel import get_best_move, minimax


def test_should_find_stalemate():
    board = Board()
    board.set_board_fen("rk6/p2K4/8/P7/8/8/8/8")
    expected_move = Move(chess.A5, chess.A6)

    played_move = get_best_move(board).move

    assert played_move == expected_move
