# Title: Game of Life
# URL: https://leetcode.com/problems/game-of-life/
# Difficulty: Medium

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows, ncols = len(board), len(board[0])
        next_board = [[0] * ncols for _ in range(nrows)]

        for i in range(nrows):
            for j in range(ncols):
                live_neighbors = 0
                for x in range(max(0, i - 1), min(nrows, i + 2)):
                    for y in range(max(0, j - 1), min(ncols, j + 2)):
                        if x == i and y == j:
                            continue
                        live_neighbors += board[x][y]

                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        next_board[i][j] = 0
                    else:
                        next_board[i][j] = 1
                else:
                    if live_neighbors == 3:
                        next_board[i][j] = 1

        for i in range(nrows):
            for j in range(ncols):
                board[i][j] = next_board[i][j]


class TestGameOfLife:
    def test_example1(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        Solution().gameOfLife(board)
        assert board == expected

    def test_example2(self):
        board = [[1, 1], [1, 0]]
        expected = [[1, 1], [1, 1]]
        Solution().gameOfLife(board)
        assert board == expected
