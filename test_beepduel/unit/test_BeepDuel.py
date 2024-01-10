from chess import Board, Move
import pytest
from chess.engine import PlayResult

from beepduel.BeepDuel import random_best_move, material_difference, minimax


def test_should_return_random_move():
    move1 = Move(1, 2)
    move2 = Move(3, 4)
    move3 = Move(5, 6)

    evaluations = [
        (move1, 1),
        (move2, 3),
        (move3, 2)
    ]

    result: Move = random_best_move(evaluations)
    assert isinstance(result, Move)


def test_should_return_move_if_only_one_legal_move():
    move: Move = Move(1, 2)
    evaluations = [(move, 1)]

    expected_move: Move = random_best_move(evaluations)

    assert expected_move.from_square == move.from_square
    assert expected_move.to_square == move.to_square


def test_material_difference_should_be_0_for_starting_position():
    board = Board()
    difference = material_difference(board)
    assert difference == 0


def test_material_difference_should_be_minus_9_for_missing_queen():
    board = Board()
    board.set_board_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNB1KBNR")
    difference = material_difference(board)
    assert difference == -9


def test_minmax_depth_1_should_evaluate_material_difference():
    board = Board()
    board.set_board_fen("7k/8/8/8/1P6/8/8/K7")
    expected_evaluation = 1

    actual_evaluation = minimax(board, 1, 1)
    assert actual_evaluation == expected_evaluation

def test_minmax_depth_2_should_evaluate_material_difference():
    board = Board()
    board.set_board_fen("7k/8/8/8/1P6/8/8/K7")
    expected_evaluation = 1

    actual_evaluation = minimax(board, 1, 2)
    assert actual_evaluation == expected_evaluation
