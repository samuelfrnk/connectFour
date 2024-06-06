from Ui import UI
from GameFlow import GameFlow
from AiLogic import AiLogic
from Board import Board


class ConnectFourGame:
    def __init__(self):
        self.ui = UI()
        self.ai_logic = AiLogic()
        self.board = Board()
        self.game_flow = GameFlow(self.ui, self.ai_logic, self.board)

    def run(self):
        self.game_flow.start()


if __name__ == "__main__":
    game = ConnectFourGame()
    game.run()
    # game.run()

