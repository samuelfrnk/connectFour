# Max is considered the AI player and Min the human player.
class Evaluation:
    def __init__(self):
        pass

    @staticmethod
    def evaluation_function(board, isMax):
        if board.is_game_over():
            if board.player_won("x"):
                return -10000
            elif board.player_won("o"):
                return 10000
            else:
                return 0
        else:
            evaluation = 0
            evaluation += analyze_connected_tiles(board, isMax)
            return evaluation


def analyze_connected_tiles(board, isMax):
    score = 0
    center_col_index = len(board.grid[0]) // 2
    center_array = [row[center_col_index] for row in board.grid]
    if isMax:
        center_count_o = center_array.count("o")
        score += center_count_o * 3
    else:
        center_count_x = center_array.count("x")
        score -= center_count_x * 3
    for r in range(board.rows):
        row_array = board.grid[r]
        for c in range(board.columns - 3):
            window = row_array[c:c + 4]
            score += evaluate_window(window, isMax)

    for c in range(board.columns):
        col_array = [board.grid[r][c] for r in range(len(board.grid))]
        for r in range(board.rows -3):
            window = col_array[r:r+4]
            score += evaluate_window(window, isMax)

    for r in range(board.rows - 3):
        for c in range(board.columns - 3):
            window = [board.grid[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, isMax)


    for r in range(board.rows - 3):
        for c in range(board.columns - 3):
            window = [board.grid[r + 3 - i][c + i] for i in range(4)]
            score += evaluate_window(window, isMax)

    return score

def evaluate_window(window, isMax):
    score = 0

    if isMax:
        if window.count("o") == 4:
            score += 100
        elif window.count("o") == 3 and window.count(" ") == 1:
            score += 5
        elif window.count("o") == 2 and window.count(" ") == 2:
            score += 2
        if window.count("x") == 3 and window.count(" ") == 1:
            score -= 4

    else:
        if window.count("x") == 4:
            score -= 100
        elif window.count("x") == 3 and window.count(" ") == 1:
            score -= 5
        elif window.count("x") == 2 and window.count(" ") == 2:
            score -= 2
        if window.count("o") == 3 and window.count(" ") == 1:
            score += 4
    return score
