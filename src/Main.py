from Ui import UI
from GameFlow import GameFlow
from AiLogic import AiLogic
from Board import Board

class ConnectFourGame:
    def __init__(self):
        self.ui = UI()
        self.ai_logic = AiLogic()
        self.board = Board()
        self.game_flow = GameFlow(self.ai_logic, self.ui, self.board)

    def run(self):
        while not self.game_flow.is_game_over():
            self.game_flow.play_turn()


if __name__ == "__main__":
    game = ConnectFourGame()
    game.run()
