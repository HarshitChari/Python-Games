from tkinter import *
import numpy as np

size_of_board = 800
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 30
symbol_X_color = '#fff'
symbol_O_color = '#000000'

class Tic_Tac_Toe():
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window,
                             width=size_of_board,
                             bg='#E1306C',
                             height=size_of_board)
        self.canvas.pack()
        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0
