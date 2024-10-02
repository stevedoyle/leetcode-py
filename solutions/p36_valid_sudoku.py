# Title: 36. Valid Sudoku
# URL: https://leetcode.com/problems/valid-sudoku/
# Difficulty: Medium

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check for valid rows
        for row in board:
            if not self.isValidGroup(row):
                return False

        # Check for valid columns
        for col_idx in range(9):
            col = [board[row_idx][col_idx] for row_idx in range(9)]
            if not self.isValidGroup(col):
                return False

        # Check for valid 3x3 grids
        grp_origins = [
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        ]
        for origin in grp_origins:
            grp = [
                board[row_idx][col_idx]
                for col_idx in range(origin[1], origin[1] + 3)
                for row_idx in range(origin[0], origin[0] + 3)
            ]
            if not self.isValidGroup(grp):
                return False

        return True

    def isValidGroup(self, grp):
        tracker = set()
        for cell in grp:
            if cell == ".":
                continue
            if cell in tracker:
                return False
            tracker.add(cell)
        return True


class TestIsValidSudoku:
    def test_isValidGroup(self):
        grp = ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        assert Solution().isValidGroup(grp)

        grp = ["5", "3", ".", ".", "7", ".", ".", ".", "5"]
        assert not Solution().isValidGroup(grp)

    def test_example1(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        solution = Solution()
        assert solution.isValidSudoku(board)

    def test_example2(self):
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        solution = Solution()
        assert not solution.isValidSudoku(board)
