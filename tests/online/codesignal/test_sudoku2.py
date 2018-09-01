class TestSudoku2(object):

    def test_grid_good(self):
        grid = [
            [".",".",".","1","4",".",".","2","."],
            [".",".","6",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".","1",".",".",".",".",".","."],
            [".","6","7",".",".",".",".",".","9"],
            [".",".",".",".",".",".","8","1","."],
            [".","3",".",".",".",".",".",".","6"],
            [".",".",".",".",".","7",".",".","."],
            [".",".",".","5",".",".",".","7","."],
        ]
        assert sudoku2(grid) is True

    def test_grid_bad(self):
        grid = [
            [".",".",".",".","2",".",".","9","."],
            [".",".",".",".","6",".",".",".","."],
            ["7","1",".",".","7","5",".",".","."],
            [".","7",".",".",".",".",".",".","."],
            [".",".",".",".","8","3",".",".","."],
            [".",".","8",".",".","7",".","6","."],
            [".",".",".",".",".","2",".",".","."],
            [".","1",".","2",".",".",".",".","."],
            [".","2",".",".","3",".",".",".","."],
        ]
        assert sudoku2(grid) is False
