from Evaluation import Evaluation


class GameFlow:
    def __init__(self, ui, ai_logic, board):
        self.ui = ui
        self.ai_logic = ai_logic
        self.board = board
        self.is_human_players_turn = True
        self.depth_level = 4

    def start(self):
        while not self.board.is_game_over():
            self.ui.display_game(self.board)
            if self.is_human_players_turn:
                move = self.ui.get_player_move()
                # print("HUMAN ", move)
                if move is not None:
                    self.board.register_player_move(move)
                    self.is_human_players_turn = False
            else:
                move = self.ai_logic.choose_move(self.board, self.depth_level)
                # print("AI ",move)
                self.board.register_ai_move(move)
                self.is_human_players_turn = True
            print(Evaluation.evaluation_function(self.board))
            self.board.print_board()
            if self.board.is_game_over():
                self.ui.display_game(self.board)
                if self.board.player_won('x'):
                    self.ui.announce_winner('Human')
                elif self.board.player_won('o'):
                    self.ui.announce_winner('AI')
                else:
                    self.ui.announce_draw()
                break

        self.ui.root.mainloop()

    def adjust_depth_level(self, level):
        self.depth_level = level
