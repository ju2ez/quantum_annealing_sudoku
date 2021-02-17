"""Tests for Quantum Annealing Sudoku"""
import pytest #pylint: disable=[W0611]
from quantum_annealing_sudoku import quantum_annealing_sudoku


class TestCheckBoard:
    """Tests for the Sudoku QA"""

    @pytest.fixture
    def grid_9x9(self):
        grid_9x9 = quantum_annealing_sudoku.QuantumAnnealingSudoku(grid_9x9=True)
        return grid_9x9

    @pytest.fixture
    def grid_4x4(self):
        grid_4x4 = quantum_annealing_sudoku.QuantumAnnealingSudoku(grid_9x9=False)
        return grid_4x4

    def test_valid_board_x4(self, grid_4x4):
        valid_board= ((1,2,3,4),
        (4,3,2,1),
        (2,1,4,3),
        (3,4,1,2),
        )

        assert grid_4x4.check_sudoku(valid_board) == 0

    def  test_invalid_board_x4(self, grid_4x4):
        invalid_board= ((1,2,0,0),
         (0,0,0,0),
         (0,0,1,0),
         (0,0,4,0),
        )

        assert grid_4x4.check_sudoku(invalid_board) > 0



    def test_valid_board_x9(self, grid_9x9):
        valid_board =((5, 3, 7, 8, 9, 1, 6, 4, 2),
         (2, 6, 1, 7, 5, 4, 3, 9, 8),
         (8, 9, 4, 6, 3, 2, 1, 7, 5),
         (7, 1, 5, 3, 6, 8, 4, 2, 9),
         (3, 8, 2, 4, 1, 9, 7, 5, 6),
         (6, 4, 9, 2, 7, 5, 8, 1, 3),
         (9, 7, 3, 1, 2, 6, 5, 8, 4),
         (1, 2, 8, 5, 4, 3, 9, 6, 7),
         (4, 5, 6, 9, 8, 7, 2, 3, 1))
        assert grid_9x9.check_sudoku(valid_board) == 0

    def test_invalid_board_x9(self, grid_9x9):
        invalid_board = ((0, 0, 3, 0, 2, 0, 6, 0, 0),
                 (9, 0, 0, 3, 0, 5, 0, 0, 1),
                 (0, 0, 1, 8, 0, 6, 4, 0, 0),
                 (0, 0, 8, 1, 0, 2, 9, 0, 0),
                 (7, 0, 0, 0, 0, 0, 0, 0, 8),
                 (0, 0, 6, 7, 0, 8, 2, 0, 0),
                 (0, 0, 2, 6, 0, 9, 5, 0, 0),
                 (8, 0, 0, 2, 0, 3, 0, 0, 9),
                 (0, 0, 5, 0, 1, 0, 3, 0, 0))
        assert grid_9x9.check_sudoku(invalid_board) > 0
