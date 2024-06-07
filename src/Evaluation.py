
# Max is considered the AI player and Min the human player.
class Evaluation:
    def __init__(self):
        pass

    @staticmethod
    def evaluation_function(board):
        if board.is_game_over():
            if board.player_won("x"):
                return -10000
            elif board.player_won("o"):
                return 10000
            else:
                return 0
        else:
            evaluation = 0
            evaluation += analyze_connected_tiles(board)
            return evaluation



def analyze_connected_tiles(board):
    grid = board.get_grid()
    x_count = 0
    o_count = 0
    weight_3_connected = 10

    # Check horizontal connections
    for row in range(board.rows):
        for col in range(board.columns - 3):
            window = grid[row][col:col + 4]
            x_count += window.count('x')
            o_count += window.count('o')
            if window.count('x') == 3 and window.count(' ') == 1:
                x_count += weight_3_connected
            if window.count('o') == 3 and window.count(' ') == 1:
                o_count += weight_3_connected

    # Check vertical connections
    for col in range(board.columns):
        for row in range(board.rows - 3):
            window = [grid[row+i][col] for i in range(4)]
            x_count += window.count('x')
            o_count += window.count('o')
            if window.count('x') == 3 and window.count(' ') == 1:
                x_count += weight_3_connected
            if window.count('o') == 3 and window.count(' ') == 1:
                o_count += weight_3_connected

    # Check positive diagonal connections
    for row in range(board.rows - 3):
        for col in range(board.columns - 3):
            window = [grid[row+i][col+i] for i in range(4)]
            x_count += window.count('x')
            o_count += window.count('o')
            if window.count('x') == 3 and window.count(' ') == 1:
                x_count += weight_3_connected
            if window.count('o') == 3 and window.count(' ') == 1:
                o_count += weight_3_connected

    # Check negative diagonal connections
    for row in range(3, board.rows):
        for col in range(board.columns - 3):
            window = [grid[row-i][col+i] for i in range(4)]
            x_count += window.count('x')
            o_count += window.count('o')
            if window.count('x') == 3 and window.count(' ') == 1:
                x_count += weight_3_connected
            if window.count('o') == 3 and window.count(' ') == 1:
                o_count += weight_3_connected

    return o_count * 10 - x_count * 10
