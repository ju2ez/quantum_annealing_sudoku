""" A Python module to provide functionalities for a Quantum Annealing Sudoku """
from itertools import product

import numpy as np
class QuantumAnnealingSudoku:
    """
    Class with the necessary functions to embed a Sudoku on a Quantum Annealer.
    Credits belong to: FIND THE PROGAMMER OF THE CHECK_SUDOKU function!
    """

    def __init__(self, grid_9x9=True):
        """Possible choices: 9x9 or 4x4 grid
            If grid_9x9 is False: use a 4x4 grid
        """
        self.grid_9x9 = grid_9x9


    def check_sudoku(self, grid):
        """Validate a sudoku solution.
        Given a grid as a list of lists, return None if it is ill-formed,
        False if it is invalid, or True if it is a valid solution.
        """

        digits = set(range(1, 10))
        threes = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        grid_format=9


        if self.grid_9x9 is False:
            #use parameters for a 4x4 grid
            digits = set(range(1, 5))
            threes = [(0, 1), (2, 3)]
            grid_format=4

        error_count=0
        # Check that the grid is 4x4.
        if len(grid) != grid_format or not all(len(row) == grid_format for row in grid):
            error_count+=1

        # Check that each number appears exactly once per row
        if not all(set(row) == digits for row in grid):
            error_count+=1

        # Check that each number appears exactly once per column
        columns = [[row[c] for row in grid] for c in range(4)]
        if not all(set(col) == digits for col in columns):
            error_count+=1

        # Check that each number appears exactly once per 3x3 grid
        for row_block, col_block in product(threes, threes):
            block = [grid[r][c] for r, c in product(row_block, col_block)]
            if set(block) != digits:
                error_count+=1

        return error_count

    def encode_board_to_binary(self, board):
        """ Given a board encode it to binary format and return it """
        binary_board= np.zeros((9, 9, 9)).tolist()
        if self.grid_9x9 is False:
            binary_board= np.zeros((4, 4, 4)).tolist()

        for row_index, row in enumerate(board):
            for column_index, cell in enumerate(row):
                if cell>0:
                    binary_board[cell-1][row_index][column_index]=1
        return binary_board

    def decode_board_from_binary(self, binary_board):
        """ Given a board decode it from binary format and return it """

        board= np.zeros((9, 9))
        if self.grid_9x9 is False:
            board= np.zeros((4, 4))

        for k, color in enumerate(binary_board):
            for i, row in enumerate(color):
                for j, cell_value in enumerate(row):
                    if cell_value>0:
                        board[i][j]+=int(k+1)
                    else:
                        board[i][j]+=int(0)
        return board
