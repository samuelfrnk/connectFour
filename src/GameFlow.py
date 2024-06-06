from Ui import UI
from AiLogic import AiLogic


class GameFlow:
    def __init__(self, ui, ai_logic, board):
        self.ui = ui
        self.ai_logic = ai_logic
        self.board = board
        self.is_human_players_turn = True
        self.is_game_over = False

    def start(self):
        self.ui.display_game(self.board)
        while not self.is_game_over:
            if self.is_human_players_turn:
                move = self.ui.get_player_move()
                self.board.register_player_move(move)
            else:
                move = self.ai_logic.choose_move(self.board)
                self.board.register_ai_move(move)
            self.ui.display_game(self.board)






