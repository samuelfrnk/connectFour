class GameFlow:
    def __init__(self, ui, ai_logic, board):
        self.ui = ui
        self.ai_logic = ai_logic
        self.board = board
        self.is_human_players_turn = True

    def start(self):
        while not self.board.is_game_over():
            self.ui.display_game(self.board)
            if self.is_human_players_turn:
                move = self.ui.get_player_move()
                if move is not None:
                    self.board.register_player_move(move)
                    self.is_human_players_turn = False
            else:
                move = self.ai_logic.choose_move(self.board)
                self.board.register_ai_move(move)
                self.is_human_players_turn = True

            if self.board.is_game_over():
                self.ui.display_game(self.board)
                if self.board.player_won('x'):
                    self.ui.announce_winner('Player')
                elif self.board.player_won('o'):
                    self.ui.announce_winner('AI')
                else:
                    self.ui.announce_draw()
                break

        self.ui.root.mainloop()
