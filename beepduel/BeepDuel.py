import logging
import random
import logging

from chess import Move, Board, SQUARES, WHITE, BLACK, square_name
from chess.engine import PlayResult

piece_values = {
    1: 1,
    2: 3,
    3: 3,
    4: 5,
    5: 9,
    6: 0
}


def get_best_move(board: Board, *args) -> PlayResult:
    MAX_DEPTH = 2

    evaluations = []

    for move in board.legal_moves:
        logging.info(f"starting evaluation for root move {square_name(move.from_square)}{square_name(move.to_square)}")

        board.push(move)
        evaluation: int = minimax(board, 0, MAX_DEPTH)
        board.pop()

        evaluations.append((move, evaluation))
        logging.info(f"evaluation: {evaluation}")

    evaluations.sort(key=lambda entry: entry[1])
    if board.turn == WHITE:
        evaluations.reverse()

    selected_move = random_best_move(evaluations)
    logging.info(f"selected move: {square_name(selected_move.from_square)}-{square_name(selected_move.to_square)}")

    return PlayResult(selected_move, None)


def minimax(board: Board, current_depth: int, max_depth: int) -> int:
    current_depth += 1

    if board.is_checkmate():
        evaluation = 1000 if board.turn == BLACK else -1000
    elif current_depth == max_depth:
        evaluation = material_difference(board)
    else:
        evaluations = []
        for move in board.legal_moves:
            logging.info(f"{square_name(move.from_square)}{square_name(move.to_square)}")
            board.push(move)
            evaluation = minimax(board, current_depth, max_depth)
            board.pop()
            evaluations.append(evaluation)
        evaluation = max(evaluations) if board.turn == WHITE else min(evaluations)

    return evaluation


def random_best_move(evaluations: [(Move, int)]) -> Move:
    if len(evaluations) == 1:
        return evaluations[0][0]

    best_eval: int = evaluations[0][1]
    number_of_equal_moves = 1

    for i in range(1, len(evaluations)):
        number_of_equal_moves += 1
        if evaluations[i][1] != best_eval:
            number_of_equal_moves = i
            break

    choose = random.randrange(0, number_of_equal_moves)
    return evaluations[choose][0]


def material_difference(board: Board):
    white = 0
    black = 0
    for square in SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = piece_values[piece.piece_type]
            if piece.color == WHITE:
                white += value
            else:
                black += value

    return white - black
