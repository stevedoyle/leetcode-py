# Title: Sudoku Solver
# URL: https://leetcode.com/problems/sudoku-solver/
# Difficulty: Hard

from typing import List
from itertools import chain
import pprint


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solveSudokuHelper(board, 0, 0)

    # Takes a partially filled-in grid and attempts
    # to assign values to all unassigned locations in
    # such a way to meet the requirements for
    # Sudoku solution (non-duplication across rows,
    # columns, and boxes) */
    def solveSudokuHelper(self, grid, row, col):
        # Check if we have reached the 8th
        # row and 9th column (0
        # indexed matrix) , we are
        # returning true to avoid
        # further backtracking
        if row == 9 - 1 and col == 9:
            return True

        # Check if column value  becomes 9 ,
        # we move to next row and
        # column start from 0
        if col == 9:
            row += 1
            col = 0

        # Check if the current position of
        # the grid already contains
        # value >0, we iterate for next column
        if grid[row][col] != ".":
            return self.solveSudokuHelper(grid, row, col + 1)
        for num in range(1, 9 + 1, 1):
            # Check if it is safe to place
            # the num (1-9)  in the
            # given row ,col  ->we
            # move to next column
            if isSafe(grid, row, col, num):
                # Assigning the num in
                # the current (row,col)
                # position of the grid
                # and assuming our assigned
                # num in the position
                # is correct
                grid[row][col] = str(num)

                # Checking for next possibility with next
                # column
                if self.solveSudokuHelper(grid, row, col + 1):
                    return True

            # Removing the assigned num ,
            # since our assumption
            # was wrong , and we go for
            # next assumption with
            # diff num value
            grid[row][col] = "."
        return False


# Checks whether it will be
# legal to assign num to the
# given row, col
def isSafe(grid, row, col, num):

    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(9):
        if grid[row][x] == str(num):
            return False

    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(9):
        if grid[x][col] == str(num):
            return False

    # Check if we find the same num in
    # the particular 3*3 matrix,
    # we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == str(num):
                return False
    return True


def printBoard(board):
    for row in board:
        txt = " ".join(row)
        print(txt)
    print("")


def printCandidates(candidates):
    for row in candidates:
        print(row)
    print("")


class TestSolveSudoku:

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
        expected = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        s = Solution()
        s.solveSudoku(board)
        assert board == expected

    def test_example2(self):
        board = [
            [".", ".", "9", "7", "4", "8", ".", ".", "."],
            ["7", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "2", ".", "1", ".", "9", ".", ".", "."],
            [".", ".", "7", ".", ".", ".", "2", "4", "."],
            [".", "6", "4", ".", "1", ".", "5", "9", "."],
            [".", "9", "8", ".", ".", ".", "3", ".", "."],
            [".", ".", ".", "8", ".", "3", ".", "2", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "6"],
            [".", ".", ".", "2", "7", "5", "9", ".", "."],
        ]
        expected = [
            ["5", "1", "9", "7", "4", "8", "6", "3", "2"],
            ["7", "8", "3", "6", "5", "2", "4", "1", "9"],
            ["4", "2", "6", "1", "3", "9", "8", "7", "5"],
            ["3", "5", "7", "9", "8", "6", "2", "4", "1"],
            ["2", "6", "4", "3", "1", "7", "5", "9", "8"],
            ["1", "9", "8", "5", "2", "4", "3", "6", "7"],
            ["9", "7", "5", "8", "6", "3", "1", "2", "4"],
            ["8", "3", "2", "4", "9", "1", "7", "5", "6"],
            ["6", "4", "1", "2", "7", "5", "9", "8", "3"],
        ]
        s = Solution()
        s.solveSudoku(board)
        assert board == expected
