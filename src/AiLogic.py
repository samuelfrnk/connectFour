import random
import math
from Evaluation import Evaluation


class AiLogic:
    def __init__(self):
        pass

    def choose_move(self, board, depth):
        move, value = self.minimax_alpha_beta(board, depth, -math.inf, math.inf, True)
        print("value", value)
        print("move", move)
        return move

    def minimax_alpha_beta(self, board, depth, alpha, beta, isMaximizing):
        valid_moves = board.get_valid_moves()

        if depth == 0 or board.is_game_over():
            return None, Evaluation.evaluation_function(board)

        if isMaximizing:
            value = -math.inf
            move = random.choice(valid_moves)
            for col in valid_moves:
                b_copy = board.copy()
                b_copy.register_ai_move(col)
                new_score = self.minimax_alpha_beta(b_copy, depth - 1, alpha, beta, not isMaximizing)[1]
                if new_score > value:
                    value = new_score
                    move = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return move, value
        else: # Minimizing player
            value = math.inf
            move = random.choice(valid_moves)
            for col in valid_moves:
                b_copy = board.copy()
                b_copy.register_player_move(col)
                new_score = self.minimax_alpha_beta(b_copy, depth - 1, alpha, beta, not isMaximizing)[1]
                if new_score < value:
                    value = new_score
                    move = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return move, value

