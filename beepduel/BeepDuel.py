import random
import chess
from chess.engine import PlayResult


def get_best_move(board: chess.Board, *args) -> PlayResult:
    for move in board.legal_moves:
        board.push(move)
        if board.is_checkmate():
            return PlayResult(move, None)
        board.pop()
    return PlayResult(random.choice(list(board.legal_moves)), None)