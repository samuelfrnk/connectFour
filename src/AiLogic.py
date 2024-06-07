import random


class AiLogic:
    def __init__(self):
        pass

    def choose_move(self, board, depth):
        valid_moves = [col for col in range(board.columns) if board.is_valid_move(col)]
        return random.choice(valid_moves) if valid_moves else None
