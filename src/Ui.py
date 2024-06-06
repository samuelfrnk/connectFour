import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class UI:
    def __init__(self):
        self.column_clicked = None
        self.root = tk.Tk()
        self.root.title("Connect Four")

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.buttons = []
        for row in range(6):
            row_buttons = []
            for col in range(7):
                button = tk.Button(self.board_frame, text=" ", width=2, height=1,
                                   command=lambda c=col: self.on_button_click(c))
                button.grid(row=row, column=col, padx=2, pady=2)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.current_player = 'x'

    def on_button_click(self, column):
        """Callback function for when a column button is clicked."""
        if not self.board.is_game_over():
            move_made = self.board.register_player_move(column)
            if move_made:
                self.update_board()
                self.switch_player()

                if not self.board.is_game_over() and not self.board.is_full():
                    self.ai_move()

    def update_board(self):
        """Update the GUI with the current state of the board."""
        for row in range(6):
            for col in range(7):
                piece = self.board.grid[row][col]
                text = "X" if piece == "x" else "O" if piece == "o" else " "
                self.buttons[row][col].configure(text=text)


    def ai_move(self):
        """Perform the AI move."""
        move = self.ai_logic.choose_move(self.board)
        self.board.register_ai_move(move)
        self.update_board()
        self.switch_player()

    def display_game(self, board):
        """Display the Connect Four board."""
        self.board = board
        self.update_board()
        self.root.update()

    def get_player_move(self):
        """Prompt the user to input a column choice."""
        self.root.wait_window(self.root)  # Wait for button click
        column_choice = self.column_clicked
        self.column_clicked = None  # Reset column_clicked for next move
        return column_choice

    def announce_winner(self, winner):
        """Announce the winner of the game."""
        messagebox.showinfo("Game Over", f" {winner} wins!")

    def announce_draw(self):
        """Announce a draw."""
        messagebox.showinfo("Game Over", "It's a draw!")




