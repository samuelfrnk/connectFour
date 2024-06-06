import tkinter as tk
from tkinter import messagebox

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
                button = tk.Button(self.board_frame, text=" ", width=4, height=2,
                                   command=lambda c=col: self.on_button_click(c))
                button.grid(row=row, column=col, padx=2, pady=2)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.column_clicked_var = tk.IntVar()

    def update_board(self, board):
        for row in range(6):
            for col in range(7):
                piece = board.grid[row][col]
                if piece == 'x':
                    text = "X"
                    bg_color = "light blue"
                elif piece == 'o':
                    text = "O"
                    bg_color = "light gray"
                else:
                    text = " "
                    bg_color = "white"
                self.buttons[row][col].configure(text=text, bg=bg_color)

    def display_game(self, board):
        self.update_board(board)
        self.root.update()

    def get_player_move(self):
        self.root.wait_variable(self.column_clicked_var)
        column_choice = self.column_clicked
        self.column_clicked = None
        return column_choice

    def announce_winner(self, winner):
        messagebox.showinfo("Game Over", f"{winner} wins!")

    def announce_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")

    def on_button_click(self, column):
        self.column_clicked = column
        self.column_clicked_var.set(1)
