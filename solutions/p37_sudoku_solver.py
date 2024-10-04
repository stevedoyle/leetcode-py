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
        if not self.isValidSudoku(board):
            return

        if self.isSolved(board):
            return

        printBoard(board)

        candidates = self.getCandidates(board)
        # print(f"candidates[2][0]: {candidates[2][0]}")
        # print(f"{candidates}")
        changed = True
        while changed:
            candidates = self.getCandidates(board)
            changed = self.promoteSingleCandidates(board, candidates)
            if changed:
                candidates = self.getCandidates(board)
            changed |= self.promoteUniqueCandidates(board, candidates)
            printBoard(board)
        printCandidates(candidates)

    def promoteUniqueCandidates(self, board, candidates):
        changed = False
        for row_idx in range(9):
            row_candidates = self.getRowValues(candidates, row_idx)
            counts = {}
            row_candidates = [x for rc in row_candidates for x in rc]
            for c in row_candidates:
                if c not in counts:
                    counts[c] = 0
                counts[c] += 1
            for k, v in counts.items():
                if v == 1:
                    for col_idx in range(9):
                        if k in candidates[row_idx][col_idx]:
                            board[row_idx][col_idx] = k
                            changed = True
                            candidates[row_idx][col_idx] = []
                            break

        for col_idx in range(9):
            col_candidates = self.getColValues(candidates, col_idx)
            counts = {}
            col_candidates = [x for cc in col_candidates for x in cc]
            for c in col_candidates:
                if c not in counts:
                    counts[c] = 0
                counts[c] += 1
            for k, v in counts.items():
                if v == 1:
                    for row_idx in range(9):
                        if k in candidates[row_idx][col_idx]:
                            board[row_idx][col_idx] = k
                            changed = True
                            candidates[row_idx][col_idx] = []
                            break

        for row_offset in range(0, 9, 3):
            for col_offset in range(0, 9, 3):
                grid_candidates = self.getSubgridValues(
                    candidates, row_offset, col_offset
                )
                counts = {}
                grid_candidates = [x for gc in grid_candidates for x in gc]
                for c in grid_candidates:
                    if c not in counts:
                        counts[c] = 0
                    counts[c] += 1
                for k, v in counts.items():
                    if v == 1:
                        for row_idx in range(3):
                            for col_idx in range(3):
                                if (
                                    k
                                    in candidates[row_offset + row_idx][
                                        col_offset + col_idx
                                    ]
                                ):
                                    board[row_offset + row_idx][
                                        col_offset + col_idx
                                    ] = k
                                    changed = True
                                    candidates[row_offset + row_idx][
                                        col_offset + col_idx
                                    ] = []
        return changed

    def promoteSingleCandidates(self, board, candidates):
        changed = False
        for row_idx in range(9):
            for col_idx in range(9):
                if len(candidates[row_idx][col_idx]) == 1:
                    board[row_idx][col_idx] = candidates[row_idx][col_idx][0]
                    candidates[row_idx][col_idx] = []
                    changed = True
        return changed

    def getCandidates(self, board):
        nums = [str(n) for n in range(1, 10)]
        candidates = []
        for row_idx in range(9):
            row_candidates = []
            row_values = self.getRowValues(board, row_idx)
            # print(f"Row Values [{row_idx}] = {row_values}")
            for col_idx in range(9):
                if board[row_idx][col_idx] == ".":
                    col_values = self.getColValues(board, col_idx)
                    grid_values = self.getSubgridValues(board, row_idx, col_idx)
                    # print(f"Grid Values [{row_idx}][{col_idx}] = {grid_values}")
                    # print(f"Col Values  [{row_idx}][{col_idx}] = {col_values}")
                    already_used = row_values.copy()
                    already_used.extend(col_values)
                    already_used.extend(grid_values)
                    already_used = list(set(already_used))
                    c = [x for x in nums if x not in already_used]
                    row_candidates.append(c)
                    # print(f"[{row_idx}][{col_idx}] {already_used}")
                else:
                    row_candidates.append([])
            candidates.append(row_candidates)
        return candidates

    def getRowValues(self, board, row_idx):
        return [
            board[row_idx][col_idx]
            for col_idx in range(9)
            if board[row_idx][col_idx] != "."
        ]

    def getColValues(self, board, col_idx):
        return [
            board[row_idx][col_idx]
            for row_idx in range(9)
            if board[row_idx][col_idx] != "."
        ]

    # Subgrid indices:
    #   0 1 2
    #   3 4 5
    #   6 7 8
    def getSubgridValues(self, board, row, col):
        origin_row = row - (row % 3)
        origin_col = col - (col % 3)
        return [
            board[origin_row + row_offset][origin_col + col_offset]
            for row_offset in range(3)
            for col_offset in range(3)
            if board[origin_row + row_offset][origin_col + col_offset] != "."
        ]

    def isSolved(self, board):
        for row in board:
            if "." in row:
                return False
        return True

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
    def makeEmptyBoard(self):
        return [["." for _ in range(9)] for _ in range(9)]

    def test_getGridValues(self):
        board = self.makeEmptyBoard()
        board[0][0] = "5"
        board[0][1] = "3"
        board[1][0] = "6"
        board[2][1] = "9"
        board[2][2] = "8"
        expected = ["3", "5", "6", "8", "9"]
        actual = sorted(Solution().getSubgridValues(board, 0, 0))
        assert actual == expected
        expected = ["3", "5", "6", "8", "9"]
        actual = sorted(Solution().getSubgridValues(board, 1, 1))
        assert actual == expected
        expected = ["3", "5", "6", "8", "9"]
        actual = sorted(Solution().getSubgridValues(board, 2, 2))
        assert actual == expected

    def test_getGridValues2(self):
        board = self.makeEmptyBoard()
        board[0][3] = "5"
        board[0][4] = "3"
        board[1][3] = "6"
        board[2][4] = "9"
        board[2][5] = "8"
        expected = ["3", "5", "6", "8", "9"]
        actual = sorted(Solution().getSubgridValues(board, 0, 3))
        assert actual == expected
        expected = ["3", "5", "6", "8", "9"]
        actual = sorted(Solution().getSubgridValues(board, 1, 4))
        assert actual == expected
        expected = ["3", "5", "6", "8", "9"]
        actual = sorted(Solution().getSubgridValues(board, 2, 5))
        assert actual == expected

    def test_getCandidates(self):
        board = self.makeEmptyBoard()
        candidates = Solution().getCandidates(board)
        assert len(candidates) == 9
        assert len(candidates[0]) == 9
        assert candidates[8][8] == [str(n) for n in range(1, 10)]

        board[8][8] = "1"
        candidates = Solution().getCandidates(board)
        assert candidates[6][6] == [str(n) for n in range(2, 10)]
        assert candidates[7][7] == [str(n) for n in range(2, 10)]
        assert candidates[8][8] == []

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
