import chess
from chess.engine import PlayResult
from chess import Board
import pytest
from beepduel.BeepDuel import get_best_move


def test_should_find_back_rank_mate():
    board: Board = Board()
    board.set_board_fen("3k4/8/3K1R2/8/8/8/8/8")
    expected_move = chess.Move(chess.F6, chess.F8)

    played_move: PlayResult = get_best_move(board)

    assert played_move.move.from_square == expected_move.from_square
    assert played_move.move.to_square == expected_move.to_square
