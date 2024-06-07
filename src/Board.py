# AI players move are registered as o in the 2d board array, x for the human player
class Board:
    def __init__(self):
        self.columns = 7
        self.rows = 6
        self.grid = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]

    def print_board(self):
        print(" 0 1 2 3 4 5 6")
        for row in self.grid:
            print('|' + '|'.join(row) + '|')
        print('-' * 15)

    def register_ai_move(self, column):
        """Register AI move by adding 'o' to the specified column."""
        if self.is_valid_move(column):
            for row in reversed(range(self.rows)):
                if self.grid[row][column] == ' ':
                    self.grid[row][column] = 'o'
                    return True  # Move was successful
        return False  # Move was unsuccessful

    def register_player_move(self, column):
        """Register player move by adding 'x' to the specified column."""
        if self.is_valid_move(column):
            for row in reversed(range(self.rows)):
                if self.grid[row][column] == ' ':
                    self.grid[row][column] = 'x'
                    return True  # Move was successful
        return False  # Move was unsuccessful

    def is_valid_move(self, column):
        """Check if a move is valid (i.e., column is not full)."""
        return self.grid[0][column] == ' '

    def is_game_over(self):
        """Check if the game is over (either a player has won or the board is full)."""
        return self.player_won('o') or self.player_won('x') or self.is_full()

    def player_won(self, player):
        """Check if the specified player (AI or human) has won the game."""
        # Check horizontal, vertical, and diagonal directions for four consecutive player markers
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if self.grid[row][col] == self.grid[row][col + 1] == self.grid[row][col + 2] == self.grid[row][
                        col + 3] == player:
                    return True  # Horizontal win
        for col in range(self.columns):
            for row in range(self.rows - 3):
                if self.grid[row][col] == self.grid[row + 1][col] == self.grid[row + 2][col] == self.grid[row + 3][
                        col] == player:
                    return True  # Vertical win
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if self.grid[row][col] == self.grid[row + 1][col + 1] == self.grid[row + 2][col + 2] == \
                        self.grid[row + 3][col + 3] == player:
                    return True  # Diagonal \ win
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if self.grid[row][col] == self.grid[row - 1][col + 1] == self.grid[row - 2][col + 2] == \
                        self.grid[row - 3][col + 3] == player:
                    return True
        return False  # No win

    def is_full(self):
        """Check if the board is full (i.e., no empty spaces left)."""
        return all(cell != ' ' for row in self.grid for cell in row)

    def get_grid(self):
        """Return a copy of the grid."""
        return [row.copy() for row in self.grid]


