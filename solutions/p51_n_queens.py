# Title: N-Queens
# URL: https://leetcode.com/problems/n-queens/
# Difficulty: Hard

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row, diagonals, anti_diagonals, cols, state):
            # base case - N queens have been placed
            if row == n:
                result.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # if the queen is not placeable
                if (
                    col in cols
                    or curr_diagonal in diagonals
                    or curr_anti_diagonal in anti_diagonals
                ):
                    continue

                # place the queen
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"

                # move on to the next row
                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                # Remove the queen from the board since we are backtracking
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."

        result = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return result


class TestSolveNQueens:
    def test_example1(self):
        expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        assert Solution().solveNQueens(4) == expected

    def test_example2(self):
        expected = [["Q"]]
        assert Solution().solveNQueens(1) == expected
